---
layout: post
title: Garage Networking
date: 2025-02-08 12:00:00
categories: home
---

Our condo building has a callbox with a physical landline. It's reliable and low
maintenance but over the last few years it's become very clear that AT&T is no
longer interested in being in the business of these old phone lines and is
charging as such.

After fighting with AT&T for correct bills and looking at expensive alternatives
I was able to keep the existing system and drive our month by month costs down
to $5 with a VoIP system. **This saves us about $3000 annually** from what we
would have spent if no change had been made.

### AT&T Pricing

In 2023 our plan was $160/mo (~$2000/yr) for the line. In 2024 our legacy
contract expired and the price jumped to $450/mo ($5500/yr). Even after
negotiating down to $270/mo ($3200/yr) the risk and cost was high enough that
it was worth looking at other options.

It was difficult to get AT&T to honor the newly negotiated price (despite the
new contract, issued bills were not updated) and the experience highlighed how
high we could expect the bill to jump in the future.

*Reference:* Original AT&T pricing was $2000/yr

*Option 1:* Stay with AT&T == $3200/yr with the expectation of future increases

### ButterflyMX

I first looked at just switching out the system and going to something newer.
ButterflyMX quoted us $1000 for the hardware (on sale from $3,995) with a
software subscription of $1,200/yr.

We were looking at $100/month on top of the need to get internet for the box.
I was interested in a model with integrated LTE, but those cost even more and
still required a plan. The recommendation was WiFi and internet for the system
would have easily added another $30-60/month and brought us back to where we had
started with AT&T. This all works fine for a building with an office and easy
WiFi, but not for a condo building with no public internet and an outside gate.

*Option 2:* Butterfly MX == $2000/yr + installation costs

### Newer models from current manufacturer

I looked at newer models from the company that made our current box, and we were
looking for a few thousand there again with the need to get internet.

*Option 3:* Newer "basic" box == $2-4k box + $1000/yr internet

### Replace the landline

The core problem is the price of the phone line not the quality or reliability
of the equipement that we have now. I just needed cheaper phone service.

I first looked into getting a new coax line run which would have cost about
$360/yr all said and done. Luckily that didn't work out and I had the idea of
using an LTE backup. LTE backups (or just internet hotspots) from Verizon
and other major phone providers are pretty expensive still and were far more
bandwidth and quota than we actually needed for the call box. It just needed
a VoIP liine to work.

T-Mobile sells prepaid sim cards for $10/month with unlimited mobile internet.
That's the key piece and then the rest is just wiring to make sure that the
call box can actually call out.

Analog phone adapters allow traditional phone lines to work using VoIP. Paired
with an LTE modem and router everything is ready to go.

<center>LTE Modem <-> Router <-> Phone Adapter <-> Call Box</center>

I used Voip.ms as the phone provider and followed their general getting started
guide as well as the [handytone guide][handytone_setup] on their wiki.

It took me a bit to get right and I had to carefully set up and link the device,
the phone number, and set the caller ID to the newly purchased DID number. Once
this was all in place I could test the setup with a normal phone and could
make and receive calls.

The final piece was to put this up in the garage where the landline connected
and put an rj11 connector on the single stranded phone lines. I powered it all
up and it worked!

{% include photo.html alt="`garage equipment` output" img="/assets/2025/02/garage.jpeg" %}

VoIP.ms costs $0.85/mo. (*Update 1 yr in*: Price updated to $1.10/mo.) The calls
are so short that they're effectively free. We loaded the account in February and
as of November have not had to reload.

Total setup costs:

* [LTE Modem (Netgear LM1200-100NAS 4G LTE Modem)][modem] - ~$25
* [Router (TP-Link AC1200)][router] - $30
* [Analog Telephone Adapter (Grandstream HandyTone 801)][adapter] - ~$55

*Option 4:* $115 setup + $11/mo to operate

### Price Comparison

| Item           | Setup Cost | Monthly Cost | Annual 1st year | Annual ongoing | vs. original | vs. new AT&T |
| :------------- | ---------: | -----------: | --------------: | -------------: | -----------: | -----------: |
| Original       |         $0 |         $160 |          $1,920 |         $1,920 |           $0 |      -$1,320 |
| New AT&T       |         $0 |         $270 |          $3,240 |         $3,240 |      +$1,320 |           $0 |
| ButteflyMX     |     $1,200 |         $160 |          $3,120 |         $1,920 |            0 |      -$1,320 |
| Basic Box      |      $3000 |          $60 |          $3,720 |           $720 |      -$1,200 |      -$2,520 |
| **VoIP Setup** |       $115 |          $11 |            $247 |           $132 |      -$1,788 |      -$3,108 |

Compared to the new AT&T rates we're spending about $3000 less annually as an
HOA! This project was a huge success!

[modem]: https://www.amazon.com/NETGEAR-Broadband-Modem-LM1200-Always/dp/B0F3Y532X9
[router]: https://www.amazon.com/dp/B09G5Y1HWZ
[adapter]: https://www.amazon.com/dp/B06XW1BQHC?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_3
[handytone_setup]: https://web.archive.org/web/20250824191306/https://wiki.voip.ms/article/Grandstream_HandyTone_802_-_HT802
