---
title: 'Howto: Upgrade to Adobe Air Beta on Ubuntu'
author: admin
layout: post
permalink: /2008/10/howto-upgrade-to-adobe-air-beta-on-ubuntu/
tweetbackscheck:
- 1236175048
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/6lmcbd";s:4:"isgd";s:17:"http://is.gd/fmeC";s:5:"bitly";s:18:"http://bit.ly/5QfA";s:5:"snipr";s:22:"http://snipr.com/9t12o";s:5:"snurl";s:22:"http://snurl.com/9t12o";s:7:"snipurl";s:24:"http://snipurl.com/9t12o";s:4:"trim";s:17:"http://tr.im/4et9";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:19:"http://zi.ma/d5121d";s:9:"permalink";s:70:"http://hehe2.net/linuxhowto/howto-upgrade-to-adobe-air-beta-on-ubuntu/";}'
twittercomments:
- 'a:4:{i:1095716369;s:5:"17765";i:1040583253;s:5:"17766";i:966576279;s:5:"17767";i:1236681037;s:5:"21308";}'
tweetcount:
- 4
categories:
- Howto
tags:
- Adobe
- Adobe Air
- Howto
- Twhirl
- Ubuntu
- Upgrade
---

![](http://192.168.1.33/blog2/wp-content/uploads/2008/10/adobe-air.jpg)
I love Adobe Air! Applications like Twhirl and Woopra have become an important part of my daily computing arsenal. Over the past 6 month I have been running Adobe Air alpha which wasn't exactly quirk-less. Twhirl never saved my passwords, never minimized to the panel, and the window always had a black shadow around it. A couple of days ago I decided to upgrade to beta, I thought it was going to be a walk in the park, well I was wrong.
Simply downloading the beta version and running it will not work (at least for me). I got a permission error, adding a 'sudo' or logging in as root won't solve the problem either. So what we will need to do is completely remove the alpha version, install beta, and reinstall our Adobe Apps.
First let's remove Adobe Air alpha: 
\`sudo dpkg -r adobeair-enu\`
Then we need to insure that no old traces of Adobe Air exist: 
\`sudo rm -rf /opt/Adobe AIR\`
Clean up the traces from old runtime by deleting .adobe and .macromedia folders from your home directory and /root. 
\`rm -rf $HOME/.adobe $HOME/.macromedia\` 
\`sudo rm -rf /root/.adobe /root/.macromedia.\`
Now, you will need to remove your current installed applications. A combo of dpkg and grep should do the trick. Just type in the name of your apps between the quotes. For example: 
\`dpkg -l | grep "twhirl"\`
\*\*Finally, copy the result and plug it in front of a "sudo dpkg -r"\*\*
Now you have a system fully capable of installing [Adobe Air Beta](http://labs.adobe.com/technologies/air/linux/).
Happy tweaking!