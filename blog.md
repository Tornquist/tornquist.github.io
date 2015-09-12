---
layout: default
title: Blog
permalink: /blog/
---
<script>
  toggleBlogBtnColors = function(id) {
    $.each($('.btn-filter'), function( index, value) {
      classie.remove(value, 'btn-primary');
    });

    lookup = id + "_btn";
    classie.add($("#" + lookup)[0], 'btn-primary');
  };

  toggleSections = function(id) {
    var posts = $('.blog_post');
    var numPosts = posts.length;
    for (var i = 0; i < numPosts; i++) {
      var post = posts[i];
      if ($(post).hasClass(id) == true) {
        $(post).show();
      } else {
        $(post).hide();
      }
    }
  };

  clickBlogBtn = function(id) {
    toggleBlogBtnColors(id);
    toggleSections(id);
  };

  $(function() {
    toggleBlogBtnColors("blog_post");
    toggleSections("blog_post");
  });
</script>

<div class="row">
  <div class="col-md-8 col-md-offset-2">
  <a class="btn btn-default btn-filter" onclick="clickBlogBtn('blog_post');" id="blog_post_btn">All Posts</a>
     {% for category in site.categories %}
       <a class="btn btn-default btn-filter" onclick="clickBlogBtn('cat_{{ category | first | remove:' '}}');" id="cat_{{ category | first | remove:' '}}_btn"> {{ category | first | capitalize }} </a>
     {% endfor %}
   </div>
 </div>
 <div class="row">
  <div class="col-md-8 col-md-offset-2">
    {% for post in site.posts %}
      <div class="row blog_post {% for category in post.categories%}cat_{{ category }}{% endfor %}">
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
