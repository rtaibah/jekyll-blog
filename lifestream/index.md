---

layout: page
title: Lifestream 
excerpt: "Images from my life; shared online"
pagination: 
  enabled: true
  category: Lifestream 

---


<div class="description-blue">Over the years I have shared many personal pictures over multiple platforms like Instagram & Path. However I have come to regret that decision mainly for privacy concerns. Since then, I have retreated from these platforms and moved all my data on to this website. This is my Lifestream.</div>

{% if paginator.total_pages > 1 %}
<ul class="paginator">
  {% if paginator.previous_page %}
  <li>
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Newer</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li>
    <a href="{{ paginator.next_page_path | prepend: site.baseurl }}">Older</a>
  </li>
  {% endif %}
</ul>
{% endif %}
<ul class="post-list">

{% for post in paginator.posts %}
  <li>
    <article>
      <h3>
        <a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }}</a>
      </h3>
        <a href="{{ site.siteurl }}{{ post.url }}">
          <img src="{{ site.baseurl }}/assets/images/content/lifestream/{{ post.image }}">
        </a>
      <div class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></div>
    </article>
  </li>
{% endfor %}
</ul>
