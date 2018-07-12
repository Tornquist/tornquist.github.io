---
slug: quest
layout: project
promo_image: quest.png
feature_image: quest_full.png
promo_description: Digital Scavenger Hunt
title: Quest
subtitle: ECE477 Senior Design
release: June 2017
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
