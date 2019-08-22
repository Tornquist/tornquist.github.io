---
slug: quest
layout: project
title: Quest
release: June 2017
featured: true
rel_sort: 70
custom_css:
- youtube_embed
- syntax
---

{% for post in site.posts %}
{% if post.title == page.title %}
  *<strong>Note:</strong> This is a clone of the original [blog post]({{ post.url }}).*
  {{ post.content }}
{% endif %}
{% endfor %}
