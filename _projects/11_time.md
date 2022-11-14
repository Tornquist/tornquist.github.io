---
slug: time
layout: project
title: Time
release: Aug 2018 - Oct 2022
featured: true
rel_sort: 110
---

## Motivation
-------------

_Time_ is a time tracking application designed around flexible organization of
how time is tracked and easy reporting on where time was spent.

This application was built in response to an analysis I did in [2017][2017]
using data recorded in a contractor-focused time tracker and is largely a
correction from concerns that I had with how that software organized and
stored data.

## Screenshots
--------------

{% comment %}
!@ generate_image assets/images/projects/time/time-overview.png
  assets/2020/10/time-running-dark.png
  assets/2020/10/time-homescreen-running.png
  assets/2022/11/all-data.png
  assets/2022/11/time-data.png
!@ end_generate
{% endcomment %}

{% include photo.html img="/assets/images/projects/time/time-overview.png" %}

## Highlighted Features
-----------------------

* **Flexible data organization**
  * Categories used to track time entries have no max or minimum depth
  * Everything can be nested, or rearranged at will
* **Fast analytics based around aggregate time**
  * Default view shows total time per category today, and this week
  * Historical data can be viewed by day, week, month and year
  * Grouped category trees or singular leaf nodes can both be graphed
  * Handles DST and entries that wrap day boundaries well
* **iOS Widgets**
  * A live timer shows today and this week's time on the homescreen
* **Timezone support**
  * All time entries are recorded in the user's current locale by default
  * No locks between start and end timezone -- all can be edited
  * Reporting based around the timezone as perceived as well as any reference
    timezone
* **Simplicity**
  * Import/export everything with wizards
  * Analytics and category organization are both 1st class features
  * Single click to any feature
  * Edit everything

## Blog Posts
-------------

* 10/20 - [Time Tracking]({% post_url 2020-10-15-time-tracking %})
* 10/20 - [Is my timer running?]({% post_url 2020-10-17-is-my-timer-running %})
* 10/20 - [Building a Realtime Widget]({% post_url 2020-10-18-building-a-realtime-widget %})
* 05/21 - [SwiftUI as a Design Tool]({% post_url 2021-05-16-swiftui-as-a-design-tool %})
* 11/22 - [Finishing Time]({% post_url 2022-11-12-finishing-time %})

## Source Code
--------------

* [Time-Client](https://github.com/Tornquist/Time-Client)
* [Time-API](https://github.com/Tornquist/Time-API)
* [Time-Core](https://github.com/Tornquist/Time-Core)

[2017]: {% post_url 2018-02-11-2017-work-analysis %}
