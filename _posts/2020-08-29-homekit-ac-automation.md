---
layout: post
title: HomeKit AC Automation
date: 2020-08-29 22:30:00
categories: programming
---

A few months ago I moved into a new home with the 27-year old furnace right off
the living room. I didn't think anything of it at the time, but it has made it
*really* hard to just watch TV because it is just way too loud. My wife and I have
started using subtitles to make sure that we're not just blasting the volume for
our neighbors.

We have a Nest thermostatic, and can easily put it on eco mode to turn off the air
but it's always a pain to remember to turn eco mode back off so that the
temperature of the home remains comfortable.

For awhile I've been putting the home in eco mode and setting a reminder on my
phone to turn it back off when the show or movie ended. This "solution" had a few
particular problems:

1. It was tedious
2. It made watching an extra episode hard
3. I kept snoozing the reminders and not turning eco mode off

This may sound like a me problem, but it's not. It was a huge problem with our
home, and needed a strong technical solution.

### Goal

I use an AppleTV as a HomeKit hub and wear an Apple Watch. I'm a big fan of the
"raise to speak" Siri integration and regularly use Siri to turn on and off lights
as I walk around my home. My goal was to be able to say "hey Siri, turn off the
air for XX minutes." I was looking for a solution that would:

1. Be easy
2. Not be tedious
3. Be stable and reliable
4. Take all pain and risk out of eco mode

Asking Siri to turn off the air so I could watch TV and then have it automatically
turn back on seemed like the ideal solution.

To get started, I needed a way to get the thermostat into the HomeKit ecosystem.
I found [homebridge][0] and the [homebridge-nest][1] plugin and *finally* had a
viable path forward to watching TV in peace.

* **Homebridge** allows you to connect devices without existing HomeKit
  integrations to the Home app.
* **Homebridge Nest** is a plugin to bring the Nest into HomeKit with the creation
  of a HomeKit thermostat, an eco switch, fan switch, and temperature sensors.

### Shortcuts

The standard [Shortcuts][2] app supports powerful automations between all kinds
of apps and system services on iOS devices. I started with a prompt to ask the
user for a number of minutes and then turn eco mode on, wait those minutes, and
then turn it back off.

This would allow me to add the trigger to Siri and would allow for an easy "Hey
Siri, let me watch TV for 30 minutes" or whatever prompt I set.

Unfortunately, all shortcuts running in the background are automatically killed
after about 3 minutes. Unless I was watching less than 3 minutes at a time, this
wasn't going to be a real solution.

### Better Delays

On top of allowing existing devices without HomeKit integration to be pulled in,
Homebridge also allows **virtual devices** to be created and simulated in HomeKit.

[Homebridge-Delay-Switch][3] is a plugin that allows for virtual switches and
virtual motion sensors to be created. You can create a switch that will
automatically turn off after a set amount of time (say a 22min tv show). What
is especially nice about the implementation is that when the switch turns off
on its own, you can set it to automatically trigger a virtual motion sensor, but
should you turn the switch off manually, the motion sensor will not be triggered.
**This makes it very easy to build an automation that can be aborted.**

The one catch with the delay switches is that it was no longer a straight, single
automation. I would need a way to turn the switches on, and then another action
once they turned off. The two parts of the process were completely discrete actions.

### Putting it Together

At this point I had a [homebridge][0] with the [homebridge-nest][1], and
[Homebridge-Delay-Switch][3] plugins, and [Shortcuts][2] to tie it all together.

My plan was to set up the following automation process:

```
Delay switch turned on
    |
    |--> Turn eco mode switch on

[Wait for delay to complete]

Delay switch motion sensor triggered
    |
    |--> Turn eco mode switch off
```

The delay switch plugin must be calibrated for a specific period of time through
Homebridge. It is not dynamic. I went with 30, 60, and 120 minutes as the main
trigger lengths to cover a 22 and 50 minute TV show and normal movie.

Those times mean that I had three switches and would have three "switch on" events
to enable eco mode in response to and three "motion sensor" events to use for
disabling eco mode. Multiple trigger automations are supported by HomeKit, but
the UI doesn't exist in Apple's app. I used [Eve][4] instead when building the
automations to keep it to two (on/off) instead of six (on/off for each delay switch).

Unfortunately, Eve only automates scenes so instead of being able to just say
"when a sensor detects motion, turn this switch off" I had to create a scene
in HomeKit with the switch off and then apply that scene in the automation. A bit
silly, but the end result was the same.

At this point, all the pieces are in place. I set up the following automations:

```
Delay switch 30m, 60m, 120m turned on
              |    |    |
              V    V    V
           Enable eco mode scene
           (eco mode switch on)

Motion sensor for 30m, 60m, 120m triggered
                   |    |    |
                   V    V    V
               Diable eco mode scene
               (eco mode switch off)
```

### Polish

With the new virtual switches added to my Home app's "favorites" I was good to
go. I went through the quick settings on my phone and found a giant switch.

I was hoping that I could 3d touch on the favorite itself to switch it on, but
the action behavior was swipe down -> click home -> click item -> swipe on.

This met most of my original goals, but was a huge violation of **#2. Not being
tedious**.

This is where [Shortcuts][2] comes back into play. The heavy lifting of the
automation was already complete, but with shortcuts I was able to simplify tedious
menu navigation into a single button press.

The ability to add shortcuts to a quick action list makes it even better. With
this whole process complete I now have quick buttons on my phone to disable our
HVAC for a short and safe period of time, and now I can finally *watch tv in peace.*

We've been using this new solution for about two weeks now and it has been a much
more significant quality of life improvement than I expected. I am so happy with
how this all worked out.

{% include photos.html
  height="70" id="quiet-home"
  img1="/assets/2020/08/homekit-switch.png"
  img2="/assets/2020/08/shortcut-quick-action.png"
  img3="/assets/2020/08/shortcut-automation.png"
%}

[0]: https://homebridge.io
[1]: https://github.com/chrisjshull/homebridge-nest
[2]: https://support.apple.com/en-us/HT208309
[3]: https://github.com/nitaybz/homebridge-delay-switch
[4]: https://apps.apple.com/us/app/eve-for-homekit/id917695792
