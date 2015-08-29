---
layout: post
title: "DJ Roomba/Dubstep Robot"
date: 2013-12-11 20:57:00
categories: programming
custom_css:
- colorbox
- youtube_embed
custom_js:
- jquery
- photoset-grid
- colorbox
---
For ECE 362 (Microprocessor System Design and Interfacing) I had to design something socially redeeming with my HC9S12 Microcontroller. The original plan as the title implies was a robot that would drive around and play music at people. Plans were to create/3D print a Deadmau5 head (below) and mount screens in it that would change based on the song playing and the robot's motions. An array of IR Proximity sensors would be used to detect movement so that the robot could follow a moving object.

![DJ Roomba CAD Head](/assets/2013/12/djroomba/head.jpg)

My partner, Mark, designed the speaker system. We had a small speaker that we had connected to our board and we were controlling it using PWM. Instead of having songs pre-recorded, we generated it on the fly based on hard coded note arrays. Each array corresponded to a particular song, and based on the note a sing wave would be played by stepping through an array of pre-calculated sine wave values at different step sizes.

I worked on the screens and motor drivers. All work working individually in testing, but we ran into issues when we tried to put everything together. Some audio quality had to be sacrificed to have a slow enough interrupt rate that the screen logic could complete without causing interrupts to start stacking up. In addition to having interrupts stack up we learned that the screen process was too slow to change on the fly. Had we known this in advance we would have interfaced two microcontrollers together. Instead we simply set the screens prior to playing the music and gave up animations in time to the music.

Further sacrifices were made with the motors. Early on we were running into significant current issues. This was solved by changing from one 9V battery to six 1.5V AA batteries. This solved the problem on a small scale, but issues still existed around driving two motors. It was possible to supply more current, but we were having trouble sinking enough through the H-Bridge that was controlling the motors. Instead of fighting the motors for days, we rebranded the project. A robot that follows people became an mp3 player that reacts to movements. Motors became lights and the old system was repackaged. Swapping out the motors for lights allowed for the current issues to be eliminated. The RGB LEDs we used however needed more voltage than the 5V that the microcontroller needs. Because of this, the H-Bridge was still useful as a voltage amplifier. The IR Sensors were then repurposed to control the LED color and the screen use did not change at all.

It was disappointing to give up the robot idea, but by changing focus we were still able to leverage our PCB without needing changes, and we created a nicely packaged and fully functioning product. Many teams did not. Below you'll find photos and a video demonstrating some of the songs the unit can play. Enjoy!

--Nathan

# Gallery:

{% include /galleries/2013-12-11-dj-roombadubstep-robot.html %}

# Demo:

<div class="video-container">
<iframe class="video" src="https://www.youtube.com/embed/apr6aJZmUKY" frameborder="0" allowfullscreen></iframe>
</div>
