---
slug: online-toolbox
layout: project
title: Online Toolbox
release: May 2015
rel_sort: 40
---

One of the most important parts of marching band is recruiting. Without strong
recruitment it can be hard to get the number of musicians needed to fill in
the parade blocks or drill patterns on the field. During my time at Purdue I was
very active in the marching band and as an upperclassman I was part of the
leadership team.

All of the marching band recruiting and followup throughout the summer is done
by the leadership team of each section. Individuals have a number of students to
contact and followup on, and it is their responsibility to accurately report
headcounts and have the followthrough to see those students arrive at band camp.

This type of tracking and the amount of information captured can be managed well
using a CRM. [Doug Booth][1] was the trumpet section leader when I was a freshman,
and he had built the original Online Toolbox marching band CRM. When he graduated,
I took over maintenance of the original tool.

I had a pretty big list of features that I wanted to add, and eventually rewrote
the site using Ruby on Rails.

My tool had import/export features, easy account management, and was designed
to allow data on recruited students to continue right on into the season. Students
could be organized into sections and ranks (groups of 11 within a section).
In addition to organization features, there was the ability to track gigs
(negative marks) and automatically identify which students would be Game Day
Staff (non-marching support) for the next game.

I expanded the Doug's tool from a recruiting platform to a full marching-band
management platform. Staff, leadership and external recruitment all had features
and tools built into this product.

On top of that organization, everything was fully relational and flexible. I
wanted all the fields to be customizable and wanted to create a product that
would not need me (or anyone else) to maintain it. During the first season it
was used, the trumpet section alone had ~20% more students in camp than the
historical average.

I've written a bit more about the story in a [blog post][2] and have the source
on [GitHub][3].

{% include photos.html
  height="25" id="online-toolbox-1"
  img1="/assets/images/projects/online_toolbox/OnlineToolbox_2.png"
  img2="/assets/images/projects/online_toolbox/OnlineToolbox_3.png"
%}
{% include photos.html
  height="18" id="online-toolbox-2"
  img1="/assets/images/projects/online_toolbox/OnlineToolbox_5.png"
  img2="/assets/images/projects/online_toolbox/OnlineToolbox_6.png"
  img3="/assets/images/projects/online_toolbox/OnlineToolbox_7.png"
%}
{% include photos.html
  height="18" id="online-toolbox-3"
  img1="/assets/images/projects/online_toolbox/OnlineToolbox_8.png"
  img2="/assets/images/projects/online_toolbox/OnlineToolbox_9.png"
  img3="/assets/images/projects/online_toolbox/OnlineToolbox_10.png"
%}
{% include photos.html
  height="25" id="online-toolbox-4"
  img3="/assets/images/projects/online_toolbox/OnlineToolbox_11.png"
  img4="/assets/images/projects/online_toolbox/OnlineToolbox_12.png"
%}

[1]: https://www.linkedin.com/in/douglas-booth-76b79224
[2]: {% post_url 2015-05-01-online-toolbox %}
[3]: https://github.com/Tornquist/onlinetoolbox
