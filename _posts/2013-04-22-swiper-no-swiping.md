---
layout: post
title: "Swiper No Swiping"
date: 2013-04-22 02:25:00
categories: programming
---
Over the last few months (being 1 or 2, not 3) I've been working on a card swipe based login system for the engineering advising offices here at Purdue.  The Freshman Engineering office has an old card swipe system, but hopefully my software will provide a system that can be expanded to every office and will ultimately make everyone's job easier.

To start off the process I updated the Student Information system that the advisers use.  It needed to be revitalized, and ultimately a lot of the changes paved the way for the new system.  I went from a page that is rendered based on static tables that just display data from the database to a dynamic page built with HTML5.  One of the coolest things is the auto-completion feature when students are being looked up.

More recently it came time to add the android side of things.  It took awhile to find a card reader that not only functioned the way I wanted it to, but also had a good SDK.  After being delayed as a result of purchasing a reader that only passed encrypted data, we ultimately settled on the UniMag II card reader and it works perfectly.  The system came with an example that could easily be stripped down to almost nothing.

Once the card reader was active, the rest of the program flow could be set up.  The integration with the Purdue systems is pretty cool.  Due to the way the database is set up, direct SQL connections are a pain, so I've built an entire backend that authenticates with the device every time something is requested.  Ultimately this allows us to distinguish which office the requests come from, and disable tablets at will remotely.

This is also my first Android app that is built around the activity system.  Arcis and SoloDefense both were single activity applications where I managed all of the switching between pages manually. Although I can't really talk more about the integration setup, nor can I post tons of screenshots, but the app is really cool.  You can swipe your ID, or manually sign in to get added to a queue.  The queue integrates with the online systems I've built quite well.  It should be about finished when the semester concludes and if summer testing goes well, hopefully we can roll this out to larger groups of people, and maybe even other departments next year.  I'm certainly excited about the way this project has gone.
