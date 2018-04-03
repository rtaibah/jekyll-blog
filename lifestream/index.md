---

layout: page
title: Lifestream 
excerpt: "Images from my life; shared online"

---

<ul class="post-list">
{% for post in site.categories.Lifestream %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
