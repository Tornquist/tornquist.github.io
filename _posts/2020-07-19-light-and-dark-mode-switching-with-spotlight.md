---
layout: post
title: Light and Dark Mode Switching with Spotlight
date: 2020-07-19 07:00:00
categories: programming
---

One of the surprises I've had from the rapid work from home switch is how bright
my home office is on a sunny day and how dark it is on a cloudy day. I regularly
have to switch my interface mode to be able to see my screen and continue working.

I found myself regularly opening up the system settings and changing the system
theme, manually going to each desktop and changing the wallpaper, and manually
toggling the theme of my terminal and other editors. Some tools auto-switch, but
many tools do not.

To fix this, I've configured the following commands quickly keep working:

* **Toggle system interface:** &#8984; + Space, T, Enter
* **Dark wallpaper:** &#8984; + Space, D, Enter
* **Light wallpaper:** &#8984; + Space, L, Enter

## Tooling Updates

My regular tooling is:

1. Browser
  * Chrome
  * Safari
1. Text/Source Editing
  * Xcode
  * Atom
  * TextMate
  * Tot
1. iTerm
1. SequalPro (Ace)
1. Productivity
  * 1Password
  * Day One

Removing the tools that already have adaptive interfaces I was left with the
following needs:

1. Update Atom UI and Syntax theming
1. Update Xcode Syntax theming
1. Update iTerm profile
1. Update TextMate

### Atom

Install the [mojave-dark-mode][0] plugin.

### Xcode

Xcode is a bit tricky. Nothing needs to be set up, but the way that theming works
is not directly obvious. By default, Xcode will automatically adjust the navigation
items, toolbars, etc. when switching the system theme, but the source editor
will stay on the previously selected theme.

Out of the box, Xcode includes `Default (Light)` and `Default (Dark)`. The naming
has no impact on the response to the interface mode. The only thing that matters
is the theme selected when in a given mode.

To configure Xcode, set the system theme to dark, and then pick a theme. Toggle
to light, and then pick another theme. Those two themes will be automatically
used for light and dark mode now.

> ex: picking `Default (Light)` while in dark mode, and `Default (Dark)` while in
light mode would make the UI and editor styles opposite.

The way that the theme is linked to the current system theme is not immediately
obvious.

### iTerm

iTerm can be extended using Python scripting after the Python runtime is installed.

I'm using a [script][1] from [FradSer][2] to manage this. The process is pretty
simple.

1. Select light/dark mode themes and update the script accordingly
1. Add the script to `Application Support/iTerm/...`
1. Select the script from iTerm > Scripts and approve the `Install Runtime` action

The script is attaching a monitor to the iTerm `effectiveTheme` variable and is
automatically updating the profile in response to a variable change.

### TextMate

TextMate is an unsolved problem. I have not yet found a way to dynamically
update the theme. The priority here is lower with my daily notes in Day One, but
it would still be nice to have given I use it as a scratchpad for terminal
commands as well.

## System Updates

### System Theme

macOS Automator applications automatically show up in Spotlight search and are
a great way to manage system automation. I started with a simple automation to
toggle the system appearance. This `Change System Appearance > Toggle Light/Dark`
action is available be default.

{% include photo.html alt="Toggle System Appearance" img="/assets/2020/07/toggle-system-appearance.png" %}

By naming it _Toggle Light or Dark Mode_, `Light Mode`, `Dark Mode`, and
`Toggle Mode` are all valid name matches. Although I use it enough that `T` is
all that I need to type.

I can simply type "&#8984; + Space, T, Enter" to toggle my system interface.

### Wallpaper

Wallpaper automation is a bit broken. AppleScript (theoretically) supports
iterating over desktops and supporting setting wallpapers, but when iterating
over "every desktop", the results are significantly less than you might expect.

{% include photo.html alt="Dark Wallpaper" img="/assets/2020/07/set-dark-wallpaper.png" %}

That AppleScript says `tell every desktop`, but only sets the desktop/space that
the user is currently looking at. This is probably a privacy feature as these
commands used to work.

To add the two wallpaper actions, make a new Automator Application with a single
"Run AppleScript" that sets the path to either the light or the dark wallpaper.
This enables:

* **Dark wallpaper:** &#8984; + Space, D, Enter
* **Light wallpaper:** &#8984; + Space, L, Enter

_Note: All the automations must be run within Automator and allowed through the
OS security rules before they will work in Spotlight._

## Conclusion

I can now use Spotlight to trigger explicit wallpaper changes on a given desktop
and can use Spotlight to trigger a system-wide interface change. My core tools
all automatically adjust to the interface change or have been explicitly
configured to listen.

Instead of navigating through layers of GUIs, I now have three main keyboard
shortcuts that allow for instant reconfiguration.

This is a massive win for my productivity and happiness in my workspace.

[0]: https://atom.io/packages/mojave-dark-mode
[1]: https://gist.github.com/FradSer/de1ca0989a9d615bd15dc6eaf712eb93
[2]: https://gist.github.com/FradSer
