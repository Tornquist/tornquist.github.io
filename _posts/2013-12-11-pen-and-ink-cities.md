---
layout: post
title: "Pen and Ink Cities"
date: 2013-12-11 20:09:00
categories: programming
custom_css:
- syntax
---
I recently completed Intro to Computer Graphics (CS 334). It started with an introduction to how computer graphics systems work, and concluded with a wide-sweeping look at numerous aspects of the field. For the class we were required to select a final project. I chose to do NPR (Non-Photorealistic Rendering) in a pen and ink style. In addition to the rendering style, I developed a system to generate cities. The software takes a \*.txt input that has a description of the city (number of city blocks and size of each block) and descriptions of buildings. From these descriptions the software creates buildings and lays them out within the specified city block structure to generate cities.

A text file like this:

```text
WORLD
3 50
3 50

BUILDING
10 3 3
10 3 3
10 30
F 0 0 [ - 0 4 ] 0 [ + 0 4 ] [ + 0 4 ]
R -2 -1 +1 +2 +2 +3 +4 +3 +2 +3 +4
```

Creates this:

{% include photo.html alt="L City" img="/assets/2013/12/l_city.png" %}

As you can see, the grammar allows for multiple buildings and styles to be created from a single description. The [] used in the building logic specify ranges. If a larger city is used with multiple building types, much more advanced cities can be created:

{% include photos.html
  height="21" id="pen-and-ink-cities"
  img1="/assets/2013/12/city_1.png"
  img2="/assets/2013/12/city_2.png"
  img3="/assets/2013/12/city_3.png"
%}

The pen and ink styling is much more evident when the software is actually being used. If you are interested in trying it for yourself, grab the Visual Studio Project (Requires G3D) or the compiled \*.exe below. Both files include the readme on how to create cities and the syntax for my grammar. Enjoy!

--Nathan

[Source](/assets/files/pen_ink_cities/PEN_INK_CITIES_SOURCE.zip) - Requires [G3D](http://g3d.sourceforge.net/)

[EXE](/assets/files/pen_ink_cities/PEN_INK_CITIES_EXE.zip)
