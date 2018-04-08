---

layout: page
title: Notes 
excerpt: "My notes, aka tweets"

---

<h3>Work in progress</h3>
<div>Notes aka Tweets. This space will be used to archive my tweets.</div>

<ul class="post-list">
{% for post in site.categories.Notes %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
