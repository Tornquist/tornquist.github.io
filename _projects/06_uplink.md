---
slug: uplink
layout: project
promo_image: uplink.png
feature_image: uplink_full.png
promo_description: Sports Graphics
title: Uplink Sports
subtitle: Sports Graphics Made Simple
release: October 2016
rel_sort: 41
custom_css:
- colorbox
- youtube_embed
custom_js:
- photoset-grid
- colorbox
---
My senior design project was ***robot soccer controlled and broadcast to
Twitch***.  It was pretty much the coolest project ever.

I teamed up with three of my friends to
build a soccer arena and robots to compete in it.  Our directive was to
build something useful that incorporated a microcontroller as well as a
plethora of on-chip and off-chip peripherals. We built the most useful
thing that we could think of.

This is our gaudy promo/demo video:

<div class="video-container">
<iframe class="video" src="https://www.youtube.com/embed/29wN6f5H5uw" frameborder="0" allowfullscreen></iframe>
</div>

We chose to build robots that could play soccer.  Our system ended up
using far more than just a microcontroller.  Each robot had a
microcontroller that functioned as the "brains" of the bot.  That
microcontroller would communicate with a WiFi Module to request
commands, and direct the motors to execute those commands.  A central
webserver on the arena kept track of the scoring and managed the webcam
feeds.  Finally, a webserver running on a laptop communicated with
Twitch to receive and queue commands for the robots, and sent video back
to the users. Oh and ***the robots were powered like bumper cars.***

{% include /galleries/project-senior-design.html %}

What to learn more? [Check out the project
website](https://engineering.purdue.edu/ece477/Archive/2015/Spring/477grp1/)
