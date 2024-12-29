---
title: "Functional Programming Chronicles"
date: 2024-07-23T19:27:56+01:00
draft: true
tags: ["Programming"]
math: true
showtoc: true
---

The past year I've been dabbling in exploring some other programming languages and paradigms. This post collects some thoughts and learnings along the way. Note that this will not be a tutorial, although I will sprinkle in links to them if you are interested.

## Why
As someone who never had a formal education in computer science (apart from the odd course given in C and Lisp in university), a programming language has mostly been just a tool to implement my thoughts and algorithms and make them compile/run. After starting work as a data scientist, I quickly settled on Python to *get the job done™* for most of my work. Compared to a lot of languages I knew up until then, it was so simple and quick to get something going. It didn't get in my way and allowed me to basically write code in English. It had an abundance of ML-related libraries which meant that for my work it was almost impossible to *not* use it. 

Implicitly (or explicitly) I was told you should write Object-Oriented code as a best practice, so thats what I learned to do, and have happily done for a while (though I never was a big fan of implementing 5 layers of inheritance and factories to do a simple thing). I was vaguely aware of functional programming, and had read a blog post or watched a video about it in the past, but it never stuck, because again, a language/paradigm was just a tool and I needed to *get the job done* and not let this nerd stuff get in the way too much of that.

I can't remember exactly what it was (probably some Youtube videos comparing the implementation of simple algorithms in a few languages), but a few months ago it did strike me how completely different functional code could be to procedural, and oftentimes how *elegant* as well.

I decided there had to be a reason why these computer sciency types were often so excited about functional programming, and with my day-job having less hands-on programming for a while, I was ready to do some coding again. Maybe, next to broadening my horizon, I could even pick up a few tricks to bring back to my Python code. 

## Functional Programming in Haskell
Because my goal was to learn functional programming, and I was warned this could be a bit frustrating for someone with years of Pythonic code etched into their brains, I needed to pick a language that would *force* me to do so. So instead of Python, or Scala, I went for Haskell.

An example snippet: 
```haskell

```


Working through some tutorials like [learn you a Haskell](https://learnyouahaskell.com/) and a [MOOC by the University of Helsinki](https://haskell.mooc.fi/), I started writing some little scripts like a module for a [Fourier-Legendre transformation](https://hal.science/hal-01116888/document), or a tool that can be used to browse pages through the [Gemini protocol](https://geminiprotocol.net/) in your CLI.

To be clear, I am still *horrendous* at Haskell, but I have been able to use it to get a little hands-on experience with some core concepts in functional programming.

Some outcomes so far:
1. **Loops**: At first I really missed being able to use loops and thinking through step-by-step like a recipe book about what my program needed to do. After some adjustment to the functional style (banging my forehead against the closest hard surface and remembering that recursion exists and is pretty cool) it feels more like I'm defining what an outcome should look like, and everything happening at the same time (the implicit time-dimension I had while thinking about code is gone). It's closer to writing mathematics.
2. **Purity**: I found it valuable to explicitly discuss the concept of *pure functions*, which are functions that are deterministic and have no side effects (like touching a database, filesystem, HTTP request, etc) so everytime you run it with the same input, you are *guaranteed* to get the same output. This makes testing pure functions way easier.
3. **Typing**: Another thing I really liked about Haskell is its strong typing system. Gone is my oh so convenient-when-writing duck-typing (yes yes i know about mypy), but in its place is a system that can be used very deliberately to design custom data types, and make sure that operations on them are specifically defined, and functions guaranteed to work only with (or return) a specific type. This system essentially is Haskells alternative to the need to use any OOP.
4. **Monads**: This is the thing everyone dreads learning about in Haskell. And it took me a while as well to connect the category theory explanation to the code examples and its actual usefullness. They are a way to further structure your code, keeping as much of it in the form of pure functions, while having a good way to hande input/output, exceptions, optional datatypes, global state. 



## Array programming

### APL
[APL (Array Programming Language)](https://en.wikipedia.org/wiki/APL_(programming_language)) is admittedly a bit of an odd language. It was developed in the 1960s and still pops up during [code golf](https://en.wikipedia.org/wiki/Code_golf) because it can be so terse. Its main 'thing' is that it mostly uses a set of Unicode symbols instead of the ASCII we all know. Each unicode symbol ia a function, and the only datatype is an array (hence the name). It has influenced many other languages down the road. 

Some example code: 
* The symbol `⍴` is a function taking one input (called *monadic* in APL) that, when applied to a single array, returns the size of it. 
* `+` and `÷` are functions taking 2 arguments (called *dyadic* in APL) and returning the sum and division (no surprise there)
* `/` is a function taking another (dyadic) function on the left, and an array on the right, and [folds](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) (aka *reduces*) the array using the function on the left.

Putting all these together we can make a function calculating the average value of an array `X` in APL as follows:

```APL
(+/X)÷⍴X
```
To read this, note that APL is evaluated right-to-left. `⍴X` is evaluated, but now the dyadic function `÷` requires that its argument (between the parentheses) is evaluated first. `+/X` will sum-reduce aka add up all the numbers in the array `X`. Eventually the division is evaluated.

This 'odd' decision of using glyphs like `⍎⌽⍕⌈*○≡⍬` to represent the 'building blocks' of computation is explained in Kenneth Iversons 1979 Turing award lecture [Notation as a Tool of Thought](https://dl.acm.org/doi/pdf/10.1145/358896.358899). APL was initially invented simply as a notation, and only years later was a programming implementation made. A lot of its proposed benefits comes down to defining good building blocks, and cutting as much 'noise' out as possible. Yes, this means you have to learn how to read a few new symbols, but you did so as well in your mathematics courses, and I hope you recognize the value of using mathematical notation instead of trying to explain each formula and derivation in plain English. Another neat thing that inspired other languages is that each function is defined on arrays of any dimension.

The terse nature of these glyphs means that complex programs which would take many lines of code to implement in most languages are often very brief in APL, see for example an implementation of [Conways Game of Life in APL](https://en.wikipedia.org/wiki/APL_(programming_language)#Game_of_Life):
```APL
life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵}
```

Not very many people use APL anymore, and even though there is a GNU APL version, the most commonly used variant is Dyalog APL, which does offer free licenses for personal/non-commercial use.

It spawned a few related languages, like [J](https://en.wikipedia.org/wiki/J_(programming_language)) (made by the same person, but this time using ASCII digraphs instead of glyphs), [K](https://en.wikipedia.org/wiki/K_(programming_language)), [Q](https://en.wikipedia.org/wiki/Q_(programming_language_from_Kx_Systems)) (which are still used in finance) and recently, [BQN](https://mlochbaum.github.io/BQN/).

### BQN
BQN is a language [made in 2020](https://mlochbaum.github.io/BQN/commentary/history.html) by Marshall Lochbaum, working at Dyalog at the time, that decided to bring APL into the 21st century. The glyphs remained, but it has (among [other things](https://mlochbaum.github.io/BQN/commentary/why.html)) first-class functions, namespaces and new glyph symbols that are easier to remember.

For a quick comparison with APL, here is again the code to calculate the average of an array `X`:
```BQN
(+´÷≠)X
```

### Tacit programming
Another neat thing about these languages is that they enable [tacit programming](https://en.wikipedia.org/wiki/Tacit_programming), which is a style of programming that removes all references to the arguments of functions, instead focussing solely on functions and functions transforming other functions. This is often also referred to as *point-free programming*. See it as functional programming pushed to its extreme.




### Combinators



## Learnings so far

## Links

* [Try Haskell online](https://play.haskell.org/)
* [Try APL online](https://tryapl.org/)
* [Intro to APL](https://xpqz.github.io/learnapl/intro.html)
* [BQN resources](https://mlochbaum.github.io/BQN/index.html)
* [Try BQN online](https://mlochbaum.github.io/BQN/try.html)
* [BQNCrate (searchable code examples)](https://mlochbaum.github.io/bqncrate/)