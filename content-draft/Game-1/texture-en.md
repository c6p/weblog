Title: Texture
Date: 2014-08-06 21:47
Slug: texture
Lang: en

I have created the UV coordinates and textured with the image below. Coordinates sent are shaped as an hexagon, though test texture is oversimplified.

![Kaplama resmi](static/tile.png)

Hexagon tiles are textured randomly.

<div markdown="span" class="video-container">
http://youtu.be/-svtF538OeY
</div>

To be honest I wrote this part on monday, then have spent last two days debugging. First I thought problem is shader, wrote a new one. Or somehow coordinates are not sent to the graphics card and searched h3dutCreateGeometryRes function for errors. But as said error quite possibly is within your code, since these libraries are heavily tested. At last I have convinced myself coordinates are wrong and printed. It was ok. And finally I realized I am checking coordinates within the calculation function, and I am sending a now invalid pointer to a local variable. First use Occam's Razor.
