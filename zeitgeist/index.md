---

layout: page
title: Web Zeitgeist 
excerpt: "Web stuffs including images, videos, et al, that encompasses the 'spirit' of my web experience at a given time."
pagination: 
  enabled: true
  category: Zeitgeist 

---

<div class="description-blue">Over the years I blogged/shared (read: overshared) many things. This Web Zeitgeist holds all the things I shared but don't really fit in a blogpost, nor are they personal. It mostly contains memes, viral content, and intersting things I found around the web. It encompasses the 'spirit' of my web experience at a given time.</div>


{% if paginator.total_pages > 1 %}
<ul class="paginator">
  {% if paginator.previous_page %}
  <li>
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Newer</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="older">
    <a href="{{ paginator.next_page_path | prepend: site.baseurl }}">Older</a>
  </li>
  {% endif %}
</ul>
{% endif %}

<ul class="post-list">
{% for post in paginator.posts %}
  <li>
    <article>
      <h3><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} </a></h3>
      <div class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></div>

      {% if post.video %}
      <div class="iframe-container">
        <iframe src="https://www.youtube-nocookie.com/embed/{{ post.video }}?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
      {% endif %}

      {% if post.image %}
        <a class="post-thumb" href="{{ site.siteurl }}{{ post.url }}">
          <img src="{{ site.baseurl }}/assets/images/content/zeitgeist/{{ post.image }}">
        </a>
      {% endif %}

      {{ post.content | strip_html | truncatewords: 50 }}
    </article>
  </li>
{% endfor %}
</ul>




{% if paginator.total_pages > 1 %}
<ul class="paginator">
  {% if paginator.previous_page %}
  <li>
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Newer</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="older">
    <a href="{{ paginator.next_page_path | prepend: site.baseurl }}">Older</a>
  </li>
  {% endif %}
</ul>
{% endif %}
