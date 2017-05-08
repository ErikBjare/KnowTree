KnowTree
========

(Name [undecided](#naming))

For usage of the early prototyping code see `USAGE.md`.

# About

Similar to a [technology tree in video games](https://en.wikipedia.org/wiki/Technology_tree) but for learning stuff in real life. Essentially a dependency graph for learning.

The closest thing to this is, in some sense, Wikipedia. But it's meant to be a reference, [not a directory](https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not#Wikipedia_is_not_a_directory) and [not a textbook](https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not#Wikipedia_is_not_a_manual.2C_guidebook.2C_textbook.2C_or_scientific_journal).

It is essentially a new type of generation [Learning Management System](https://en.wikipedia.org/wiki/Learning_management_system) which is a lot more personal and of personal value.

Perhaps a better analogy would be a fancy digital [learning log](https://en.wikipedia.org/wiki/Learning_log) where everything you've learned it immortalized. This would be used for analysis of what you know (based on what you have learned), what you don't, how you could learn something (links to rated resources) and make a lesson plan to learn anything (by mapping out learing prerequisites). It could also be used for simply keeping track of what you know and what you've learned, a good start. An activity graph would be a powerful tool to motivate the user.


## Examples

**Example 1:** [This article](http://manishearth.github.io/blog/2017/03/04/what-are-sum-product-and-pi-types/) explains sum, product and pi types. It requires knowledge of structs and enums, optionally requires basic set theory. It provides (basic knowledge of)/(intuition to) sum, product and pi types. If a learner wants to learn sum, product and pi types. They would have to have learned structs and enums before. Once they read the article, they could mark sum, product and pi types as learned (or a lighter version such as "basic understanding") in their tree, and even get informed about what "next steps" would be.

**Example 2:** The entirety of Khan Academy could be put in such a learning tree. They already have a [basic one](https://www.khanacademy.org/exercisedashboard) of their own, although quite dated (designwise) and messy.


## Value proposition

 - Planning out what you need to learn in order to reach some goal. (Learning the concepts you want to learn by telling you what you need to learn to get there)
   - If someone wants to learn X, they would be presented with a variety of options to do so. The work of figuring out how and where is just a matter of choosing between the presented options.
 - Keeping track of what you know.
   - Enables a simple way of letting others know what you know. Useful in resumes.
 - The learner would be provided with an overview of what they can do with the thing they want to learn (how to build upon their acquired knowledge).
   - Example: If someone has just learned the basics of programming, they would be shown what they can do/learn with what knowledge.
 - Freedom of learning *what you want* while still learning *what you need*.
   - There is no core curricula, the learner can themselves choose which path they want to take while still getting some indication of which paths are reasonable/practical.


## Naming

Alternative names:

 - TreeLearn
 - LearnerTree
 - Graph-equivalents
   - LearnerGraph
   - LearningGraph (two g's in a row is probably bad)
   - LearniGraph (gets rid of the two g's issue)
 - Tree of Knowledge (or some variation thereof)
   - I've bought the domain names knowledgetree.io and knowtree.io


# Is there something similar?

I've made some basic searches, nothing found. But more extensive searching would be in order.

Update: Turns out [Nikita Voloboev](https://github.com/nikitavoloboev), [who's mindmap repo I've found before](https://github.com/nikitavoloboev/knowledge-map) is "Building a visual search engine and mind maps to organise world's knowledge with a study plan for learning anything" (his GitHub profile description 2017-04-16). Looks like he's taking a different approach, but has likely thought a lot about stuff related to this. I've reached out to him.

Update 2: Nikita gave some really good feedback, will integrate later.

[Arbital](https://arbital.com/) is an example of a wiki with some fresh ideas.

Update 3: Googled around, [found this (Swedish)](https://magisterfalk.wordpress.com/tag/kunskapstrad/) which was interesting. Another datapoint to the claim that there's no such thing as a new idea. I should gather info from that blogger.


# Implementation

It would probably be best implemented as a webapp. Visualization of the graph would likely be best done with D3.

The real question is how to do it in a way that minimizes the complexity of the backend and frontend so that we can iterate quickly.

Perhaps the graph itself could be represented with Neo4j?


## Datastructure

The graph will contain at least three types of nodes:

 - Field of knowledge
   - Mathematics, Physics, Computer Science, etc.
   - Sub-fields would probably be necessary.
   - Essentially serves as categories for more granular pieces of knowledge. Wikipedia already does categorization like this well.
 - Topics/Concepts (goals?)
   - Can belong to one or more fields of knowledge.
   - Essentially what you want to learn.
   - [This PDF](https://worldview.unc.edu/files/2013/07/Getting-the-Big-Idea-Handout.pdf) contains some information about the "concept-topic divide".
   - Nodes of this type have relations to each other.
     - Required prerequisites and recommended/optional prerequisites. 
     - **This is what builds the arguably most important part of the graph.**
 - Learning resources
   - Can supply knowledge about one or more topics/concepts.
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


## Visualization

The [D3.js gallery](https://github.com/d3/d3/wiki/Gallery) has great examples. We could probably get a lot of good ideas from some of them.

Update: I've started attempts at prototyping the structure of such a tree using [Gephi](https://gephi.org/).

Update 2: Gephi wasn't the right tool for the job, yEd was a lot better (but not open source). I found [this neat collapsible tree demo](http://live.yworks.com/yfiles-for-html/2.0/complete/collapse/index.html) on their website, the balloon style was really nice.

# Issues

There might be plenty of things making the idea in need of modification or entirely unfeasible/impractical, those things go here.

 - Looking for feedback currently, expect more here in the future. 
   - **Update:** I've reached out to a handful of friends for feedback, most of it overwhelmingly positive. I've created a [new section for feedback](#feedback).
 - Too simplistic? Can we really reduce knowledge to a tree/graph in a useful way?
 - Knowledge about a topic usually has levels (basic, intermediate, advanced, expert), these would be hard to structure in the graph.
   - We should probably focus on basics/intermediate knowledge first anyway, so might not be that big of an issue initially.
 - Monetization: Is there any good way to monetizing it without sacrificing maximum value provided?
   - Donations work, but have their own problems.
   - Offering a premium service of some sorts?
     - Enterprise?
       - Support for closed ecosystems?
     - Pro users? *(I just went through and s/user/learner'd the whole document, I laughed when I realized this would become Pro learner)*
 - Internationalization
   - Learning resources are usually specific to a certain language, some are translated however. 
   - We'd need to track which languages a resource is available in if we want to scale beyond an english-speaking audience.

# Feedback

The only feedback I've gotten so far has been extremely positive, still looking for more constructive feedback/ways to improve/potential issues.

# Questions

 - Is the tree actually a tree? Might it actually be a graph?
   - It will at least be a directed acyclic graph (I hope, otherwise it'd be messy)
 - Might a tree/graph like this be useful in training/building AI?

