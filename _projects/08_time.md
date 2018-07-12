---
slug: 2017-work-analysis
layout: project
promo_image: time.png
feature_image: time_full.png
promo_description: 2017 Work Analysis
title: 2017 Work Analysis
subtitle: Time Tracking Done Right
release: Feb 2018
featured: true
rel_sort: 41
custom_css:
- colorbox
- youtube_embed
custom_js:
- photoset-grid
- colorbox
---

{% for post in site.posts %}
{% if post.title == page.title %}
  *<strong>Note:</strong> This is a clone of the original [blog post]({{ post.url }}).*
  {{ post.content }}
{% endif %}
{% endfor %}
