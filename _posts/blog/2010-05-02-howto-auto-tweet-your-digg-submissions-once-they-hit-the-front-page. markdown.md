---
id: 287
title: 'Howto: Auto-Tweet Your Digg Submissions Once They Hit The Front Page'
date: 2010-05-02T21:57:00+00:00
author: rami
layout: post
guid: http://rtaibah1.wordpress.com/2010/05/02/howto-auto-tweet-your-digg-submissions-once-they-hit-the-front-page
permalink: /2010/05/02/howto-auto-tweet-your-digg-submissions-once-they-hit-the-front-page/
posterous_39894d3ad3d9f6a441052a50351e8a54_post_id:
  - "17975449"
  - "17975449"
  - "17975449"
posterous_39894d3ad3d9f6a441052a50351e8a54_permalink:
  - http://blog.ramitaibah.com/howto-tweet-your-digg-submissions-once-they-h
  - http://blog.ramitaibah.com/howto-tweet-your-digg-submissions-once-they-h
  - http://blog.ramitaibah.com/howto-tweet-your-digg-submissions-once-they-h
categories:
  - Uncategorized
---
As most of you know, I am an avid Digger (<a href="http://digg.com/users/rtaibah" target="_blank">rtaibah</a>.) So yesterday, I thought how cool would it be if I could auto-tweet any Digg story I submit once it hit the home page. Unfortunately, Digg provides RSS feeds for users&#8217; submits only, but not popular stories submitted by users. Enter Yahoo Pipes!

The trick here is to grab the general popular story feed from Digg, feed to it Yahoo Pipes, and filter it to pull stories submitted by you. Lets start shall we?

First, you can use&nbsp;<a href="http://feeds.digg.com/digg/popular.rss" target="_blank">Digg&#8217;s popular feed</a>&nbsp;but if you use this feed, your tweets will lead to the Digg story on Digg. Instead, I grabbed the popular feed from <a href="http://feeds.feedburner.com/Socialblade-DiggFrontpageData" target="_blank">Socialblade</a>&nbsp;which links to the original story NOT Digg. Anyways you can use either.

Next head to <a href="http://pipes.yahoo.com/pipes/" target="_blank">Yahoo Pipes</a>&nbsp;and if you don&#8217;t have a Yahoo account get one (or dig up that one you haven&#8217;t used for 7 years :)) Now here is the fun part:

Click on &#8220;Create Pipe&#8221; on the top right, the pipes editor will appear:

<div class='p_embed p_image_embed'>
  <a href="http://139.59.20.41/wp-content/uploads/2011/12/yahoo-pipes-digg-tutorial-1-scaled1000.png"><img alt="Yahoo-pipes-digg-tutorial-1" height="273" src="http://139.59.20.41/wp-content/uploads/2011/12/yahoo-pipes-digg-tutorial-1-scaled1000.png?w=300" width="500" /></a>
</div>

Under Sources, drag and drop &#8220;Fetch Feed&#8221; to the Pipes canvas. Under Operators, drag and drop &#8220;Filter.&#8221; Then fill one of the two feeds I provided earlier in the feed field, and choose &#8220;item.description -> does not contain -> your username&#8221; as follows:

<div class='p_embed p_image_embed'>
  <a href="http://rtaibah1.files.wordpress.com/2010/05/yahoo-pipes-digg-tutorial-2-scaled1000.png"><img alt="Yahoo-pipes-digg-tutorial-2" height="274" src="http://rtaibah1.files.wordpress.com/2010/05/yahoo-pipes-digg-tutorial-2-scaled1000.png?w=300" width="500" /></a>
</div>

Don&#8217;t forget to link the pipes like in the above screenshot. Save your work, then click on &#8220;My Pipes&#8221; you will see your feed that you just created. Hover over it, and click &#8220;view results.&#8221; There you will get an RSS icon that links to that feed. Now all you have to do is feed into one of the many auto-tweeting services like <a href="http://twitterfeed.com" target="_blank">twitterfeed</a> or <a href="http://hootsuite.com" target="_blank">hootsuite</a>.

Here is the result:

<div class='p_embed p_image_embed'>
  <a href="http://139.59.20.41/wp-content/uploads/2011/12/screenshot-3-scaled1000.png"><img alt="Screenshot-3" height="185" src="http://139.59.20.41/wp-content/uploads/2011/12/screenshot-3-scaled1000.png?w=300" width="500" /></a>
</div>

&nbsp;

&nbsp;