---

layout: page
title: Books 
excerpt: "Summarizing books I've read. For my own personal use; shared with the world."

---
<h3>Work in progress</h3>
<div>This section is to summarize books I've read.</div>
<ul class="post-list">
{% for post in site.categories.Books %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
