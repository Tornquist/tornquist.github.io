---
layout: post
title: "Pumpkin Wars: Revenge of the Gourds"
date: 2015-10-28 21:45:00
categories: programming art
custom_css:
- youtube_embed
---
The new BB-8 robot from Star Wars came to life today in the form of a
pumpkin.  This happy little guy was created as my team's entry in HERP
DERP 2, an internal pumpkin carving hackathon at Enova.

<div class="video-container">
<iframe class="video" src="https://www.youtube.com/embed/pstlwaIRbaY" frameborder="0" allowfullscreen></iframe>
</div>

About a month ago I received an email from the CTO of my company with
the subject *HERP DERP 2: Rise of the Machines*.  The email opened
with:

> Recently a book came into my possession, a truly mysterious book.
> Bound in fog and written in whispers, it tells of the first Enova
> Halloween event known as "HERP DERP" and prophesied its return.  In
> words both strange and familiar, it said that when the sun had passed
> its zenith on the twenty second day of the tenth month, gourds
> augmented with electronics and intelligence would rise and be judged.

Shortly after that initial email I began talking to Costi, the CPTO at Enova
(Chief Pumpkin Technical Officer), and started making plans for my team.  With my
background as a computer engineer this type of rapid hardware
prototyping is right up my alley.  I have been more than excited for
this competition for quite awhile.

When the official HERP DERP 2 logo came out (pictured below) I knew that
we had to do something more than just lights and sound.

{% include photo.html img="/assets/2015/10/herp_derp_banner.png" %}

The guidelines of the competition are simple: use an arduino or
Raspberry Pi and make something cool.  After seeing the new [Star Wars
trailer](https://youtu.be/sGbxmsDFVnE) my team decide the new robot,
BB-8 (shown below), was the perfect fit.  What could be cooler than pumpkin carving,
Star Wars, and robots all combined?

![BB-8](/assets/2015/10/bb8.png)

The team was made up of:

* Zach Bright
* Lizzie Clark
* John McCormack
* Arnaud Thiercelin
* Nathan Tornquist (me)

To build anything resembling BB-8, we would need two pumkins.  When
talking about the design, it became clear that we wanted the electronics
to be housed within the larger pumpkin, and for the head to just be
impaled on a rotating dowel.  With this basic idea, Arnaud and I were
able to build a simple frame the weekend before the competition:

{% include photo.html alt="Frame" img="/assets/2015/10/frame.jpg" %}

The idea was simple.  A stepper motor with a belt would connect to the
central shaft and rotate it.  This way we could have a large enough
dowel to support a pumpkin, and we could
still use a normal motor.

{% include photo.html alt="Frame and Motor" img="/assets/2015/10/frame_motor.jpg" %}

From there, the motor would connect to a h-bridge that was driven by a
Raspberry Pi.  Instead of the Pi controlling the robot completely,
we set up a simple Apache webserver to call specific scripts when URLs were
hit.  We didn't want to just stop there! Arnaud kept going with that idea, and set up an app that would call the endpoints!  Long story short,
this means that we had a native iOS app that allowed anyone to control
the robot pumpkin!**\***

###### \* Assumming the user was on the correct network. Due to company security on the WiFi, it was difficult to get the Pi on the local network.  Instead of fighting with this, we just used my phone as a hotspot and routed all of the traffic through it.

While Zach, Arnaud and I were busy setting up the hardware for inside
the pumpkin, Lizzie and John were quickly painting the pumpkins to look
like the robot.  Once they were all painted and cleaned up we were able
to put the pumpkins on the frame and see how it looked. I'd say they
nailed it!

{% include photo.html alt="BB-8 Pumpkin" img="/assets/2015/10/bb8_pumpkin_combined.jpg" %}
