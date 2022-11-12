---
slug: time
layout: project
title: Time
release: Aug 2018 - Oct 2022
featured: true
rel_sort: 110
---

I really enjoyed [analyzing my working hours in 2017][start], and I'm a
big fan of the infographics that [Nicholas Felton][feltron] makes on his own life.
The goal of this project was to combine those two ideas into a platform for
continuous monitoring and reporting on how I spend my time.

That's what I've built. *Time* supports unbounded nested categories, tracking of
singular events or ranges of data, import/export of everything, iOS widgets, and
has excellent handling of data across timezones and days.

{% comment %}
!@ generate_image assets/images/projects/time/time-overview.png
  assets/2020/10/time-running-dark.png
  assets/2020/10/time-homescreen-running.png
  assets/2022/11/all-data.png
  assets/2022/11/time-data.png
!@ end_generate
{% endcomment %}

{% include photo.html img="/assets/images/projects/time/time-overview.png" %}

I have written about this project in these posts:

* 10/20 - [Time Tracking]({% post_url 2020-10-15-time-tracking %})
* 10/20 - [Is my timer running?]({% post_url 2020-10-17-is-my-timer-running %})
* 10/20 - [Building a Realtime Widget]({% post_url 2020-10-18-building-a-realtime-widget %})
* 05/21 - [SwiftUI as a Design Tool]({% post_url 2021-05-16-swiftui-as-a-design-tool %})
* 11/22 - [Finishing Time]({% post_url 2022-11-12-finishing-time %})

And the source code can be found here:

* [Time-Client][client]
* [Time-API][api]
* [Time-Core][core]

[start]: {% post_url 2018-02-11-2017-work-analysis %}
[feltron]: http://feltron.com
[client]: https://github.com/Tornquist/Time-Client
[api]: https://github.com/Tornquist/Time-API
[core]: https://github.com/Tornquist/Time-Core
