---

title: "Web Design for a 7 Year Old"
author: rami
layout: historical-blog 
categories: [Blog]
image: 
tags: keynan

---

Over the past year I have been trying to teach my 6 year old Python through games. I was using [insert book here]. The book starts with teaching the basics of programming like variables, strings, loops...etc. I found this a bit problematic since these concepts were a bit too abstract for him, and the lack of immediate results didn't help. Great you assigned a number to a variable. Now what? We experimented with Turtle a few times and he really enjoyed changing colors, and doing loops to create interesting shapes. But still the leap from basics to an actual playable game was a bit too big.

Which got me thinking, why not start with basic web design? With HTML/CSS there is almost no logic and the results are immediate. So over the past weekend, I asked Keynan, if he wants to build his own website. He didn't know what a website was. After I explained, he was like 'oh so like an app?' Woe to me.

Anyways we sat down as I explained to him we need a `<header>`, a `footer`, and a `body` using a simple wireframe. He wasn't impressed. Screw all this theoretical BS I thought, and just fired vim and wrote 'Hi Keynan' inside a `<p>` tag and launched the file in the browser. His eyes lit up for a brief second. As if saying 'ok that's nice but not all that impressive'...So I envelope his name in a `strong` then an `em`. Same look.

I had my secret weapon though. Color! That ought to get his attention. I introduce a `style` tag to the document and instruct it to color `p` tags blue. Excitedly I switch to the browser and hit refresh. Nothing. Still boring black. Well that was embarassing. After a few minutes of debugging, I realized I had my syntax wrong (thank you CSS-in-JS, React et al!) back to business.

The intoduction of color was what made it click to him. He said I want the phrase 'Hi Keynan' in an alternating black, white, and pink. I explained to him that white won't work since the background is white. Why don't we do black and pink only? He begrudgingly conceded. I quickly wrapped the colors we wanted pink in `span`s and gave them `.pink` classes. Now I have his full attention.

Adding images was the most interesting part for him. He really enjoys finding wallpapers of his favorite things and cycling the desktop every now and then. So show him to copy and paste images from the wallpaper folder to his project folder and renaming the images to make them easier to type in vim. He then proceeds adding 7 images by copying my first `img` line.

Up to this point I never thought this exercise will go anywhere. But then I thought wouldn't it be cool to actually publish this? So I add a few styles to make a grid out of his images, add borders to the images, and a background to the document. I then create a github account for him, link up the repo to Netlify, and hook up his domain (which I bought 7 years ago). He now has a brand [new website](https://keynantaibah.com).

Over the weekend he showed his website proudly to everybody he met.

