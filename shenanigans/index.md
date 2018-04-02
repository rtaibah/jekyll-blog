---
layout: page
title: Shenanigans 
excerpt: "Internet shenanigans, which includes images, videos, et al, I found interesting or fun over the years"
---

<ul class="post-list">
{% for post in site.categories.Shenanigans %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
