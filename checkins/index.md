---

layout: page
title: Checkins 
excerpt: "Places in the world I've been to"

---

<h3>Work in progress</h3>
<div>Places in teh world I've been to. This is my personal Foursqure.</div>

<ul class="post-list">
{% for post in site.categories.Checkins %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
