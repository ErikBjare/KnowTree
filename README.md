LearningTree
============

(Name [undecided](#naming))


# Core Idea

Similar to a [technology tree in video games](https://en.wikipedia.org/wiki/Technology_tree) but for learning stuff in real life. 

Useful for:

 - Keeping track of what you know (and, possibly, letting others know what you know. Useful in resumes).
 - Planning out what you need to learn in order to reach some goal. (Learning the concepts you want to learn by telling you what you need to learn to get there)


# Naming

Alternative names (domain names are a bitch):

 - TreeLearn
 - LearnerTree
 - Graph-equivalents
   - LearnerGraph
   - LearningGraph (two g's in a row is probably bad)


# Examples

**Example 1:** [This article](http://manishearth.github.io/blog/2017/03/04/what-are-sum-product-and-pi-types/) explains sum, product and pi types. It requires knowledge of structs and enums, optionally requires basic set theory. It provides (basic knowledge of)/(intuition to) sum, product and pi types. If a learner wants to learn sum, product and pi types. They would have to have learned structs and enums before. Once they read the article, they could mark sum, product and pi types as learned (or a lighter version such as "basic understanding") in their tree, and even get informed about what "next steps" would be.

**Example 2:** The entirety of Khan Academy could be put in such a learning tree.


# Is there something similar?

I haven't made a search yet, I should do that.


# Requirements

### Core

 - Mark topics as `learned` or `want to learn`
 - Concepts

### Extras

 - Voting on learning resources
   - Reddit-style voting
 - Wiki-like editing of the tree (each node a file?)


# Datastructure


## Types of nodes in tree

 - Field of knowledge
   - Mathematics, Physics, Computer Science, etc.
   - Essentially categories for more granular pieces of knowledge, some topics 
 - Topics/Concepts
   - Can belong to one or more fields of knowledge
   - Essentially, what you want to learn
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

### Extras

 - Projects


## Relations between concepts in the tree

 - Required prerequisite
 - Recommended prerequisite


# Questions

 - Is the tree actually a tree? Might it actually be a graph?
   - It will at least be a directed acyclic graph (I hope, otherwise it'd be messy)

