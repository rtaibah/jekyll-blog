---

layout: page
title: Lifestream 
excerpt: "Images from my life; shared online"

---

<div class="description-blue">Over the years I have shared many personal pictures over multiple platforms like Instagram & Path. However I have come to regret that decision mainly for privacy concerns. Since then, I have retreated from these platforms and moved all my data on to this website. This is my Lifestream.</div>

<ul class="post-list">
{% for post in site.categories.Lifestream %} 
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
