---
title: 'Howto: Fresh Ubuntu Install Without Losing Your Current Settings'
author: admin
layout: post
permalink: /2008/11/howto-fresh-ubuntu-install-without-losing-your-current-settings/
tweetbackscheck:
- 1236174529
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/58alep";s:4:"isgd";s:17:"http://is.gd/77h7";s:5:"bitly";s:18:"http://bit.ly/HAGr";s:5:"snipr";s:22:"http://snipr.com/9sg5c";s:5:"snurl";s:22:"http://snurl.com/9sg5c";s:7:"snipurl";s:24:"http://snipurl.com/9sg5c";s:4:"trim";s:17:"http://tr.im/49ks";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:19:"http://zi.ma/7a1d25";s:9:"permalink";s:92:"http://hehe2.net/linuxhowto/howto-fresh-ubuntu-install-without-losing-your-current-settings/";}'
twittercomments:
- 'a:7:{i:1098583646;s:5:"17650";i:1056101533;s:5:"17651";i:1003468450;s:5:"17652";i:1003468397;s:5:"17653";i:1002916609;s:5:"17654";i:1002914701;s:5:"17655";i:1001893383;s:5:"17656";}'
tweetcount:
- 7
categories:
- Howto
tags:
- Install
- Linux
- opensource
- Ubuntu
---

![](http://192.168.1.33/blog2/wp-content/uploads/2008/11/ubuntu-distros.jpg)

**Warning**: There are  two commands mentioned in this how to, both that require double dashes -- -- but for some reason WordPress is not rendering that correctly. After each _dpkg_ hit _space_ and hit the dash button twice. Sorry for the the inconvenience.
A clean install or an upgrade? That's a question that keeps [tossed around](http://www.linux.com/feature/134517 "tossed around") every new \*\*Ubuntu\*\* release. Common wisdom would suggest that a clean install would probably be better, however the inconvenience of losing current installed apps and configuration makes most of us shy away from this path. But what if I told you that you could have the good of both worlds? A fresh install and keeping your apps and configuration intact?
\#\#\# Configuration
Keeping your configuration intact is pretty straight forward and obvious. Just backup your /home folder onto an external drive or whatever. Make sure you also **grab the hidden files**, don't [do my mistake](http://twitter.com/bianconeri4ever/status/999382370 "do my mistake")!
\#\#\# Applications
Now for the current applications. Basically we just need to make a full list of the installed apps.
\`sudo dpkg --get-selections \> /home/user/package.selections\`
Of course don't forget to backup \*package.selections \*on the external hard-drive. Also you should backup your \*/etc/apt/sources.list\* file since you probably have some extra sources listed over there. Now you can go about your business and do a fresh install.
\#\#\# Restore
Once your done with the fresh install, copy the file\* package.selections\* into your home. Then copy your \*sources.list\* file into /etc/apt/ and update it to match your current distro (e.g Gutsy --\> Intrepid) you can use CTRL + H in gedit for that. Then do a "sudo apt-get update" ,and finally invoke:
\`sudo dpkg --set-selections /home/package.selections && apt-get dselect-upgrade\`
apt-get will now start downloading all your apps, this will take some time depending on the number of apps you have installed.
Once that's done, just copy your backup-ed /home over the current /home (again don't forget hidden folders).
Log out and log back in to your shiny new fresh install!
\*\*Edit:\*\* As the commentators below also mentioned, it would also be wise to have your /home in a seperate partition (thanks Boo Radley), back  up /etc (thanks Bartek), and use the tar command to back up home (it will preserve your structure and permissions)