---
layout: default
title: Projects
permalink: /projects/
section_id: portfolio
section_class: bg-light-gray
---

<div class="row">
{% for project in site.projects %}
  <div class="col-md-4 col-sm-6 portfolio-item">
    <a class="portfolio-link" data-toggle="modal" href="#bad_link">
      <div class="portfolio-hover">
        <div class="portfolio-hover-content">
          <i class="fa fa-plus fa-3x"></i>
        </div>
      </div>
      <img alt="{{ project.title }}" class="img-responsive" src="/assets/images/projects/{{ project.promo_image }}">
    </a>
    <div class="portfolio-caption">
      <p class="text-muted">
        {{ project.promo_description }}
      </p>
    </div>
  </div>
{% endfor %}
</div>
