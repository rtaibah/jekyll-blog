---

layout: page
title: Web Zeitgeist 
excerpt: Web stuffs including images, videos, et al, that encompasses the 'spirit' of my web experience at a given time.

---

<div class="description-blue">Over the years I blogged/shared (read: overshared) many things. This Web Zeitgeist holds all the things I shared but don't really fit in a blogpost, nor are they personal. It mostly contains memes, viral content, and intersting things I found around the web. It encompasses the 'spirit' of my web experience at a given time.</div>

<ul class="post-list">
{% for post in site.categories.Shenanigans %} 
  <li><article><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} </a>
  <div class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></div>
  </article></li>
{% endfor %}
</ul>
