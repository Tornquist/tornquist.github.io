---
layout: post
title: Building for Reader View
date: 2021-05-26 08:00:00
categories: programming
---

This website has displayed well in both browser and app-based reader modes with
the exception of image galleries. I've been writing about building and iterating
on the UI for Time recently and these highly visual posts need images for the
content to make sense.

Without a fix, a horizontal row of images would either be hidden in reader mode
or would pivot to a vertical list. This means that content is either missing
completely or so tall that it's unwieldy to read the article (shown below). Reader
mode was actively making it harder to read the posts that I have been writing.

This _really_ bothered me.

{% comment %}
!@ generate_image assets/2021/05/broken-examples.png
  assets/2021/05/correct-safari-2.png
  assets/2021/05/broken-reader-2.png
  assets/2021/05/broken-safari-2.png
!@ end_generate
{% endcomment %}

<figure>
  <img class="image" src="/assets/2021/05/broken-examples.png">
  <figcaption>
    <i>Safari</i> base webpage, <i>Reeder</i> Reader Mode, <i>Safari</i> Reader Mode
  </figcaption>
</figure>

I needed a solution that would:

1. Make sure images are shown in reader mode
1. Force images to display in a row
1. Maintain easy including/inserting of images
1. Preserve styles of the normal site (non reader mode)
1. Maintain easy deployment with base github actions

After reading a lot about how reader modes worked and trying to fix the display
problems with metadata, I came to the conclusion that I really needed a way to
generate composite images easily because:

* Single images display properly in reader mode (fixes #1)
* Single images do not wrap (fixes #2)
* Generated images are maintainable (fixes #3)
* Generated images could match styles and be regenerated (fixes #4)
* Local generation maintains deployment (fixes #5)
* Github actions could verify _correct_ images (fixes #5)

To generate these images I wrote a script that would:

1. Scan the project and posts folders
1. Search for "start image generation" tags
1. Scan the following lines for image paths
1. Close a "generation request" when a "stop image generation" tag was found
1. Use image magick to stitch all of the images together with padding and a
  transparent background

In addition to scanning for generation requests, I also use regex to find the
styles in `main.css` that controls the existing galleries. I can then run
`make images` to generate fresh images from a change in the styles or a change
in a particular post.

{% include photo.html alt="`make images` output" img="/assets/2021/05/website-build-images.png" %}

The original way to add a row of images was with a photos include file.

```
{% raw %}
 {% include photos.html
   height="<height>" id="<html element id>"
   img1="<image path>
   img2="<image path>"
   img3="<optional image page>"
   img4="<optional image page>"
   img5="<optional image page>"
 %}
{% endraw %}
```

With generated images, I instead use:

```
{% raw %}
 {% comment %}
 !@ generate_image <generated output path>.png
   <input image path 1>.pngmake
   ...
   <input image path n>.png
 !@ end_generate
 {% endcomment %}

 {% include photo.html img="<generated output path>.png" %}
{% endraw %}
```

By using a jekyll comment, I keep the generation request next to the usage.
It's very easy to read the code and see what images will be included and will
be displayed on the page. I can even start writing with the normal include, and then
swap a few lines to generate an image for the final publishing.

I like that no magic is being done. The posts display as written and if images
need to be generated they can be via an explicit action. The generated images match
the original formatting and the articles now display correctly in reader mode.

Problem solved!

{% comment %}
!@ generate_image assets/2021/05/website-comparison.png
  assets/2021/05/website-base.png
  assets/2021/05/website-reader-mode.png
!@ end_generate
{% endcomment %}

{% include photo.html img="/assets/2021/05/website-comparison.png" %}

---

Further reading:

1. Daniel Aleksandersen has an excellent blog series _[Web Reading Mode][1]_
  explaining the technical differences between readers and different platforms.
2. Scott Vinkle's post _[How Does HTML Microdata Help With Accessibility?][2]_
  is a helpful resource on microdata that I used to configure dates and bylines.
3. Mandy Michael's post _[Building websites for Safari Reader Mode and other
  reading apps][3]_ is another good resource on microdata and instapaper's
  reader mode.

[1]: https://www.ctrl.blog/entry/browser-reading-mode-parsers.html
[2]: https://scottvinkle.me/blogs/work/how-html-microdata-helps-with-accessibility
[3]: https://medium.com/@mandy.michael/building-websites-for-safari-reader-mode-and-other-reading-apps-1562913c86c9