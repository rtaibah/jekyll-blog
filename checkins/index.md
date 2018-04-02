---
layout: page
title: Checkins 
excerpt: "Places in the world I've been to"
---

<ul class="post-list">
{% for post in site.categories.Checkins %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
