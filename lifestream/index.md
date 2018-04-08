---

layout: page
title: Lifestream 
excerpt: "Images from my life; shared online"

---

<h3>Work in progress</h3>
<div>Images from my life. This will be my personal Instagram</div>

<ul class="post-list">
{% for post in site.categories.Lifestream %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
