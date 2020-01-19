---

title: "Web Design for a 7 Year Old"
author: rami
layout: historical-blog 
categories: [Blog]
image: keynan-taibah-first-website.png
tags: keynan

---
![Keynan Taibah first website](/assets/images/content/blog/keynan-taibah-first-website.png)

Over the past year I have been trying to teach my 6 year old Python through games. I was using [insert book here]. The book starts with teaching the basics of programming like variables, strings, loops...etc. This was a bit uninspiring to him, since these concepts were a bit too abstract. The lack of immediate results didn't help either. Great you assigned a number to a variable. Now what? We experimented with Turtle a few times and he really enjoyed changing colors, and doing loops to create interesting shapes. But still the leap from the basics to an actual playable game was a bit too big.

Which got me thinking, why not start with basic web design? With HTML/CSS there is almost no logic and the results are immediate. So over the past weekend, I asked Keynan, if he wants to build his own website. He didn't know what a website was. After I explained, he was like 'oh so like an app?' Woe to me. 🤦

we sat down on the kitcken table and his trusty sky blue HP laptop as I told him about `<header>`, `footer`, and `body` tags using a simple wireframe. He wasn't impressed. Theoretical is not your thing son? Fine. I fire up Vim (don't worry I intorudce him to Gedit later) and type 'Hi Keynan' inside a `<p>` tag and launched the file in the browser. His eyes lit up for a brief second. As if saying 'ok that's nice but not all that impressive'...So I envelope his name in a `strong` then an `em`. Same look.

I had my secret weapon though. Color! That ought to get his attention. I introduce a `style` tag to the document and instruct it to color `p` tags blue. Excitedly I switch to the browser and hit refresh. Nothing. Still boring black. Well that's embarassing. After a few minutes of debugging, I find the culprit. I had my syntax wrong (thank you CSS-in-JS, Saas, React et al.) Back to business.

The intoduction of color was what made it click to him. He said I want the phrase 'Hi Keynan' in an alternating black, white, and pink. I explained to him that white won't work since the background is white. Why don't we do black and pink only? He begrudgingly conceded. I quickly wrapped the letters we wanted pink in `span`s and gave them `color: pink` styles. Now I have his full attention.

Adding images was the most interesting part for him. He really enjoys finding wallpapers of his favorite things and cycling the desktop every now and then. I show him how to copy and paste images from the wallpaper folder to his project folder and renaming the images to make them easier to type in vim. He then proceeds adding 7 images one-key-at-a-time by copying my first `img` line. 

Up to this point this project was doomed to sit lonely in `/home/keynan`, but then I thought it would  be really cool to actually publish it. So I add a few styles to make a grid out of his images, add borders to them, and a throw in a hot pink background (of his choosing) to the document. I then create a github account for him, link up the repo to Netlify, and hook up his domain (which I bought 7 years ago). Voila. He now has a brand [new website](https://keynantaibah.com). 

Over the weekend he kept shopping his website proudly to everybody he met. He would go up to an aunt or uncle and ask them for their phones to show them his new website.

