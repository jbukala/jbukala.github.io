---
title: "Fourier Analysis"
date: 2023-11-01T19:49:21+01:00
draft: true
tags: ["Fourier", "Waves", "Spectrum", "Math", "Machine Learning", "Linear Algebra", "Data Science"]
math: true
showtoc: true
---

## Fourier Analysis for DS

*This post is adapted from a presentation I gave to a group of data scientists / analysts / engineers at my client a few months ago.*

People going into Data Science as a profession tend to come from a diverse set of technical backgrounds. The last few years more and more come from specifically Data Science masters programs. Fourier Analysis is a topic that tends to not be discussed in these settings. I think it's still interesting enough to dive into for a bit, both because of its interesting mathematics and because it can give a lot of insight when working with time-series data.

In this post I hope to give you a brief overview of what the topic is all about, explain the mathematics behind it and what you can do with it.

## What is Fourier Theory?

Fourier theory busies itself with trying to view everything as waves. The most straightforward setting of this is periodic signals over time. See the figure below for an example. Here you can imagine observing the top signal, and trying to find a set of sine functions such that, when added to eachother, will result in this function.

![Decomposition of a periodic signal into sine waves](images/sine-wave-decomposition.svg) \
*Fig: How to get from the top (red) signal to its constituent simple sine waves?*

In this example, the red function can be built by $f(x) = \sin(0.01x) + 1.5\sin(0.02(x+100))$. It is not a priori clear that this is easy or even possible, right? After all, the problem of finding the prime decomposition of a huge number is so difficult that most of our cryptography is based around it. Perhaps the decomposition of a general function into sine waves will be similar?

We lucked out here though for reasons I'll go into later. This decomposition is quite fast to calculate and has resulted in more than a few technological applications over the years. So much so that I'm 100% sure you have used it today without realizing it, unless you are reading this post on paper far from human civilization. (In which case: please reach out to me by mail pigeon because I'm very curious how you heard of it.)

### Why sine waves though
At this point maybe you're thinking: What is the big deal around sine waves anyways? If your head is not still in high school geometry class you're probably not spending most of your day using sin/cos/tan to find triangle side lengths etc.

In a nutshell: they are the simplest form of a periodic function that is smooth, differentiable, integrateable. Their first and second derivatives have some nice properties. Each sine wave has one constant *frequency* (the amount of vibrations per second), which allows you to look at functions in terms of their frequencies, which can be very insightful depending on the application. Using sine waves also causes the decomposition process itself to have some nice properties which we can go into later on.

### Fourier Series

### The Fourier Transform

## Mathematical Intuition

## Applications

### Discrete Fourier Transforms

### Fast Fourier Transform

## Follow-up Topics

## Conclusion

## Continue Reading