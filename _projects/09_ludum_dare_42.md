---
slug: ludum-dare-42
layout: project
promo_image: ld42.png
feature_image: ld42.png
promo_description: Ludum Dare 42
title: "Ludum Dare 42: Running out of Space"
release: Aug 2018
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
