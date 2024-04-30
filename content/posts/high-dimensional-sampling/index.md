---
title: "High-Dimensional Sampling"
date: 2024-03-16T10:00:00+01:00
draft: true
tags: ["Math", "Machine Learning", "Bayesian", "Integral", "MCMC", "Sampling"]
math: true
showtoc: true
---

# Motivations

## Bayesian inference

Bayes' theorem is most often stated as follows:
$$
P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)} \quad \text{where} \quad P(B) \neq 0
$$
Which is very simple to show by multiplying both sides by $P(B)$ and using the definitions of conditional probability.

This theorem holds not only for discrete events but also for probability distributions in general. This fact is then used in a setting where $A$ is the value of some parameters $\theta$ that you would like to estimate given the measured values of some set of data points $\mathbf{D}$. It then looks like this:
$$
P(\theta | \mathbf{D}) = \frac{P(\mathbf{D} | \theta) \cdot P( \theta )}{P(\mathbf{D})} \\[12pt]
= \frac{P(\mathbf{D} | \theta) \cdot P( \theta )}{\int P(\mathbf{D} | \theta) d\theta}
$$
Again, using the definition of conditional probability to re-write $P(\mathbf{D})$ as an integral over the entire domain of $\theta$. So far so good. Now you can put in any prior knowledge you have about your parameters into $P(\theta)$ (or make it a constant function if you have none), and put the core of your model in $P(\mathbf{D} | \theta)$, describing how a model with a specifically selected parameter value $\theta$ will generate data. The last re-write for $P(\mathbf{D})$ in the above formula even saves you from interpreting the almost philosophical question of "what is the probability of my data" by explicitly restricting it only to the model/parameter space you are integrating over.

Note: If you have a limited set of parameter values you are interested in and only care about [comparing their values relative to eachother](https://en.wikipedia.org/wiki/Bayes_factor), the denominator in this equation is simply divided out, so $P(\mathbf{D})$ doesn't have to be calculated at all.

## Dimensionality of $\theta$
The problem comes in when you want to calculate this last integral $\int P(\mathbf{D} | \theta) d\theta$ in the case where you have a large number of parameters. In other words: $\theta$ is a high-dimensional vector. In many situations, there is [no closed-form solution](https://en.wikipedia.org/wiki/Nonelementary_integral). This leaves you with the option of making a numerical approximation.

## Solutions
One angle of approach is to approximate the actual integral with one that is very similar, but simpler to integrate and then solve that one. This is called [variational inference](https://en.wikipedia.org/wiki/Variational_Bayesian_methods), has a rich theorical background with some ways to get bounds for your approximation. It's computationally a quite efficient method for calculating this integral, but it is not guaranteed to asymptotically converge to the correct value.
The other way is to try and draw samples from the probability distribution $P(\mathbf{D} | \theta)$, and asymptotically approximate it using them. The samples can be used not only to calculate this integral, but in fact a very general approach to all expectation values of a quantity $f$ under a probability distribution $\pi$:

$$
\mathbb{E}_{\pi} [ f ] = \int f(x) \pi(x) dx \approx  \frac{1}{N} 
 \sum_{n=1}^{N} f(x_{i})$$

Where $\lbrace x_{i} \rbrace$ is the set of $N$ points sampled from $\pi(x)$. Of course, for this we should be able to evaluate the function $f$ at this set of points, which usually isn't a big deal.  The problem now comes down to drawing samples from a general $\pi(x)$.

# High-Dimensional space
To look at the workings of sampling approaches, it is first interesting to take a closer look at the space in which we're working. High-dimensional spaces have some peculiarities.

## Volumes & Distances

Euclidean distance as a function of dimension:
$$
||\mathbf{x}|| = \large( \sum_{n=1}^{N} x_i \large)^{\frac{1}{2}}
$$

Volume as a function of dimension
generate boxes in center, increase dimension

**Concentration-of-measure**: fight between space exponentially increasing as you go away from origin but prob distribution exponentially dropping: prob mass as a function of origin distance has a maximum somewhere and will tend to zero quickly in high dimensions.

## Typical Set
Small subspace in which most of the probability mass is present.

## Examples

# Approaches

## Uniform sampling
Generating uniformly random numbers is actually a relatively simple case that has been studied for ages in the context of computer science, and for which any self-respecting scripting/programming language will have a standard library implementation. See the [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) for a simple example. For an $N$-dimensional point, simply sample $N$ one-dimensional points and concatenate them into a vector.

Of course, this only works when $\pi(x)$ is a constant. Not the most generic case. However we will see that this is a major building block for the rest of the approaches.

As a side-note, there are some specific probability distributions we can sample by simply transforming uniform random numbers $z \in [0,1]$, like scaling and shifting to get a uniform number $y = (z+a)(b-a) \in [a,b]$, or using the [Box-Muller transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform) to sample from a Gaussian.

## Rejection Sampling
Armed with uniform samples, and a reasonable idea for what the maximum of the function $f_{max}$ is you want to integrate, rejection sampling is a method that generates a lot of uniform random sample proposals $\mathbf{z}_i$, and for each of these of these generates another uniform random number $a_i \in [0, f_{max}]$. If $a_i < f(\mathbf{z}_i)$, the point is added to the set of samples $\lbrace x_i \rbrace$. If not, it is instead discarded. The method is fairly simple when looking at it visually:

![Example of rejection sampling on a one-dimensional function](https://www.jarad.me/figs/2013-10-03-rejection-sampling/unnamed-chunk-4-1.png) \
*Fig: Example of rejection sampling. Many points are generated in this 2D box, but only the blue ones below the function (black line) are kept. The red ones are discarded. ([source](https://www.jarad.me/teaching/2013/10/03/rejection-sampling))* 

I won't give proof here that the sampled points come from the function $\pi(x)$, but it should be intuitively clear that many points $x_i$ are generated where the function is high, and very little points where the function is small, that this scales linearly with the function value.

Okay, so this solves our problem, right? Sample from the function using this method, and approximate any integral or expectation value of this probability distribution! Unfortunately, there are a few drawbacks to this method. Firstly, you should have a good idea of the function maximum, and err towards a larger number to keep its statistical validity intact. Secondly, the method can be very inefficient, as all of the points you reject are essentially just wasted effort. Already in the image above you can see a lot more red points than blue ones, and this is just for a one-dimensional function with a tight bound on $f_{max}$.

Taking into account what we now know about the typical set and concentration of measure in high dimensions, this approach seems almost hilariously wasteful. Practically all of the points will be rejected, so in our high-dimensional setting it's mostly good for generating extra CO2 with your computer..

## Importance sampling
A more scalable approach is [importance sampling](https://en.wikipedia.org/wiki/Importance_sampling). This method actually takes into account the information you have about the function you're trying to sample from. What you do with this method is sample from a probability distribution that is similar, but much simpler. Think for example of using a Gaussian distribution as an approximation, where we have methods of cheaply sampling from it.

![Example of importance sampling](images/importance_sampling.PNG) \
*Fig: Example of importance sampling. The distribution $p(z)$ is approximated by the simpler $q(z)$.([source](https://cedar.buffalo.edu/~srihari/CSE676/17.2%20Importance%20Sampling.pdf))* 

Of course, doing this in a naive manner would give you the wrong result! We need some way of correcting the samples from $q$ to make them statistically come from $p$ instead. Luckily there is a simple way of doing this, simply weigh each sample $\mathbf{x_i}$ by a factor $w_i = \frac{p(\mathbf{x_i})}{q(\mathbf{x_i})}$, making the sample more important if $p$ is larger than $q$ at that point, and vice versa. The (simple) proof for this can be found in the source pdf of the image.

## Gibbs sampling
## Markov-Chain Monte Carlo methods
### Metropolis-Hastings
Approach: Sample a uniform random location. From this location use a reasonable distribution like a Gaussian centered on the current location to generate a new proposal point to move towards. If the function at this point has a higher value, move. If not, only move there with probability $p_{\text{accept}} = \frac{f(x_{\text{new}})}{f(x_{\text{old}})}$. Take a sample from this chain every $\epsilon$ steps. Use a few chains to handle multimodal distributions better.

Advantage: Simple to implement as well as conceptually. Will converge to right result.
Disadvantage: in high-dim many proposals will fall outside of the typical set. Proposals are sort of 'blind' to the actual function, so many need to be generated until one gets accepted. The first steps of each chain will have to be discarded to give it time to converge to the target distribution (so-called burn-in steps).

### Hamiltonian Monte Carlo
In a sampled point, simulate particle dynamics by giving a random momentum to your point and letting it follow the curves of the posterior. After a while take a sample and set new random velocity. In this way it should follow the typical set quite nicely.
advantages: Proposals made on basis of posterior shape. Much more efficient
### No U-Turn Sampler
HMC method that recognizes when particle dynamics result in taking a U-Turn. At this point, stop simulating dynamics and generate new velocity. (TBD: check)
Advantages: Even more efficient than HMC in general.
# Software

## STAN
## PyMC

## Example implementations
### Tuning parameters
### Timing

# Conclusion
When to pick which approach:
* VI for large datasets, very high dimension (faster, less accurate)
* MCMC for smaller ones, the need for optimal fit and accuracy (slower, more accurate). Go for MH in lower dimensions perhaps, NUTS in general

# Further Reading
* [An introduction to Variational Inference](https://arxiv.org/abs/2108.13083) if you want to know more about this approach.
* [A conceptual introduction to Hamiltonian Monte Carlo](https://arxiv.org/abs/1701.02434). Beware: 60 pages although not too dense to read. Covers a lot of the topics above from a theoretical standpoint.
* Get going with [PyMC](https://www.pymc.io/welcome.html). The beginner guides are quite good to get started with bayesian modeling from a practical perspective.
* Great [visualizations with explanations](https://arogozhnikov.github.io/2016/12/19/markov_chain_monte_carlo.html) on Metropolis-Hastings and Hamiltonian Monte Carlo
* More methods for generating random samples from [specific probability distributions](https://en.wikipedia.org/wiki/Non-uniform_random_variate_generation)
