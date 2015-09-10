---
layout: default
title: Blog
permalink: /blog/
---

{% for post in site.posts %}
  <div class="row">
    <div class="col-sm-8 col-sm-offset-2">
      <div class="page-header">
        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
          <small>{{ post.date | date: "%b %-d, %Y" }}</small>
        </h2>
      </div>
    </div>
  </div>
{% endfor %}
