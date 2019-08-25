---
slug: senior-design
layout: project
title: Twitch Plays Robot Soccer
release: May 2015
featured: true
rel_sort: 50
custom_css:
- youtube_embed
---

The title of my senior design project was *Robot Soccer Controlled and Broadcast to
Twitch*. It was pretty much the coolest project ever.

At Purdue, senior design projects are submitted in the spring the year prior.
Senior design in ECE requires a few things:

1. Use of a microcontroller
2. A non-trivial set of integration with other chips
3. A PCB to connect the various components

Around the time I was writing the proposal, [Twitch Plays Pokemon][1] had just
happened for the first time and we wanted to create something like that. The
basic idea was that we would design a set of robots that could be controlled
through twitch. Viewers would enter commands in the chat interface. These commands
would be received, queued, and eventually sent to the robots. The viewers would
have live feeds from webcams on the field as well as a video stream from the
perspective of each robot.

To make this all work, we had a server running on a raspberry pi that would
act as a host for the two robots. Originally the pi was also tasked with receiving
video feeds from each robot and an on-field webcam, but that ended up being too
much data. The on-robot cameras were cut and video ended up being managed by a laptop.

The robots needed to be able to make network requests to the server and control
the motor drivers that directed the wheels and front paddle (for kicking). This
could have all been accomplished with a raspberry pi on each robot, but to meet
the requirements for the project, we used a PIC32 microcontroller that communicated
with a RN171 WiFi module and the motor controllers. The board photos below show
how all of the components were connected. The PIC32 was at the center, with WiFi
in the top left, power in the top right, and a motor controller in each of the
two bottom corners.

{% include photos.html
  height="40" id="senior-design-1"
  img1="/assets/images/projects/senior_design/senior_design_pcb_layout.png"
  img2="/assets/images/projects/senior_design/senior_design_pcb.jpg"
%}

One of the most interesting aspects of the project was how to power the robots.
If we wanted the robots to be fully user controllable, we needed to make sure
that users could not just make each robot go in circles and tangle everything up.
To accomplish this, we decided to copy bumper cars and ground the soccer field
and have a charged grid on the top for the robots to connect to. Below are
renderings of the early designs illustrating this concept.

{% include photo.html alt="Robot Renders" img="/assets/images/projects/senior_design/senior_design_robot_render.png" %}

The arena was built out of plexiglass with a stainless steel bottom and screen
door material for the powered grid on the top.

{% include photo.html alt="Arena" img="/assets/images/projects/senior_design/senior_design_arena.jpg" %}

With everything put together, this is what the robots look like inside the
arena.

{% include photos.html
  height="32" id="senior-design-2"
  img1="/assets/images/projects/senior_design/senior_design_2.jpg"
  img2="/assets/images/projects/senior_design/senior_design_4.jpg"
%}

Some better photos of the robots:

{% include photos.html
  height="32" id="senior-design-3"
  img1="/assets/images/projects/senior_design/senior_design_1.jpg"
  img3="/assets/images/projects/senior_design/senior_design_3.jpg"
%}

This is our (extremely gaudy) promo/demo video:

<div class="video-container">
<iframe class="video" src="https://www.youtube.com/embed/29wN6f5H5uw" frameborder="0" allowfullscreen></iframe>
</div>

All in, this project worked surprisingly well. The biggest issue we had was
caused by the flex in the plexiglass. We should have built a more stable frame
on the outside to keep it from sagging. We used spring steel to connect to the
powered grid, and it ended up needing more force for a solid connection than we
had anticipated. This meant that the robots either moved really well on the
outside of the arena, or really well on the inside.

Despite the difficulties, users were able to connect to the twitch feed and
remotely control our robots. Thanks to [Mark Harlan][2], [TJ Root][3], and
[Josh Hannan][4] for working alongside me on this project.

[1]: https://en.wikipedia.org/wiki/Twitch_Plays_Pokémon
[2]: https://www.linkedin.com/in/mark-harlan-b187a558
[3]: https://www.linkedin.com/in/tj-root-a3b07548/
[4]: https://www.linkedin.com/in/joshua-hannan-85124a83/
