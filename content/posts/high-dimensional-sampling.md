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
Again, using the definition of conditional probability to re-write $P(\mathbf{D})$ as an integral over the entire domain of $\theta$.

## Dimensionality of $\theta$
The problem comes in when you want to calculate this last integral in the case where you have a large number of parameters. In other words: $\theta$ is a high-dimensional vector, so its domain is as well. For many of these integrals in general, there is no closed-form solution. 

## Solutions
One angle of approach is to approximate the actual integral with one that is very similar, but simpler to integrate and then solve that one. This is called [variational inference](https://en.wikipedia.org/wiki/Variational_Bayesian_methods), has a rich theorical background with some ways to get bounds for your approximation. This is computationally a quite efficient/fast method for calculating this integral, but it is not guaranteed to asymptotically converge to the correct value.
The other way is to try and draw samples from the probability distribution $P(\mathbf{D} | \theta)$, and asymptotically approximate it using them. The samples can be used not only to calculate this integral, but in fact all expectation values under this distribution.

# High-Dimensional space
To look at the workings of these sampling approaches, it is first interesting to take a closer look at the space in which we're working. High-dimensional spaces have a few peculiarities.

## Volumes
## Typical Set
## Examples

# Approaches

## Uniform sampling
## Rejection Sampling
## Importance sampling
## Gibbs sampling
## Markov-Chain Monte Carlo methods
### Metropolis-Hastings
Approach: Sample a uniform random location. From this location use a reasonable distribution like a Gaussian centered on the current location to geenrate a new proposal point to move towards. If the function at this point has a higher value, move. If not, only move there with probability $p_{\text{accept}} = \frac{f(x_{\text{new}})}{f(x_{\text{old}})}$. Take a sample from this chain every $\epsilon$ steps. Use a few chains to handle multimodal distributions better.

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

