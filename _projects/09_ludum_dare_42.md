---
slug: ludum-dare-42
layout: project
title: "Ludum Dare 42: Running out of Space"
release: August 2018
rel_sort: 90
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
