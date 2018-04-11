---
id: 2174
title: 'Heartbleed Aftermath: Changing 163 Password'
date: 2014-04-10T21:02:57+00:00
author: rami
layout: post
guid: http://rtaibah.com/blog/?p=2174
permalink: /2014/04/10/heartbleed-aftermath-changing-163-password/
categories:
  - Geeky
tags:
  - Heartbleed
  - Internet
  - Lastpass
  - Passwords
  - Security
---
<figure id="attachment_2176" style="width: 1024px" class="wp-caption aligncenter"><img src="http://139.59.20.41/wp-content/uploads/2014/04/Screen-Shot-2014-04-10-at-8.38.49-PM-1024x633.png" alt="Lastpass Heartbleed Password Change" width="1024" height="633" class="size-large wp-image-2176" /><figcaption class="wp-caption-text">#OpPasswordChange: Lastpass Heartbleed Password Change</figcaption></figure>
  
Around six month ago, I decided to overhaul my password system, or lack thereof. I basically had two passwords that I used everywhere, both of which were derived from the same pattern. Important sites such as Google or Twitter had a slightly more complicated password. 

My game plan: every site to have a completely random 100 character password. My weapon: <a href="http://lastpass.com" target="_blank">Lastpass</a>. The process was tedious and lengthy (a couple of days.) But helped sleep better.

Enter Heartbleed. [Heartbleed](http://heartbleed.com/) brought all that effort to naught. The worst thing is that you can&#8217;t be sure of anything. Its like a smokescreen of doubt: We don&#8217;t know which passwords were compromised and which weren&#8217;t. I decided to change EVERY password, better safe than sorry.

Luckily, Lastpass makes the process a little easier. Auto-login helps, and their password generator is a blessing. I was able to change 76 passwords in about 4 hours. 20 passwords an hour, or a password every 3 minutes. About 90 more to go! Total: 163

Different UI&#8217;s and experiences were the main problem. Should I be looking in account or profile or settings? Is it privacy or security? Each site had a slightly different definition of all these, and it was up to me to fumble around (I am looking at you Couchsurfing) over and over to find the change password page. 

Lastpass also was not faultless. The different technologies that websites use to build their forms caused major hiccups for the plugin. It failed in updating, detection and reporting in many different ways:

  * Lastpass fails to inform me that it detected a change and that it had in fact updated my password. So I scurry back to my vault to make sure it did.
  * The opposite sometimes happens too. It can fail in detecting a password change. This is troublesome to say the least. When I change a password (which is a 100 random character long, mind you) and the plugin fails to detect the change, you could potentially lock yourself out. Unless you had the foresight of copying the password, there would be noway back short of going through the password reset process. I actually locked myself out of Google and did not have access to the backup E-mail on file. That was a nerve-wrecking 15 minutes.
  * False positives. Last Pass sometimes asks for confirmation of a password change before the website actually accepts the change. For example if a site accepts only 32 character passwords and I input 100 and submit. Lastpass prompts me if I want to change the password on file. If I click &#8216;yes&#8217; before the site spits an error, the actual password gets overwritten and Lastpass is out of sync.
  * Lastpass sometimes fails to report that it changed a password forcing me to go into my vault and manually confirm it.
  * Lastpass plugin sometimes fails to detect a form, or fails to autofill/autogenerate passwords
  * On some websites Lastpass mistakes the &#8216;enter old password&#8217; field to be the username field and inputs my username. Forcing me to go into my vault and copy the actual password.

Here are some protips from a serial password changer:

  * Use password generator. But always copy the password into your clipboard (don&#8217;t forget to overwrite the last password when you are done or want to take a break.)
  * If you password protect your passwords, tick on the don&#8217;t ask for 8 hours or something. Get rid of that pesky prompt until you are done with this process. Trust me you will be going in for manual checks a lot
  * Lastpass saves the history for each password. So if you changed a password in Lastpass but failed to change on the site, you can always go and see the prior password
  * I discovered this after I changed 70 password, but Lastpass has a nifty <a href="https://lastpass.com/?securitychallenge=1&#038;lang=en-US" target="_blank">Heartbleed tool</a> (or click the Lastpass plugins > tools > security check) which detects the last password change and whether the corresponding website changed their own keys or not. If a website changed their keys and your password&#8217;s timestamp is older, it recommends changing the password. If the site has not updated its keys, it tells you to wait<figure id="attachment_2175" style="width: 1024px" class="wp-caption aligncenter">

[<img src="http://139.59.20.41/wp-content/uploads/2014/04/Screen-Shot-2014-04-10-at-7.55.48-PM-1024x613.png" alt="Lastpass Heartbleed detection tool" width="1024" height="613" class="size-large wp-image-2175" />](http://139.59.20.41/wp-content/uploads/2014/04/Screen-Shot-2014-04-10-at-7.55.48-PM.png)<figcaption class="wp-caption-text">Lastpass Heartbleed detection tool</figcaption></figure> 

Heartbleed is a very harsh lesson for the Internet, and a reminder how this whole thing is fragile and could come crumbling down. The system is broken and needs serious attention. I trust [geeks will rally](http://lorddoig.svbtle.com/heartbleed-should-bleed-x509-to-death) around the cause to fix many of these issues. 

What were your experiences with Lastpass or password changing experience in general? I would love to hear from you. Tell me in the comments.