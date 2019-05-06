---

layout: page
title: Blog
excerpt: "An archive of blog posts sorted by date."
pagination: 
  enabled: true
  category: Blog 

---

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
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/{{ post.video }}?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      {% endif %}

      {% if post.image %}
        <a class="post-thumb" href="{{ site.siteurl }}{{ post.url }}">
          <img src="{{ site.baseurl }}/assets/images/content/blog/{{ post.image }}">
        </a>
      {% endif %}

      {{ post.content | strip_html | truncatewords: 50 }}<a href="{{ site.siteurl }}{{ post.url }}"> continue reading</a>
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

