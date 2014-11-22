---
layout: page
title: Books 
excerpt: "Summarizing books I've read. For my own personal use; shared with the world."
---

<ul class="post-list">
{% for post in site.categories.books %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
