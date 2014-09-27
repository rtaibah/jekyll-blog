---
title: 'Hacking Symantec: Easy Peasy'
author: admin
layout: post
permalink: /2008/06/hacking-symantec-easy-peasy/
tweetbackscheck:
- 1236162956
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/6n9rrh";s:4:"isgd";s:17:"http://is.gd/fjaG";s:5:"bitly";s:18:"http://bit.ly/Gi1D";s:5:"snipr";s:22:"http://snipr.com/9shir";s:5:"snurl";s:22:"http://snurl.com/9shir";s:7:"snipurl";s:24:"http://snipurl.com/9shir";s:4:"trim";s:17:"http://tr.im/49yq";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:19:"http://zi.ma/e98494";s:9:"permalink";s:63:"http://hehe2.net/linuxobservations/hacking-symantec-easy-peasy/";}'
twittercomments:
- 'a:0:{}'
tweetcount:
- 0
categories:
- Observations
- The Dark Side
tags:
- Hacking
- Norton
- Symentac
---

Last week, the IT department had an epiphany, they decided to replace Mcafee Anti-Virus with Norton on all employees computers. Since I work in a company technologically retarded, the announcement almost went unnoticed with minimal opposition from all the departments. Only a handful (actually one besides me) didn't like the decision. We discussed it a bit, that Norton is a resource hog, and will probably slow up our systems. However we begrudgingly obliged.

While I knew that my system was screwed, since I didn't defragment for some time, had loads of unnecessary applications, didn't clean my registry for a few month...etc. You know how XP could become after a couple of month of usage. The Norton installation was like the last nail in my laptops coffin. The system has become so annoyingly slow, that on more than one occasion I almost punched the screen! Switching between applications could take up to 30 seconds, sending out an E-mail would take another 30 seconds, random freezes while typing a document, it really got frustrating. I decided to take matters into my own hands. Step one: be the technological renegade I always been, get rid of Norton!

So I fire up my Control Panel, and then click on the Add/Remove Programs icon, click on the damn Norton icon and Remove. Oh oh not so fast cowboy, I needed a password:

[![](http://docs.google.com/a/linuxologist.com/File?id=dff3md6g_26frh2g5t7_b)](File?id=dff3md6g_26frh2g5t7_b)

At this point, a lot of ideas crossed my mind, smart guessing, brute force, social engineering...etc. But I decided to appeal to Google, maybe there was a default password I could use. After a quick 30 second Google, I landed on a forum, someone had the same exact problem I had, one suggested to fire up the Task Manager and kill a process run by the user (not System) called Msiexec.exe. My first thought, was NO WAY, it can't be that easy! But decided to try it.

[![](http://docs.google.com/a/linuxologist.com/File?id=dff3md6g_27ftbx77cz_b)](File?id=dff3md6g_27ftbx77cz_b)

Lo and Behold! The uninstallation rolled and I had a Norton free system within a minute!

Now my question is: is this the kind of security millions of computer users and thousands of corporation depending on? How can such a hack go unnoticed for multiple versions (yes it has been around even for earlier versions) by such a "leading" computer security company? Didn't any one report it? File a bug? Security through obscurity my ass!