---
title: "Knot Theory"
date: 2023-11-13T19:55:59+01:00
draft: true
tags: ["Math", "Theory", "Knots", "Linear Algebra", "Topology", "Group Theory", "Polynomials"]
math: true
showtoc: true
---

## Playing with strings

Knot theory is one of those topics where you start out asking a very simple and natural question, follow a thread (*hehe*), then look around you and realize you're knee-deep in at least 5 fields of math.

The central topic of interest within knot theory is - you guessed it - knots. A **knot** in this context can be thought of as just a piece of string that is attached together at the ends. So if you feel like it, go and grab a piece of string lying around your house, or cut open a rubber band or whatever. It's literally all you need.

Disclaimer: I'm not going to write down any *proofs* in here. I'll just mention that it is proven and then you can go down to the lecture series videos if you are interested in them. Also, I'm just learning to work with Inkscape to draw graphics whenever I can't find them on Wikipedia, so cut me some slack in that department.

The simplest possible knot we can look at is made when we take our piece of string and just tie the ends together so that it makes a clean circle. This is such a simple knot it is barely even a knot, right? This is why it's called the **un-knot**. It's depicted on the left in the figure below:

![The unknot in 2 forms](images/unknot.svg)\
*Fig: The unknot in 2 different forms. The line being invisible for a little bit denotes the fact that it crosses underneath itself there*

But wait a minute - what about the knot on the right? If we would grab that string by the top bit and rotate that around, we would get the unknot again. Because this is possible, we say that they are both the same knot. We are not really interested in those differences that can be removed through actions like these. This means that the unknot can take very [complicated forms](https://en.wikipedia.org/wiki/Unknot#Examples).

But how do we know if a knot is the unknot when all we see is a complicated diagram? Should we simply get a piece of string and try to pull from all directions until we get the unknot back? What if we don't succeed? Does that mean it's not actually the unknot, or that we just didn't try for long enough?

Finding out if two knots are equivalent to eachother is actually the central question of knot theory, and it leads to some interesting places.

As it turns out, there are actually 3 types of way you can handle a knot to make it change it

![First part of the Knot Table](https://upload.wikimedia.org/wikipedia/commons/1/12/Knot_table.svg)\
*Fig: The table of prime knots up to 7 crossings with Alexander-Briggs notation ([Source](https://en.wikipedia.org/wiki/File:Knot_table.svg))*


## References

* A really great [lecture series on knot theory](https://www.youtube.com/watch?v=EBWP1POPc2A&list=PLOROtRhtegr4c1H1JaWN1f6J_q1HdWZOY) by Dr. Bosman at Andrews University. The Youtube video playlist starts with a nice entry level explanation to the central topic, but goes very in depth and the lecturer is excellent.
