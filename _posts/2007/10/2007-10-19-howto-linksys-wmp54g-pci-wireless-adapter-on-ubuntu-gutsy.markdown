---
title: 'HOWTO: Linksys WMP54G PCI Wireless Adapter on Ubuntu (Gutsy)'
author: admin
layout: post
permalink: /2007/10/howto-linksys-wmp54g-pci-wireless-adapter-on-ubuntu-gutsy/
tweetbackscheck:
- 1236173593
- 1236173593
shorturls:
- 'a:11:{s:7:"tinyurl";s:25:"http://tinyurl.com/5x7bec";s:4:"isgd";s:17:"http://is.gd/fiTD";s:5:"bitly";s:18:"http://bit.ly/brTm";s:5:"snipr";s:22:"http://snipr.com/9sftf";s:5:"snurl";s:22:"http://snurl.com/9sftf";s:7:"snipurl";s:24:"http://snipurl.com/9sftf";s:4:"trim";s:17:"http://tr.im/49iw";s:5:"adjix";s:207:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.adjix.com/AdjixAPI.html";s:4:"advu";s:203:"(10 Jan 2008 temporary restriction: API requires valid partnerID or partnerEmail key in request. Contact us if this affects you.) Invalid Adjix request. API documentation @ http://web.ad.vu/AdjixAPI.html";s:4:"zima";s:19:"http://zi.ma/089351";s:9:"permalink";s:86:"http://hehe2.net/linuxhowto/howto-linksys-wmp54g-pci-wireless-adapter-on-ubuntu-gutsy/";}'
twittercomments:
- 'a:0:{}'
tweetcount:
- 0
categories:
- Howto
tags:
- Gutsy
- Howto
- linksys
- Linux
- ndiswrapper
- Ubuntu
- WiFi
- wireless
- wmp54g
---
I have a Dell sitting in my living room with a Linksys WMP54G PCI wireless adapter installed. The adapter worked just fine under Feisty (well TBH I never got the triangular bars icon of wireless connections but the two terminals of wired connections, but do I care??). Anyways I did upgraded to Gutsy on the 17th, just 1 day shy of its official release, by invoking a 'gksu 'update-manager -c', and to my horror the adapter stopped working!! No Internet connection for me! ![:(](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_sad.gif)
I am not sure if this card is not supported under Gutsy, or just something went awry during the upgrade process (will try a Gutsy live CD later), but i tried using the "Windows Wireless Driver" function but to no avail.
Anyways, this is how I managed to get my WMP54G to work under Gutsy:
1-First of all grab the driver from \[here\]\[1\] (XP not Vista)
2-Extract the .exe file using any archive manager and place on your desktop (or where ever you wish)
3-Go to the \[ndiswrapper\]\[2\] homepage, and download the latest release (1.48 to date).
4-Next we will have to install ndiswrapper, so fire up a terminal and navigate to the folder where you downloaded ndiswrapper.
\`tar zxvf ndiswrapper-_version_.tar.gz\` 
\`sudo make uninstall\` 
\`sudo make\` 
\`sudo make install\`
5- If everything went as planned, you should have ndiswrapper installed now, next we will need to install the driver. Assuming that the downloaded driver from step 1 is on your desktop: 
\`ndiswrapper -i ~/Desktop/_WMP54Gversion_/Drivers/WMP54G/Rt2500.INF\`
6-Finally you will have to load the ndiswrapper module. 
\`sudo modprobe ndiswrapper\`
6-In my case this didn't really work, which probably explains why using the "Windows Wireless Driver" function didn't work in the first place. So here is the tricky part, apparently Gutsy already loaded my card's module and is conflicting with the new installed driver. So we will have to remove the modules using rmmod.
\`sudo rmmod rt2500pci rt2x00pci rt2x00lib\`
Thats it! Perhaps you would have to unload ndiswrapper using rmmod and reload it again though.
8-Finally, you will probably need to cement this in order not to do this everytime you restart, so you will have blacklist the three modules we removed. 
\`sudo nano /etc/modprobe.d/blacklist\`
And add these lines:
\`blacklist rt2500pci  
blacklist rt2x00pci  
blacklist rt2x00lib\`
Also add the ndiswrapper in /etc/modules to automatically load it when booting 
\`sudo nano /etc/modules\` 
And add: 
\`ndiswrapper\`
Happy tweaking!! ![:)](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_smile.gif)
\*Edit: If you know of anyway to improve this guide, or have suggestions, or other workarounds. Please comment or E-mail me. \*
\[1\]: http://www.linksys.com/servlet/Satellite?blobcol=urldata&blobheadername1=Content-Type&blobheadername2=Content-Disposition&blobheadervalue1=application%2Fx-msdownload&blobheadervalue2=inline%3B+filename%3DWMP54Gv4\_20050503.exe&blobkey=id&blobtable=MungoBlobs&blobwhere=1130824506903&ssbinary=true&lid=7513643981B16
\[2\]: http://ndiswrapper.sourceforge.net/joomla/