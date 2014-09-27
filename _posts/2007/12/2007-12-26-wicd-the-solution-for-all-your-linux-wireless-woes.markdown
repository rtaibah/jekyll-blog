---
title: 'Wicd: The Solution For All Your Linux Wireless Woes!'
author: admin
layout: post
permalink: /2007/12/wicd-the-solution-for-all-your-linux-wireless-woes/
tweetbackscheck:
- 1236174623
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/7gkt4s";s:4:"isgd";s:17:"http://is.gd/fjua";s:5:"bitly";s:18:"http://bit.ly/teZh";s:5:"snipr";s:22:"http://snipr.com/9sjnm";s:5:"snurl";s:22:"http://snurl.com/9sjnm";s:7:"snipurl";s:24:"http://snipurl.com/9sjnm";s:4:"trim";s:17:"http://tr.im/4afz";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:19:"http://zi.ma/3f5318";s:9:"permalink";s:79:"http://hehe2.net/linuxhowto/wicd-the-solution-for-all-your-linux-wireless-woes/";}'
twittercomments:
- 'a:2:{i:1116308511;s:7:"retweet";i:1116281959;s:7:"retweet";}'
tweetcount:
- 2
categories:
- Howto
---
\#\#\#\#\# \*Update: Lately this article has been getting some traffic from StumbleUpon and Reddit, however I would just like to bring to your attention that this is almost 9 month old. I personally haven't used Wicd for quite a long time, not really a fan of wireless. Anyways, my original [source](http://www.lockergnome.com/linux/2007/10/18/ubuntu-gutsy-wireless-help/) is currently recommending going back to Network Manager. Proceed at your own risk :))\*
Last week I got a phone call from my cousin asking for help with his laptop, and apparently my Linux evangelism paid off and I heard from the other end "Rami, I want you to install Linux on my laptop." Like any Linux geek, I happily obliged. I burned an Ubuntu Gutsy CD and installed it for him. Besides some auto mounting glitches that were fixed fairly quickly, everything went fine.
However, a few days ago, I got the highly anticipated and dreaded after-call that something wasn't right. He went back to his folks house and he couldn't connect to their wireless network. I sensed trouble instantly, Ubuntu and wireless aren't real good friends. So I headed down there to try to fix his issue. Apparently he needed to have WEP + static IP in order to connect. After a few trial and errors with the Ubuntu Network Manager, it became evident that it is WORTHLESS! It is so buggy and unfriendly I almost gauged my eyeballs!
So I Googled away, jumping from forum to forum, and blog to another. Nothing seemed to work! after around 3 hours I almost gave up, until I stumbled into a [lockergnome](http://www.lockergnome.com "lockergnome") [post](http://www.lockergnome.com/linux/2007/10/18/ubuntu-gutsy-wireless-help/ "post") by [Matt Harley](http://www.lockergnome.com/linux/author/matt-hartley/ "Matt Harley"). Now this was not your regular Howto, it was more of a rant (a video one also!), Matt recommended a program called [wicd](https://sourceforge.net/project/showfiles.php?group_id=194573 "wicd"). Abra cadabra it worked!
[wicd](https://sourceforge.net/project/showfiles.php?group_id=194573 "wicd") is such a nice program, I really don't know why Ubuntu (and other distros) don't include it. It is miles ahead of the default Gnome network manager, I can't understand how you can call a network manager a manager if you can't configure each connection by right clicking on it or whatever. With [wicd](https://sourceforge.net/project/showfiles.php?group_id=194573 "wicd") I can add an IP, gateway, subnetwork mask to each connection. I can also choose the type of encryption of each network and add specific scripts!!
Thank you Matt for sharing your expertise with us, and I will be definitely reading reading your articles [lockergnome](http://www.lockergnome.com "lockergnome") from now on! ![:)](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_smile.gif)