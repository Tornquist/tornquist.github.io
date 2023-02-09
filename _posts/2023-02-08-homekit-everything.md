---
layout: post
title: HomeKit Everything
date: 2023-02-08 22:00:00
categories: programming
---

I'm a huge fan of single-day household projects. Better light switches, a new faucet, etc. Small things that make our home nicer or easier.

A few years ago I wrote about using HomeKit + Homebridge to automate turning our
[HVAC off and back on][ac] so we could hear the tv. Since then I've done a
handful of other projects that get used every day, such as:

1. [Using HomeKit to avoid walking down two flights of stairs before bed](#front-door-security)
1. [Fixing a design problem with my bedroom closet](#closet-lights)
1. [Adding a switch to HomeKit to turn on my desktop computer](#pc-power)

There are even smaller projects like [using an adapter][belkin] so that I can
airplay to my stereo, or [turn on my kitchen lights][dimmer] with my voice to
make washing dishes easier.

I really enjoy the feeling of a project that "just works."

### Front Door Security
-----------------------

**Prompt**

I live in an apartment with two flights of stairs. You walk up stairs from the
front door to the main living space, and then another flight up to the bedrooms.
This is fine except when you're laying in bed at night and wonder if you've
closed and locked the front door. Then those stairs are _awful_.

**Supplies**

* HomeKit adapter board for hard wired sensors
* Smart door lock

**Configuration**

My home was wired with a built-in security system. Using the adapter board I was
able to expose the states of hard wired sensors into HomeKit to report if the
door is open or closed.

The smart lock when integrated with HomeKit provides lock state.

Knowing the door is closed does not tell you anything about if it's locked.
Knowing the door is locked isn't helpful if it was locked open. With these two
pieces of information I configured a shortcut to read both values and respond
with a specific phrase to let me know that everything is okay.

<details><summary>View the automation</summary>
<p>
{% include photo.html img="/assets/2023/02/is-my-home-secure.png" %}
</p>
</details>

I can now tap the shortcut on my phone, or ask Siri &ldquo;Hey Siri, is my home
secure?&rdquo; and I'll immediately know if it's both closed and locked. I can
trigger this with my phone, through our HomePod before bed, in my car with
CarPlay while driving away, etc. This completely solved the nagging questions.

### Closet Lights
-----------------

**Prompt**

Our bedroom has a walk-in closet with a light switch outside of the door on the
hinge side. This means that it's impossible to turn on the closet lights without
lighting up the main bedroom. You can't reach around a mostly closed door.

For about a year my wife or I would use our cell phone flashlights in the 
closet while getting ready early to avoid waking the other. It was far less than
ideal.

If I just put a new switch inside the closet, it would also be on the hinge side
which didn't feel natural when entering the room. I couldn't run wiring to the
right side of the door without going up and around the doorframe. I couldn't put
a  normal smart bulb in without having an always-on switch outside of the room
(or removing the switch completely).

**Supplies**

* [Caseta In-Wall Smart Dimmer Switch Expansion Kit][dimmer]
* [Caseta Smart Hub][hub]

**Configuration**

I replaced the external light switch with a Caseta Smart Dimmer so that the
physical switch would still control the lights. Inside the room I mounted the
pico smart remote (companion for switch) at normal switch height where your hand
would naturally reach when walking in the room.

This is exposed to HomeKit with the Caseta bridge, but that's not really needed.
The built-in switches cover 99% percent of our usage. Caseta was the only
hardware configuration that would let us keep the original wiring as the control
for the light without having to remove or wire a ciruit always on.

### PC Power
------------

**Prompt**

I have a Windows PC in my entertainment center. It's a gaming computer + Quicken
machine. I use Quicken for Windows from my mac via RDP. When I want to use
Quicken, I have to get up to turn on the computer. It's minor, but it means that 
I cannot just open Quicken like other applications on my computer. For many
reasons&trade; I don't use Quicken in a VM.

**Supplies**

* PC with a network card that supports Wake-on-LAN (WoL)
* [TP-Link Powerline Adapter][powerline]
* Router with dedicated mac/IP configuration
* HomeBridge

**Configuration**

To avoid having to get up to turn on the computer, I use HomeKit to trigger
a WoL packet to be sent to the machine. The Homebridge extension also regularly 
pings the computer to report if it's on or off.

All together this gives me a switch in HomeKit that I can use to turn my computer
on.

**Expanded steps**

1. Connect the computer to the router via powerline adapter<br/>_I had no way to
    run a direct ethernet line_
1. [Enable WoL in the computer's BIOS](https://web.archive.org/web/20230123213604/https://www.asus.com/support/FAQ/1045950/)
1. [Enable support for the network card in device manager](https://web.archive.org/web/20230123213730/https://www.windowscentral.com/how-enable-and-use-wake-lan-wol-windows-10)
1. [Set designated IP/MAC address lock in router](https://web.archive.org/web/20230123213706/https://www.math.cmu.edu/~gautam/sj/blog/20200406-tplink-wol.html)
1. [Increase network priority of wifi to make sure wifi is used once booted](https://web.archive.org/web/20230123213414/https://www.tenforums.com/tutorials/92180-change-network-adapter-connection-priorities-windows-10-a.html)
1. [Enable ping in Windows](https://activedirectorypro.com/allow-ping-windows-firewall)<br/>_So that the homebridge-wol extension can check on/off status_
1. [Hide 'shutdown' from the Windows start menu](https://community.spiceworks.com/topic/2279159-hideshutdown-no-longer-working-consistently)<br/>_Windows 10 only supports WoL from sleep_
1. Configure the Homebridge WoL plugin using the computer's mac and IP addresses

[ac]: {% post_url 2020-08-29-homekit-ac-automation %}
[dimmer]: https://www.casetawireless.com/us/en/products/dimmers-switches
[hub]: https://www.casetawireless.com/us/en/products/expansion-kits-and-smart-bridge
[powerline]: https://www.amazon.com/TP-LINK-Powerline-Pass-Through-TL-PA9020P-KIT/dp/B01H74VKZU
[belkin]: https://www.belkin.com/audio-adapter-with-airplay-2/P-AUZ002.html