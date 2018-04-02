---

layout: page
title: Photostream 
excerpt: "Pictures from my life"

---

<ul class="post-list">
{% for post in site.categories.Photostream %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
