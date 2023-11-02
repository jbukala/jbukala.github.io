---
title: "Understanding NNs"
date: 2023-11-01T19:54:22+01:00
draft: false
tags: ["Physics", "Math", "Machine Learning", "Artificial Neural Networks", "AI", "Data Science", "Sparsity", "Thermodynamics"]
math: false
---

## Understanding of Neural nets from first-principles: Brain dump

So I was reading my company's IT newsletter the other day where one of the topics was sparse modeling ([discussing this Forbes article](https://www.forbes.com/sites/johnwerner/2023/08/17/sparse-models-the-math-and-a-new-theory-for-ground-breaking-ai/)) and it got me thinking again about some things I was reading the past months, about trying to understand how and why (mainly) Deep Learning works.

### First-principles

In a way, sure we know how it works on the microscopic level of each individual neuron (activation functions, matrix multiplications, gradient descent and all that), and we also often describe it at a high level (where we tend to greatly anthropomorphize it: "the model learned to do *X* because in all its examples it saw this object from the same angle, .."). But there are many questions in between where it seems we never connected the dots, instead relying on empiricism, often crude observations and post-hoc justifications for choices here:
* Which activation function do we choose? 
* How deep do we make our network? Where to place skip connections?
* Convolutional filter size? How wide is each layer? 
* etc. etc.

Each one of these seems be some black magic or fingerspitzengefühl on some level. Interestingly, someone actually did attempt to look at how batch normalization works from a statistical perspective (Check out that absolutely [demonic 95-page paper](https://arxiv.org/abs/1902.08129) of pure statistics though). The papers below go into some more detail on this subject.

### Interesting reading on the topic

1. ["Why is AI hard and Physics simple?"](https://arxiv.org/pdf/2104.00008.pdf) - where they try to advocate for seeing AI from the perspective of a physicist, exploring and using sparsity to make a working theory from a bottom-up approach. They argue that we are in a similar situation now with AI as we were with physics in the 1800's, where we invented working combustion engines but only had formulated thermodynamical laws relying on some simple connections we could observe (between temperature, pressure, volume, all macroscopic descriptors). Not until statistical mechanics (a few decades later) was there a way to fully explain how microscopic phenomena could actually give rise to macroscopic behavior, and show that these thermodynamical laws were just emergent from statistics. This spurred on great further advancements in science in its wake. The parallel here can be made with simple substitutions:
    * Physics &harr; AI
    * "Engine goes boom" &harr; "Adam just works best"
    * Thermodynamics &harr; Current DL understanding
    * Statistical mechanics &harr; First-principles understanding of DL
    * Tech advancements &harr; Who knows. Would be nice to have to have each learning task answer all those questions posed above (by inferring an optimal architecture, optimizer & activation), increasing performance, decreasing energy usage, training models quickly and with more stability, etc.
2. In ["The principles of deep learning theory"](https://deeplearningtheory.com/) mostly the same authors as the previous do exactly that: a statistical bottom-up approach to modelling (fully-connected) neural nets, starting from a limit where each hidden layer is infinitely large (showing that this actually simplifies the model enormously and reduces the neural net to a Gaussian process!), and then backing off from this simplification just a bit to study the case of very wide and/or deep networks. In this framework they derive an optimal layer width/depth ratio for learning & hyperparameter tuning. To show the possibility of this approach for more general networks, they also have a [follow-up paper](https://arxiv.org/abs/2304.02034) doing this for transformer architectures.
3. In the *"Why is AI hard and physics simple"* paper they also refer to a famous 1960s article by Eugene Wigner: ["On the unreasonable effectiveness of mathematics in the natural sciences"](https://web.njit.edu/~akansu/PAPERS/The%20Unreasonable%20Effectiveness%20of%20Mathematics%20(EP%20Wigner).pdf). In the article, Wigner stops and ponders why math works so extremely well in our world in the first place. Or in Wikipedia language: "Wigner observes that a physical theory's mathematical structure often points the way to further advances in that theory and even to empirical predictions". The paper itself is quite legible and brain teasing if you're in the semi-philosophical mood.
4. Random cool slightly older paper: ["The Loss Surfaces of Multilayer Networks"](https://arxiv.org/abs/1412.0233) For some type of Neural Net models (*spin-glass*) they show that the larger the neural network, the more that the value of all local minima converge to that of the global minimum (the loss surface looks sort of like an egg-carton), so that your optimizer has to only find a local minimum in order to be effective (and the larger problem is actually avoiding saddle points, by e.g. using momentum in your optimizer).

### Conclusion

I think we're in quite interesting times regarding this topic: There is a lot of ground to cover but it also feels like progress is fast. Just wanted to mention: The only reason we're in this scenario in the first place is because the 'empirical' approach has been wildly successful, so of course it makes a lot of sense to keep pushing forward on that front as well. Like all science there should be good a balance between theory and experiment.
