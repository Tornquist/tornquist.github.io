---
layout: default
title: Blog
permalink: /blog/
---
<style>
  .catblocs > .catbloc:target ~ .catbloc:last-child, .catblocs > .catbloc {
    display: none;
  }
  /* :last-child works, but for some reason .catbloc:last-child will not */
  .catblocs > :last-child, .catblocs > .catbloc:target {
    display: block;
  }
</style>

<script>
  function keepLocation(oldOffset) {
    if (window.pageYOffset!= null){
      st=oldOffset;
    }
    if (document.body.scrollWidth!= null){
      st=oldOffset;
    }
    setTimeout('window.scrollTo(0,st)',0);
  }
  toggleBlogBtnColors = function(id) {
    $.each($('.btn-filter'), function( index, value) {
      classie.remove(value, 'btn-primary');
    });

    lookup = id + "_btn";
    classie.add($(lookup)[0], 'btn-primary');
  };
  clickBlogBtn = function(id) {
    keepLocation(window.pageYOffset);
    toggleBlogBtnColors(id);
  };
  $(function() {
    resetBlogBtnColors = function() {
      filter = window.location.hash;
      if (filter == "") {
        toggleBlogBtnColors("#allposts");
      } else  {
        toggleBlogBtnColors(filter);
      }
    };
    resetBlogBtnColors();
  });
</script>

<div class="row">
  <div class="col-md-8 col-md-offset-2">
  <a href="#allposts" class="btn btn-default btn-filter" onclick="clickBlogBtn('#allposts');" id="allposts_btn">All Posts</a>
     {% for category in site.categories %}
       <a class="btn btn-default btn-filter" href="#{{ category | first | remove:' ' }}" onclick="clickBlogBtn('#{{ category | first | remove:' '}}');" id="{{ category | first | remove:' '}}_btn"> {{ category | first | capitalize }} </a>
     {% endfor %}
   </div>
 </div>
 <div class="row">
  <div class="col-md-8 col-md-offset-2">
    <div class="catblocs">
      {% for category in site.categories %}
        <div class="catbloc" id="{{ category | first | remove:' ' }}">
          {% for posts in category %}
            {% for post in posts %}
              {% if post.title %}
                <div class="row">
                  <div class="col-sm-12">
                      <h2>
                        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
                        <br/>
                        <small>
                          {{ post.date | date: "%b %-d, %Y" }}
                          {% if post.categories %}
                            {% for category in post.categories %}
                              &middot; {{ category }}
                            {% endfor %}
                          {% endif %}
                        </small>
                      </h2>
                      <hr>
                  </div>
                </div>
              {% endif %}
            {% endfor %}
          {% endfor %}
        </div>
      {% endfor %}
      <!-- All Posts is last, so therefor default -->
      <div class="catbloc" id="allposts">
        {% for post in site.posts %}
          <div class="row">
            <div class="col-sm-12">
                <h2>
                  <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
                  <br/>
                  <small>
                    {{ post.date | date: "%b %-d, %Y" }}
                    {% if post.categories %}
                      {% for category in post.categories %}
                        &middot; {{ category }}
                      {% endfor %}
                    {% endif %}
                  </small>
                </h2>
                <hr>
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  </div>
</div>
