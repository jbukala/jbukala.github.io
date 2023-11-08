---
title: "Geometric Algebra"
date: 2023-11-01T19:57:52+01:00
draft: true
tags: ["Physics", "Math", "Algebra", "Geometric Algebra", "Vector", "Rotor", "Imaginary", "Quaternion"]
math: true
showtoc: true
---

## Geometric Algebra

### The Beauty: Inner Product
Think back for a minute to your first Linear Algebra course: Remember how nice inner products were to compute? Try to think of how to do it from the top of your head. If its a bit blurry: its just taking each component of the vectors, multiplying them and adding all the results: 
$$\mathbf{a \cdot b} = \sum_{i=0}^{N} a_i b_i$$ 
Calculating it gives you a scalar that says something about the angle between the two (it gives you $\cos(\theta)$, scaled by the vector magnitudes). As simple to do in 2D as it is in 687D. 

### The Beast: Outer Product
Now consider outer products in contrast. Do you still remember? *Yeah, neither do I*. Something about each component having the other components multiplied together in 2 different ways, and then subtracting the 2 results from eachother. Oh right, and then it only exists in 3 dimensions (And actually also in 7 dimensions, *what, how*)?! Wikipedia says the formula is:
$$
\mathbf{a \times b} = 
\begin{bmatrix}
           a_2b_3 - a_3b_2 \\
           a_3b_1 - a_1b_3 \\
           a_1b_2 - a_2b_1 \\
         \end{bmatrix}
$$
Now what does the output mean: you get a vector orthogonal to your 2 original ones, with a magnitude that is equal to the surface that is spanned by the paralellogram of the 2 vectors. How does a vector *length* equal some *surface* area in the same space? The units dont even work. Its clear that something is off.

### A Way Out
When you inevitably bring it up its often encouraged to not worry too much about it, its just some math stuff, shut up and learn the formula by heart. For those people plagued for years by these questions, today I present salvation from your vector-related nightmares: **Geometric Algebra** (known in some circles as a *Clifford algebra*).

Geometric Algebra is a simple and small step back from Linear Algebra in terms of abstractness, but gives you a nice and consistent framework where many things just suddenly make *sense*: Outer products and all the questions related to it above here, imaginary numbers, quaternions, rotors.

## Multiplying Vectors
To kick this journey off think about what we can do with vectors in general: we can add them together, we can multiply them with scalars, but we're going to take a look at how to multiply vectors with eachother. Lets take as our axioms for the multiplication the following, where $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ are any vectors, $\mathbf{ab}$ is our vector multiplication result and $\mathbf{a+b}$ is vector addition as usual:
$$
\mathbf{a(bc) = (ab)c} \\
\mathbf{a(b+c) = ab + ac} \\
\mathbf{(a+b)c = ac + bc} \\
\mathbf{aa} = a^2 \in \reals
$$

### n-Vectors
Lets first discuss what objects are living in this space. To give an idea about how you can visualize them, lets draw some pictures (how can you do *geometric* algebra without some pictures after all).

The objects we are interested in are on the same ladder as *scalars* and *vectors* are, we are just adding some extra rungs. Again, think about your first Linear Algebra course: You had *scalars*, which are just numbers with a *magnitude*. This is then contrasted by *vectors*, which can be visualized as an arrow, which now not only has a magnitude (which is the arrow's length) but a direction as well (where is it pointing). Note that it doesnt matter where exactly you draw this vector, arrows with the same direction and length are seen to be *equivalent*. 

![Scalar, Vector](images/BiVectorPicture.png)

This step from 0D point to 1D line practically begs us to keep going: But what would the equivalent 2D look like? The answer is that a 1D line segment becomes a 2D surface/sheet, and the magnitude of this sheet is its *area*. Note that our 1D arrows were pointing a certain way, and thus our sheet should do the same, ergo its a 2D *oriented* flat surface (essentially this means we can assign a top and bottom side to it). We call this object the **bi-vector**

![Scalar, Vector, Bi-Vector](images/BiVectorDrawing.gif)

Much like the 1D vector scenario, it doesnt matter much where you place this object. To go even further: as long as its magnitude (*area*) stays the same and the surfaces' top to points to the same direction, you can even transform the surface however you like.

![Two equivalent Bi-Vectors]()

And we can do the same things with it as we are used to with 1D vectors: multiplying with a scalar just scales the surface by that amount. Where we can lay our 1D arrows end-to-end and draw a line from start to end to add the vectors, we can align a side of each bi-vector, and draw a new bi-vector from start to end to get the sum of two bi-vectors.

![Adding vectors and bi-vectors]()

Much like having a basis $\{e_i\}$ of a 1D vector space, you can take a set of mutually orthonormal surface areas and construct any bi-vector in that space from it by addition and scalar multiplication. 

Hopefully after seeing these things in action, you are convinced that bi-vectors are consistent objects, we can work with them like vectors and the results of that make sense. Of course bi-vectors are also not the end of this ladder we are climbing, we have a general recipe to do this for any dimension (its just that the drawings will get less, uhm, informative). As a last example, 1 rung higher on the ladder we will get an oriented (has an inside and outside) 3D volume, called a **tri-vector**:

![Tri-vector]()

### Interactions between n-Vectors
So far all the mono, bi, tri, $n$-vectors have lived happily in their own world. While a neat continuation of a train of thought, defining them hasnt really added anything to our understanding yet. 

The key to their usefulness come in when we revisit the cross product, but doing it *the proper way*.

### Cross-product revisited
Remember that the inner product gave us some information on how much 2 vectors overlap, helping you measure the angle between them, or projecting one onto the other. The issue is that this inner product gives a limited amount of information on the original vectors: in 3D space, if you know a vector $\mathbf{a}$, an inner product $\mathbf{a \cdot b} \in \reals$, and you are interested in $\mathbf{b}$, there is a whole plane orthogonal to $\mathbf{a}$ in which $\mathbf{b}$ could lie, and this lack of info about the original vector $\mathbf{b}$ gets even worse in higher dimensions.

In 3D the cross-product actually gives us enough information (if we combine it with the inner product) to reconstruct the original vectors. So: can we make something similar to the cross-product in 3D, but *better*? Spoiler: yes we can.

Let us define the *wedge product* $\mathbf{a} \wedge \mathbf{b}$. Remember from the cross-product that we got some measure of the area of the space that was spanned between the two input vectors, and it also gave a direction orthogonal to the them. These are nice things, lets keep them.

The difference is that our wedge product will actually output a bi-vector. It will be the bi-vector with its surface's top pointing orthogonal to the input vectors, and a magnitude equal to the area spanned by the paralellogram of the 2 vectors. The surface will either point up or down depending on which vector is first, such that $\mathbf{a} \wedge \mathbf{b} = -\mathbf{b} \wedge \mathbf{a}$ (a.k.a. it is *anti-commutative*).

![Wedge product on vectors resulting in a bi-vector]()

In this way the wedge product has brought us *up* on the ladder of $n$-vectors. We start to see how the different levels of $n$-vectors begin to interact.

Neat to note here is something about the basis elements of our bi-vector space. Now we have the wedge product we can actually represent the basis-surfaces by wedge products of basis-vectors. if $\{e_i\}$ is a basis of the vector space, and $A_i$ is the basis-surface pointing in the $i$-direction for the bi-vectors, we can build a basis:
$$\{A_i = e_j \wedge e_k|   \forall i \neq j \neq k\}$$
![Building bi-vector bases from vector bases]()

## Defining the geometric product
Now we can finally make a nice workable definition of a geometric product between vectors:
$$
\mathbf{ab} \equiv \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \wedge \mathbf{b}
$$
In this way we combine all the information of both the inner product as well as our wedge product.

### First Observations
Firstly you will note that the inner product produces a scalar and the wedge product an $n$-vector. How can we add them? The answer here is that there actually is no need to, just like how when we represent complex numbers $z = a + bi$, we don't know how to add $a \in \reals$ to $bi \in \Im$.

Thinking about what happens with this product in some simple settings, we can quickly see that if $\mathbf{a}$ and $\mathbf{b}$ are parallel, the area spanned by the input vectors will be 0 and thus it reduces to a simple inner product. If they are orthogonal however, it will be the inner product that equals zero and only the wedge will remain.

To continue and make sense of what the consequences of our definition are, lets clarify something: We already know we can build a basis of higher order $n$-vectors from wedge products of basis vectors. Assuming our basis is orthonormal the geometric product and wedge product are the same, so for the basis of our bi-vector space we can just write $\{ \mathbf{e_ie_j}| i\neq j\}$

We also know that:
1. $\mathbf{e_ie_i} = ||\mathbf{e_i}||^2 = 1$ (because its parallel with itself)
2. $\mathbf{e_ie_j} = -\mathbf{e_je_i} \quad \forall i \neq j$ (because the wedge product is anti-commutative)

## Consequences
With these building blocks in hand, we can just start writing everything in terms of the original basis vectors again, and use the observations on how those basis vectors transform to study what happens.

### Example in 3D:
Lets say we now want to calculate the product of two vectors in 3D. We write the vectors in terms of their components and simply start multiplying out the terms:
$$
(a_1\mathbf{\hat{x}} + a_2\mathbf{\hat{y}} + a_3\mathbf{\hat{z}})(b_1\mathbf{\hat{x}} + b_1\mathbf{\hat{y}} + a_3\mathbf{\hat{z}})
\newline
=
\newline
a_1a_2 \mathbf{\hat{x}\hat{x}} +
a_1b_2 \mathbf{\hat{x}\hat{y}} +
a_1c_2 \mathbf{\hat{x}\hat{z}} +
\newline
b_1a_2 \mathbf{\hat{y}\hat{x}} +
b_1b_2 \mathbf{\hat{y}\hat{y}} +
b_1c_2 \mathbf{\hat{y}\hat{z}} +
\newline
c_1a_2 \mathbf{\hat{z}\hat{x}} +
c_1b_2 \mathbf{\hat{z}\hat{y}} +
c_1c_2 \mathbf{\hat{z}\hat{z}} +
$$

If we now use that $\mathbf{\hat{x}\hat{x}} = \mathbf{\hat{y}\hat{y}} = \mathbf{\hat{z}\hat{z}} = 1$ we can bring those numbers together, and that $\mathbf{\hat{x}\hat{y}} = - \mathbf{\hat{y}\hat{x}}$ etc and bring those terms together too, we end up with the general formula of the geometric product of two vectors in 3D:
$$
\mathbf{ab}  = a_1a_2 +b_1b_2 + c_1c_2 + \newline
(a_1b_2 - b_1a_2)\mathbf{\hat{x}\hat{y}} + (b_1c_2 - c_1b_2)\mathbf{\hat{y}\hat{z}} + (a_1c_2 - c_1a_2)\mathbf{\hat{x}\hat{z}}
$$

## Outcomes

### Imaginary numbers

### Quaternions

### Rotors


## More Info
The above content is an amalgation of the sources below. All of them approach the topic from a different direction. If your interest is piqued, I definitely recommend to watch the first video, as the visualizations are really nice to build an intuition.
* A ~45 min [animated intro video](https://www.youtube.com/watch?v=60z_hpEAtD8) on geometric algebra. The rest of the videos on this channel are also quite good at explaining it further, and applying it in different settings.
* A nice ~50min [intro talk](https://www.youtube.com/watch?v=htYh-Tq7ZBI) by game developer Freya Holmer.
* [GAlgebra](https://galgebra.readthedocs.io/en/latest/galgebra_guide.html), a Symbolic Geometric Algebra/Calculus package for SymPy. Also has a great (more traditionally mathy) introduction to the topic