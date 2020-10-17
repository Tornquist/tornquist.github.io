---
layout: post
title: Time Tracking
date: 2020-10-15 18:15:00
categories: programming
---

{% assign time = site.projects | where: "slug", 'time'  | first %}
{% assign macropad = site.projects | where: "slug", 'macropad'  | first %}

In August 2018 I started building a time tracking app that I've been calling
*[Time]({{ time.url }})* (creative name, I know). The goal of this project is
to build an engine that I can use to answer questions such as:

* How much am I working?
* Am I putting enough time into **&#119909;** hobby?
* How long has it been since I cleaned my house?
* How long has it been since I've caught up with **&#119910;** friend?

While getting started on this project, the main motivation to build it myself
over using an existing tool was the fact that all of the tools out there were
really based around consulting and expense reports. A time tracking app based
around simple curiosity and clear data didn't really exist.

I also wanted to make sure that the data was easy to archive and stored in such
a way that would allow it to last. I didn't want an iOS update to mean that I
would lose access to years of information.

It has now been over two years since I started this project. I've worked
on it off and on with a few other major projects and life changes along the way.
In 2019, I designed and built a [macropad]({{ macropad.url }}) and redesigned
[this website]({% post_url 2019-08-28-2019-site-refresh %}). In early 2020 my
wife and I purchased our first home just before the world shut down for COVID-19.
From the beginning of COVID through May/June I was building a [telemedicine
platform][0] for SkinIO with the goal of pivoting and saving the company.

Long story short, _there was some stuff going on._

Aug. 2nd was the last day I tracked in both _Time_ and _[Tyme][1]_, and when I decided
to fully commit to the new platform that I am building. I had just wrapped up
a major [styling update][2] that I had started on Feb. 22nd (right before the world
changed), and the app was finally complete enough that I could use it to track
my daily and weekly time.

### Project status

I keep all of my notes for side projects in a moleskin notebook. I think that for
the same reasons that I'm fascinated by time and how it's spent, I have some
romantic or nostalgic ideas about hand written project notes.

It's not about the idea that my notes or projects are great or world changing; it's
more about the diary that's formed. I can look back through this notebook and
see the sketches and mappings from when I was [building an app to propose to my now wife]({% post_url 2017-06-18-quest %})
and the early ideas of what this project would become.

In June 2019 I made a list of what was needed to start using the app daily:

{% include photo.html alt="Time Features" img="/assets/2020/10/time-goals.jpg" %}

The critical items there have **all** been marked off. The app is themed, a server
is hosted that I'm using daily, and it's tracking the timezone data and adjusting
both for event time and local/relative comparison.

As far as a "daily tracker" is concerned, this app meets all of the goals I set
out with and is in a tighter and cleaner form factor.

What's next is to finally answer my initial questions of _how much am I working?_
and _where do I spend my time?_

### Answering the question

I have data from every working minute of 2018, 2019 and 2020 that has never been
analyzed. I started tracking my time in 2016 to make sure that I wasn't working
on Uplink so much that it was taking away from my work at SkinIO.

When I look back at my GitHub activity graph from the last three years, I can see
the days that I committed work, but it doesn't show me the time I spent thinking
and sketching, or iterating on items that never made it into a final commit. It
doesn't show my time learning to play the piano.

I used to have the goal of **one commit per day**, but that goal orients activity
and time around producing some output instead of just intentionality of time. I
want to look back and say "I prioritized my family, my friends, my hobbies and
my work, and each was done with intentionality." I don't want to just force
items into a messy commit history.

My next task on this project is to rebuild the GitHub activity graph using my
self-reported data. I want to control the input, the output, and the narrative
so that this is a tool for self-reflection and accountability and not just a
graph of someone else's metric.

If someone wants to graph the actual time spent on a project, let them. If they
want to graph the days that some work occurred, that is just as viable.

I am working to build a habit tracker, a time tracker, and a whole engine for
comparison and analysis of data. When it's done, I will be able to look back and
clearly answer the questions I posed two years ago. When I make a conscious effort
to work less, or work more responsibly, I want to know if it's actually changing
or if I've just normalized longer hours.

---

_This post is the first in a series about my Time project._

[0]: https://skinio.com/teledermatology/
[1]: https://www.tyme-app.com/en/
[2]: https://github.com/Tornquist/Time-Client/pull/23