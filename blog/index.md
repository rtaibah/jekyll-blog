---

layout: page
title: Blog
excerpt: "An archive of blog posts sorted by date."

---

<ul class="post-list">
{% for post in site.categories.Blog%} 
  <li>
    <article>
      <a href="{{ site.siteurl }}{{ post.url }}">{{ post.title }} </a>
      <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>
    </article>
  </li>
{% endfor %}
</ul>
