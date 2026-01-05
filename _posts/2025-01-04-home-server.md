---
layout: post
title: Home Server
date: 2025-01-04 12:00:00
categories: programming
---

## Overview

I've been running a set of APIs on Digital Ocean and a second set of smart home
applications on a Raspberry Pi for the last 6 years or so. Originally I had
planned to publicly launch [Time][t] and wanted to prepare for isolation, but
I ended up deciding just keeping the application for my own use.

After 6 years, both servers were out long term support on their base OSs and
were due for an update. I took advantage of the opportunity to consoldiate and
containerize everything with a focus on an easier to update and manage
environment.

My primary goal was to address difficulty with updates and ensure that I could
easily keep both nodes up to date with all security updates. The Pi and droplet
had bare metal installs. Each was relatively simple, but this made it more
difficult to update the applications and base OS, and increased the likelihood
of one update breaking another. Containers should make it easier to update the
base hardware and specific applications in isolation.

The final result is _very_ similar to what I started with. All the same apps are
running (just in containers), the same networking is supported (with a UI vs
nginx), and it continues to be stable. The main outcome and goal was met as and
I've also reduced my reocurring monthly costs (after spending more up front).

## Application Overview

In my original configuration, the Raspberry Pi ran all home-focuced software
including [homebridge](https://homebridge.io/),
[pi hole](https://pi-hole.net/), and a [vpn](https://www.wireguard.com/). The
droplet ran an API for Time, for Uplink, and supporting the routing (nginx/pm2)
and databases (mysql) for each.

When moving everything to containers, all for same infrastructure would be
running, but nginx/pm2 were replaced with [traefik][tt]/[portainer][p] and I
needed to ensure that I could properly containerize everything.

I had a handful of problems moving from bare metal installs. The homebridge
container is designed for host networking, DNS settings made it a bit slow to
migrate the PiHole install, and the VPN was the hardest of all. I ended up just
running wg-easy (a version of wireguard already set up for a container install). 

* Bare metal
  * docker
  * backup scripts
* Docker
  * Infra management containers
    * portainer -- container management gui
    * traefik -- proxy/routing
    * autoheal -- container restart
  * Personal/Home containers
    * homebridge -- smart home
    * wg-easy -- vpn
    * pihole -- ad blocker
  * Time API containers
    * time-api
    * time-db
  * Uplink API containers
    * uplink-api
    * uplink-db

On the hardware side, I have a running Pi5, [SSD][ssd] hat, [PoE][poe] hat and
unfortunantly chunky [case][case] for the entire setup.

## General Setup

1. Setup the pi: Assemble, flash disk image, configure SSH, etc.
1. Update everything
```
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```
1. Setup docker
   1. Install docker ([docs][d-docs]) 
   1. Add user to docker group `sudo usermod -a -G docker $USER` (required for
      portainer, and to avoid `sudo` for every docker command)
1. Setup Portainer
    1. Install ([docs][p-docs])
        * Doc tip: In my case, I _did_ need port 9000 mapped because this is what
          I mapped in Traefik. Just stay consistent.
    2. Navigate to Portainer url (In my case, `raspberrypi.local:9443`)
    3. Create Portainer user through UI

At this point you're ready for containers.

## Containers

Docker compose is a tool to configure and link multiple docker containers
together. Each compose file will correspond to one application.

I ended up with a few main networks.

* **Host**: homebridge and Glances (system monitoring)
* **pihole**: pihole
* **time**: time API, time DB, Traefik
* **uplink**: uplink API, uplink DB, Traefik
* **traefik**: traefik, vpn, speedtest tracker (general testing)

The reason I attached the vpn and speedtest directly to the Traefik network
was because it was easier than standing up two more and adding them to the
traefik compose file. This traefik network is effectively the default network.

<details>
<summary>
<b>traefik.yaml</b> -- This serves as the main networking/routing hub for the entire
setup. Traefik reads a config file (below) as well as docker tags (ex: time) to
construct the routing and renew ssl certs with letsencrypt.
</summary>
<!-- language: lang-yaml -->
<pre><code>
networks:
    default:
    time-api_time-api-network:
        external: true
    uplink-analytics-api_uplink-network:
        external: true


volumes:
    letsencrypt:

services:
    traefik:
        image: "traefik:v3.6"
        container_name: "traefik"
        command:
            - "--log.level=DEBUG"
            - "--api.insecure=true"
            - "--providers.docker=true"
            - "--providers.docker.exposedbydefault=false"
            - "--providers.file.filename=/dynamic-config/traefik.yml"
            - "--entryPoints.web.address=:80"
            - "--entryPoints.websecure.address=:443"
            
            - "--certificatesresolvers.tlsResolver.acme.tlschallenge=true"
            - "--certificatesresolvers.tlsResolver.acme.email=xxx"
            - "--certificatesresolvers.tlsResolver.acme.storage=/letsencrypt/acme.json"

            - "--certificatesresolvers.route53.acme.email=xxx"

            - "--certificatesresolvers.route53.acme.dnschallenge=true"
            - "--certificatesresolvers.route53.acme.dnschallenge.provider=route53"
            - "--certificatesresolvers.route53.acme.storage=/letsencrypt/acmeRoute53.json"
            
            - "--entrypoints.web.http.redirections.entrypoint.to=websecure" # Automatic http redirect
            - "--entrypoints.web.http.redirections.entrypoint.scheme=https" # Automatic http redirect
    ports:
        - "80:80"
        - "443:443"
        - "8080:8080"
    environment:
        - "AWS_ACCESS_KEY_ID=xxx"
        - "AWS_SECRET_ACCESS_KEY=xxx"
        - "AWS_REGION=xxx"
        - "AWS_HOSTED_ZONE_ID=xxx"
    restart: unless-stopped
    networks:
        - default
        - time-api_time-api-network
        - uplink-analytics-api_uplink-network

    volumes:
        - letsencrypt:/letsencrypt
        - "/home/pi/Config/Traefik:/dynamic-config/"
        - "/var/run/docker.sock:/var/run/docker.sock:ro"
</code></pre>
</details>
<p></p>
<details>
<summary>
<b>homebridge.yaml</b> -- Homebridge is a tool to map smart devices into HomeKit. It's
a critical piece of my smart home setup.
</summary>
<!-- language: lang-yaml -->
<pre><code>
version: '3'
volumes:
    homebridge:
services:
    homebridge:
        image: homebridge/homebridge:ubuntu
        container_name: homebridge
        restart: always
        network_mode: host
        environment:
            - HOMEBRIDGE_CONFIG_UI_PORT=8581
        volumes:
            - homebridge:/homebridge
        # labels:
            # - "traefik.*" # Stored in dynamic configuration due to host networking
</code></pre>
</details>
<p></p>
<details>
<summary>
<b>pihole.yaml</b> -- PiHole is a whole-home VPN. This is the second foundational app
from the original raspberry pi setup.
</summary>
<!-- language: lang-yaml -->
<pre><code>
version: "3"
volumes:
    etc_pihole:
    etc_dnsmasq:
services:
    pihole:
        container_name: pihole
        image: pihole/pihole:latest
        ports:
            - "53:53/tcp"
            - "53:53/udp"
            - "67:67/udp"
            - "8083:80/tcp"

        environment:
            TZ: 'America/Chicago'
            WEBPASSWORD: 'xxx'
        # Volumes store your data between container upgrades
        volumes:
            - etc_pihole:/etc/pihole/
            - etc_dnsmasq:/etc/dnsmasq.d/
        cap_add:
            - NET_ADMIN
        restart: unless-stopped
</code></pre>
</details>
<p></p>
<details>
<summary>
<b>vpn.yaml</b> -- Whole home VPN for remote access. With my cell phone and laptop
automatically connecting when away, all local domains are always available for
my main devices.
</summary>
<!-- language: lang-yaml -->
<pre><code>
volumes:
    etc_wireguard:
networks:
    traefik_default:
        external: true
services:
    wg-easy:
        environment:
            - LANG=en
            - WG_HOST=xxx
            - PASSWORD_HASH=xxx

        image: ghcr.io/wg-easy/wg-easy
        container_name: wg-easy
        volumes:
            - etc_wireguard:/etc/wireguard
        ports:
            - "51820:51820/udp"
            - "51821:51821/tcp"
        networks:
            traefik_default:
        restart: unless-stopped
        cap_add:
            - NET_ADMIN
            - SYS_MODULE
        sysctls:
            - net.ipv4.ip_forward=1
            - net.ipv4.conf.all.src_valid_mark=1
        labels:
            - "traefik.enable=true"
            - "traefik.http.services.wireguard.loadbalancer.server.port=51821" # UI, not vpn
            - "traefik.http.routers.wireguard.rule=Host(`wireguard.xxx`)"
            - "traefik.http.routers.wireguard.entrypoints=websecure"
            - "traefik.http.routers.wireguard.tls.certresolver=route53"
</code></pre>
</details>
<p></p>
<details>
<summary>
<b>autoheal.yaml</b> -- Monitor and restart containers with the `restart` configuration.
This replaces pm2 from the original digital ocean configuration.
</summary>
<!-- language: lang-yaml -->
<pre><code>
services:
  autoheal:
    image: willfarrell/autoheal:latest
    network_mode: none
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
</code></pre>
</details>
<p></p>
<details>
<summary>
<b>time.yaml</b> -- Time API and DB. This is what enabled the migration from Digital
Ocean to a single device.
</summary>
<!-- language: lang-yaml -->
<pre><code>
volumes:
    db:
networks:
    time-api-network:

services:
    api:
        image: tornquist/time-api:20250118
        restart: unless-stopped
        depends_on:
            db:
                condition: service_healthy
        environment:
            SERVER_PORT: 8000
            DB_HOST: db # Will resolve to local docker ip
            DB_PORT: 3306 # Use internal network port
            DB_NAME: abc
            DB_USER: def
            DB_PASS: ghi
        ports:
            - 8001:8000
        networks:
            time-api-network:
        post_start:
            - command: "npm --prefix node_modules/time-core run db-up"
        labels:
            - "autoheal=true"
            - "traefik.enable=true"
            - "traefik.http.routers.time-api.rule=Host(`host`)"
            - "traefik.http.routers.time-api.entrypoints=websecure"
            - "traefik.http.routers.time-api.tls.certresolver=tlsResolver"
    db:
        image: bitnami/mysql:5.7.43
        restart: unless-stopped
        environment:
            MYSQL_ROOT_PASSWORD: xyz
            MYSQL_DATABASE: abc
            MYSQL_USER: def
            MYSQL_PASSWORD: ghi
        ports:
            - 3307:3306
        networks:
            time-api-network:
        labels:
            - "autoheal=true"
        healthcheck:
            test: ["CMD", "mysqladmin", "--user=root", "--password=xyz","ping", "-h", "localhost"]
            timeout: 20s
            retries: 10
        volumes:
            - db:/bitnami/mysql/data
</code></pre>
</details>

## Traefik

On the Time/Uplink containers, I was able to use docker labels to config
Traefik. The labels look like this:

```yaml
labels:
    - "traefik.enable=true"
    - "traefik.http.routers.time-api.rule=Host(...)"
    - "traefik.http.routers.time-api.entrypoints=websecure"
    - "traefik.http.routers.time-api.tls.certresolver=tlsResolver"
```

With this in place the proxy will exist when the container is running and be
disabled when the container stops. Traefik has permissions through an AWS IAM
role to put the proper DNS records in place to enable SSL cert generation.

I have public DNS records for my public APIs, but everything behind the firewall
is not listed online. I have a single A record for `*.local.nathantornquist.com`
that refers to the pi's internal IP address `192.168.0.139`. For Traefik to
generate SSL certs for these sites, I was required to use a config file instead.

Docker tags do not work.

The file is below. This took a bit to sort out, but once it was in place I had
proper SSL and routing for both my public records and internal records.

<details>
<summary>taefik.yml</summary>
<!-- language: lang-yaml -->
<pre><code>
http:
    services:
        glances:
            loadBalancer:
                servers:
                    - url: "http://192.168.0.139:61208"
        homebridge:
            loadBalancer:
                servers:
                    - url: "http://192.168.0.139:8581"
        traefik:
            loadBalancer:
                servers:
                    - url: "http://192.168.0.139:8080/"
        pihole:
            loadBalancer:
                servers:
                    - url: "http://192.168.0.139:8083/"
        portainer:
            loadBalancer:
                servers:
                    - url: "http://192.168.0.139:9000/"
    routers:
        glances:
            rule: Host(`glances.local.nathantornquist.com`)
            entrypoints: websecure
            service: glances
            tls:
                certresolver: route53
        homebridge:
            rule: Host(`homebridge.local.nathantornquist.com`)
            entrypoints: websecure
            service: homebridge
            tls:
                certresolver: route53
        traefik:
            rule: Host(`traefik.local.nathantornquist.com`)
            entrypoints: websecure
            service: traefik
            tls:
                certresolver: route53
        pihole:
            rule: Host(`pihole.local.nathantornquist.com`)
            entrypoints: websecure
            service: pihole
            middlewares:
                - pihole-redirect
            tls:
                certresolver: route53
        portainer:
            rule: Host(`portainer.local.nathantornquist.com`)
            entrypoints: websecure
            service: portainer
            tls:
                certresolver: route53
    middlewares:
        pihole-redirect:
            redirectRegex:
                permanent: true
                regex: "^https://pihole.local.nathantornquist.com/?$"
                replacement: "https://pihole.local.nathantornquist.com/admin"

</code></pre>
</details>

## Networking

* time.nathantornquist.com points to the server with my networking hardware
  and traefik acting as a firewall and proxy.
* uplink.nathantornquist.com is configured like time.nathantornquist.com
* *.local.nathantornquist.com is everything else, and is registered with a local
  IP address that only resolves within my network.

Internally I've forwarded ports from my public IP to the server as needed and
have the pi set on a static IP address.

To make sure that everything continues to work if my IP address chagnes, I have
a script running on the pi that will update the public DNS records if my IP
changes. This is run every few minutes via cron:

```
*/15 * * * * ZONE=xxx NAME_TAG=time.nathantornquist.com bash /home/pi/Scripts/update-dns.sh >/dev/null 2>&1
*/15 * * * * ZONE=xxx NAME_TAG=uplink.nathantornquist.com bash /home/pi/Scripts/update-dns.sh >/dev/null 2>&1
```

<details>
<summary>update-dns.sh</summary>
<!-- language: lang-yaml -->
<pre><code>
#!/bin/bash
set -e

if [ -z "$ZONE" ]
then
    echo "ZONE is required"
    exit 1
fi
if [ -z "$NAME_TAG" ]
then
    echo "NAME_TAG is required"
    exit 1
fi

MY_IP=$(curl -f ifconfig.me)

aws route53 change-resource-record-sets --hosted-zone-id $ZONE --change-batch '{"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":"'$NAME_TAG'","Type":"A","TTL":1800,"ResourceRecords":[{"Value":"'$MY_IP'"}]}}]}'

echo "Updated $ZONE/$NAME_TAG to $MY_IP"
</code></pre>
</details>

## Backups

The final piece of the puzzle is proper backups. To make sure that I didn't put
myself at risk or lose my data if the device failed I have full backups that run
nightly and back up full docker data as well specific database files.

I wanted to avoid having to coordinate file systems directories or formats so
all docker volumes are isolated to their specific containers. To back them up, I
mount the volumes and dump them individually instead of changing/copying the
files from the root file system.

## Pain Points

While setting all of this up, the primary pain points I had were:

1. **SSD migration**: Normally I install everything on a sd card and the mirror
   that to a USB drive for long term hosting. I tried to do the same with the
   ssd, but had significantly more trouble given the device ID naming baked into
   the ssd.
2. **Routing**: Each docker image/application had particular sensitivities for
   how networking could be configured. I ended up with a mix of host networking
   and proper isolated networking so that the home automation services all
   continued to function.
3. **VPN Functionality:** It was very hard for me to get a working VPN with
   proper loopback and access to the other docker applications and devices on my
   home network. The majority of my iteration was done here.


[t]: {% link _projects/11_time.md %}
[tt]: https://traefik.io/traefik
[h]: {% link _posts/2023-02-08-homekit-everything.md %}
[p]: https://www.portainer.io/
[ssd]: https://shop.pimoroni.com/products/nvme-base?variant=41219587178579
[poe]: https://www.waveshare.com/wiki/PoE_HAT_(F)
[case]: https://makerworld.com/en/models/413567-raspberry-pi-5-poe-nvme-case-waveshare-pimoroni#profileId-315577
[d-docs]: https://docs.docker.com/engine/install/debian/
[p-docs]: https://docs.portainer.io/start/install-ce/server/docker/linux