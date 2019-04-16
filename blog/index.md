---

layout: page
title: Blog
excerpt: "An archive of blog posts sorted by date."

---

<ul class="post-list">
{% for post in site.categories.Blog%} 
  <li>
    <article>
      <h3><a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} </a></h3>
      <div class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></div>
      {{ post.content | strip_html | truncatewords: 50 }}
    </article>
  </li>
{% endfor %}
</ul>
