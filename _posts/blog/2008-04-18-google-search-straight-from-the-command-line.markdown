---
title: Google Search Straight From the Command Line!
author: admin
layout: post
permalink: /2008/04/google-search-straight-from-the-command-line/
tweetbackscheck:
- 1236174421
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/7yzv3c";s:4:"isgd";s:17:"http://is.gd/fjwa";s:5:"bitly";s:18:"http://bit.ly/bAyo";s:5:"snipr";s:22:"http://snipr.com/9sjug";s:5:"snurl";s:22:"http://snurl.com/9sjug";s:7:"snipurl";s:24:"http://snipurl.com/9sjug";s:4:"trim";s:17:"http://tr.im/4ah1";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:18:"http://zi.ma/1a6c9";s:9:"permalink";s:71:"http://hehe2.net/internet/google-search-straight-from-the-command-line/";}'
twittercomments:
- 'a:0:{}'
tweetcount:
- 0
categories:
- Apps
- Internet
tags:
- Bash
- CLI
- Command Line
- Google
- Linux
---
[![Google Linux](http://192.168.1.33/blog2/wp-content/uploads/2008/04/google-linux.gif)](http://www.tux-planet.fr/blog//)
[Sebastian Bilbeau](http://www.tux-planet.fr/blog//) authored a script that enables you to Google straight from the comfort of your command line interface! How sweet is that? The script will give you the links of the first 11 result in Google, nothing more nothing less. Meaning don't expect it to give you titles and description, very rudimentary stuff I must say, but still it is kinda neat. Cheers Sebi!
You only need to do two simple things, first of all you will need to install the command line browser lynx:
\> sudo apt-get install lynx
You will then need to download a script authored by
\> wget http://public.tux-planet.fr/shell/script-google
Change permissions and rename:
\> chmod +x google.sh && mv google.sh google
Now here is where the fun starts, execution!
\> rami@rami-desktop:~/Desktop$ ./google Royal HeHe2-ness
\> 
\> http://dd0s.jaiku.com/presence/32174627
\> 
\> /blog/ 
\> /blog/linux-general/etymology-of-a-linux-distro/ 
\> /blog/linux-general/the-7-habits-of-highly-effective-linux-u 
\> /blog/linuxhumor/howto-convert-a-friend-to-linux/
Now only if I could figure out the practicality of this? Any ideas guys? ![:)](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_smile.gif)