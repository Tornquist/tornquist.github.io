---
slug: 2017-work-analysis
layout: project
title: 2017 Work Analysis
release: February 2018
featured: true
rel_sort: 80
custom_css:
- youtube_embed
---

{% for post in site.posts %}
{% if post.title == page.title %}
  *<strong>Note:</strong> This is a clone of the original [blog post]({{ post.url }}).*
  {{ post.content }}
{% endif %}
{% endfor %}
