---

layout: page
title: Web Zeitgeist 
excerpt: Web stuffs including images, videos, et al, that encompasses the 'spirit' of my web experience at a given time.

---

<h3>Work in progress!</h3>
<div>Web stuffs including images, videos, et al, that encompasses the 'spirit' of my web experience at a given time.</div>

<ul class="post-list">
{% for post in site.categories.Shenanigans %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} </a>
  <div class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></div>
  </article></li>
{% endfor %}
</ul>
