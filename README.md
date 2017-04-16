LearningTree
============

(Name [undecided](#naming))


# About

Similar to a [technology tree in video games](https://en.wikipedia.org/wiki/Technology_tree) but for learning stuff in real life. Essentially a dependency graph for learning.


## Examples

**Example 1:** [This article](http://manishearth.github.io/blog/2017/03/04/what-are-sum-product-and-pi-types/) explains sum, product and pi types. It requires knowledge of structs and enums, optionally requires basic set theory. It provides (basic knowledge of)/(intuition to) sum, product and pi types. If a learner wants to learn sum, product and pi types. They would have to have learned structs and enums before. Once they read the article, they could mark sum, product and pi types as learned (or a lighter version such as "basic understanding") in their tree, and even get informed about what "next steps" would be.

**Example 2:** The entirety of Khan Academy could be put in such a learning tree.


## Value proposition

 - Planning out what you need to learn in order to reach some goal. (Learning the concepts you want to learn by telling you what you need to learn to get there)
   - If someone wants to learn X, they would be presented with a variety of options to do so. The work of figuring out how and where is just a matter of choosing between the presented options.
 - Keeping track of what you know.
   - Enables a simple way of letting others know what you know. Useful in resumes.
 - The user would be provided with an overview of what they can do with the thing they want to learn (how to build upon their acquired knowledge).
   - Example: If someone has just learned the basics of programming, they would be shown what they can do/learn with what knowledge.
 - Freedom of learning *what you want* while still learning *what you need*.
   - There is no core curricula, the user can themselves choose which path they want to take while still getting some indication of which paths are reasonable.

## Naming

Alternative names (domain names are a bitch):

 - TreeLearn
 - LearnerTree
 - Graph-equivalents
   - LearnerGraph
   - LearningGraph (two g's in a row is probably bad)


# Is there something similar?

I've made some basic searches, nothing found. But more extensive searching would be in order.


# Requirements

### Core

 - User should be able to mark topics as `learned` (possibly on different levels such as basic or advanced) or `want to learn`.
 - The graph will highlight what the user needs to learn in order to learn what they want to in the end.
   - Example: If I want to learn how to build rockets, I should mark the topic/goal "build a rocket" as `want to learn` and subsequently, the graph/tree will highlight what I need to know to get there (ballistic physics, orbital mechanics).
 - The graph should provide learning resources for the topics I want/need to learn.

### Extras

 - Voting on learning resources
   - Reddit-style voting
 - Wiki-like editing of the tree (each node a file?)


# Implementation

It would probably be best implemented as a webapp. Visualization of the graph would likely be best done with D3.

The real question is how to do it in a way that minimizes the complexity of the backend and frontend so that we can iterate quickly.


## Datastructure


### Types of nodes in tree

 - Field of knowledge
   - Mathematics, Physics, Computer Science, etc.
   - Essentially categories for more granular pieces of knowledge, some topics 
 - Topics/Concepts (goals?)
   - Can belong to one or more fields of knowledge.
   - Essentially what you want to learn.
 - Learning resources
   - Can supply knowledge about one or more topics/concepts
   - Examples:
     - Reading materials
       - Articles
       - Books
     - Exercises
       - Khan Academy
     - Courses
       - MOOCs
       - Brick-and-mortar University courses
     - Flashcards?
     - Projects?
       - Could also be learning goals.


### Relations between concepts in the tree

 - Required prerequisite
 - Recommended/optional prerequisite


# Issues

There might be plenty of things making the idea in need of modification or entirely unfeasible/impractical, those things go here.

 - Looking for feedback currently, expect more here in the future.
 - Too simplistic? Can we really reduce knowledge to a tree/graph in a useful way?
 - Monetization: Is there any good way to monetizing it without sacrificing maximum value provided?
   - Donations work, but have their own problems.
   - Offering a premium service of some sorts?
     - Enterprise?
       - Support for closed ecosystems?
     - Pro users?


# Questions

 - Is the tree actually a tree? Might it actually be a graph?
   - It will at least be a directed acyclic graph (I hope, otherwise it'd be messy)
 - Might a tree/graph like this be useful in training AI?

