---
slug: arcis
layout: project
title: Arcis
release: July 2012
rel_sort: 20
---

Arcis was my first large-scale Android project and the first with intentional
enemy design/artificial intelligence. When I set out to build Arcis, I wanted to
build a game that combined arcade and tower-defense mechanics.

The initial idea was to call the game *Storm the Castle* with the player controlling
a single tower with a trebuchet on top. Enemies would run from all sides of the
screen to attack that central tower. As enemies ran towards the tower,
the player would be able to build walls anywhere on the game board to block and
route enemies. (This is where the tower-defense mechanics came into play.)

To route the enemies, I modified A\* pathfinding to generate a direction of travel
from any point on the board towards the main tower. The game background shows the
results of this algorithm and the player would see entire sections of the board
get darker as walls were built and the distance necessary to travel increased.

As I worked on this project, it became clear that I would be unable to create
the graphics necessary to really bring the medieval inspiration to life. Other
than the audio, I was working on this project alone. I decided to change the name
to *Stormfront* right before the beta release on r/androidapps and r/android.
I hadn't done any research on this name, and in my mind it was just a functional
description of enemies storming a frontline. I quickly learned of a white
supremacist group by the same name and changed the name to *Arcis* for the duration
of the beta program and the final release.

Organizing and running a beta program was really exciting. I had a few hundred
people sign up through my website and was able to break that group into multiple
trials. I received excellent feedback and released the final version on the app
store in August of 2012.

The final game was difficult, but drove the shift from arcade to tower-defense
strategies well. Early in the game it was best for the player to manually target
and shoot enemies. By the 5th wave, it was important to build basic routing, and
then as the game progressed the number of enemies increased so much that a good
tower design took over gameplay completely.

Each tower had a specific strength/health. Health under a certain level would
drain automatically. This meant that the player could drag their finger across
the screen and build an entire defense system, but it would drain and vanish
pretty quickly. If the player wanted to invest more resources, they could hold
their finger on a tile and create a much stronger tower that would stay unless
destroyed by an enemy.

Towers could also be upgraded with abilities (and ability levels, 1-3). The
abilities included:

* **Health**: Automatically heal itself and (at higher levels), heal the
  surrounding towers as well.
* **Ice**: Slow down enemies within a certain distance of the tower.
* **Fire**: Targeted offensive attacks on enemies. The number of enemies a
  single tower could target and the strength of an attack increased as the
  tower was upgraded.

Together the player could build a self-healing matrix of towers that would slow
down and attack enemies. Careful routing of the walls could be used to direct
the exact path that would be taken and keep enemies at a safe distance while
keeping them within the attack radius.

An excellent composer and good friend of mine, [Michael Betz][1], did the audio
for this game. Although it is not maintained, you can get a copy of Arcis
on [Google Play][2] or look through the source code on [GitHub][3].

This project was very fun to make, and it was really exciting working with and
managing a beta program. I was very excited to receive over 2,000 downloads on
release day, and about 5,000 over the lifetime of the project. For a period of
time I was in the top 100 new games on Google Play.

{% include photos.html
  height="28" id="arcis-1"
  img1="/assets/images/projects/arcis/Arcis_1.png"
  img2="/assets/images/projects/arcis/Arcis_2.png"
%}
{% include photos.html
  height="28" id="arcis-2"
  img1="/assets/images/projects/arcis/Arcis_3.png"
  img2="/assets/images/projects/arcis/Arcis_4.png"
%}

[1]: http://michaelbetzmusic.com
[2]: https://play.google.com/store/apps/details?id=com.petronicarts.arcis
[3]: https://github.com/Tornquist/Arcis
