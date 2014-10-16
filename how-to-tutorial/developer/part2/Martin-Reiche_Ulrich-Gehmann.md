---
title: "Towards an Anthropology of Location-Based Recommendation and Search"
author: [Martin Reiche, Ulrich Gehmann]
---

With the increase and advance of software for mobile devices, the
paradigm of *relevance* for the user has experienced a major shift.
Functionality that was earlier heavily bound to software on stand-alone
machines such as mainframes is now available for citizens with
sufficient spare change wherever they are located in the world. Cell
phones have advanced to smart phones and so increased in complexity,
computational power, and practicability. However, an even more important
change has taken place: computers are no longer bound to a specific
place, but rather can be easily carried in a person’s pocket and are
therefore as mobile as their owner. This new mobile freedom and
independence is of course also applicable to the software on the
phone,[^1] which by now enables the user to use the
phone in almost any way that a software developer envisions and that
hardware allows.

Thus, software itself has become mobile, and this new mobility leads
inarguably to a paradigm shift: through the hardware of the mobile
device, software becomes aware of its own mobility and can leverage the
new kinds of information it acquires: location, acceleration, proximity
to other devices,[^2] and access to local infrastructure
through Wi-Fi. These new parameters address the user’s notion of space,
place, and relevance drastically, as these terms now have to be defined
not only through the eyes of the user, but also through the ‘eyes’ of
the software. The software can no longer be seen as independent from the
user but is intertwined with some of his properties in physical space.
This paradigm shift will be the focus of this article.

##Relevance

We all have a deep understanding of what is relevant for us in our life.
Although understanding what is relevant might be very subjective, the
idea that some things are more relevant than others is part of our
cultural heritage. When it comes to breaking down a definition of
relevance though, we can argue with the *conditio humana*: the basic
notion of the human being, i.e. what makes us human after all. If we
accept that relevance is what serves this basic notion of the *conditio
humana*, then relevance is subjective. If relevance is subjective from
the very start of its definition, we have to question whether a
definition of relevance that has its roots in computer science and
mathematics – domains that are precise and, as an effect, computable –
is an adequate definition of relevance for a human being.

At this point, there are two aspects of general importance pertaining to
discussions of the *conditio humana*. Even if it is true that the human
condition embodies a subjective concept, there are conditions that serve
as a framework within which these subjectivities remain embedded. First
of all, it was a specific sociocultural and economic context that gave
rise to an unprecedented use of technology, and, in its wake, our
dependence on technological devices to such a degree that our very
conceptions of the self (and hence of the human condition) became
strongly influenced by it. First of all, our daily life worlds became
technologized to such a degree that living without technology turns out
to be almost impossible. To provide an example, at the onset of a third
wave of modernization shortly after World War II, Schelsky notes our
increasing dependence on ‘automatization’ (as he terms it), with
respective social consequences.[^3]

This dependence was the case long before the arrival of the internet.
The technological condition became an intrinsic part of the human
condition; this effect shouldn’t be forgotten when discussing its
continuous accelerations manifested in the paradigm shift toward mobile
devices mentioned in the beginning. We have been technologically
determined for a long while (as Schelsky wrote in 1957), and in such an
overall environment, which has been characterized as a *technogene*
space,[^4] we encounter not only new paradigms but also
ontologies. Seen against the background of a continuous generation of
non-places[^5] associated with that technogene space,
that paradigm shift – or more precisely, the ontology it announces –
perfectly fits with a scenario of generating a literal utopia (that is,
a non-place).

Second, when considering possible determinants of the present human
condition, we should look back at the long history of discussions
occurring under the aegis of technology-driven modernity. Any discussion
about a new ontological status (expressed in the paradigm shift) must
consider all the past shocks related to the *conditio humana*, from 19th
century metropolization onwards to the present
state.[^6] We must consider these shocks in order to
take a broader perspective of the phenomena discussed as they deserve,
and for them to be understood at all.

##Location-Based Recommendation and Search
Location-based recommendation is a concept from mathematics and computer
science that has made a great impact on our experience of the web,
especially in the last decade. Almost every online shop offers some sort
of recommendation to its users: either they recommend products based on
what they learn about the user's previous interests or based on what
other users have bought independently of each other. Sometimes
recommendations appear completely random to outsiders. Location-based
recommendation can formally be seen as a mathematical function that puts
an entity in space in relation to other entities in (the same or
another) space by utilizing a common space called *feature space.*
[^7] Thus, in order to compute relations, the entities
are processed and reduced to *features* that resemble the entity. It
must be clear that this reduction is intentionally done by the designer
of the recommender system and that the designer’s beliefs about *what
makes an entity to be the entity it is* might be highly subjective.
Taking into account that every next step of the recommendation is first
and foremost based on this reductive step, it is obvious that the
designer’s subjective beliefs about the world are subsequently affecting
every user of the system.

Like the *conditio humana*, the problem of reduction has a long modern
history as well, one aligned with the dominance of technogene spaces
addressed earlier. A space generated by technology has to be reductive
*eo ipso* since the essence of the technical approach to reality is to
functionalize things. The question ‘what makes an entity to be the
entity it is’ has to be interpreted in these terms, too, because we are
discussing functionalities. And functionality *is* reductive, otherwise
it wouldn’t work. Based on these fundamental relations that cannot be
overcome, a functionalized entity is a reduced entity, and the feature
space that is made of functionalized entities is reductive, too, by
necessity.

With regards to *relevance*, an additional aspect comes into play. For
functionalized features, only functions are relevant at the proverbial
end of the day, whether technical functions enabling performance and the
use of apps (a point to come), economic functions sustaining the
technical ones, or last but not least, social ‘functions’ as the result
of all of this, since social functions are one of the main
*applications* of the former. So, the relevant world becomes the world
of the functional, that is, the world of functions.

By reducing the world to features, location-based recommendation
algorithms calculate the relevance of every entity in relation to
another entity. This other entity does not have to be of the same kind
as the entity that will be recommended; it might just be the location of
the user, that is a recommendation could respond to the relation of the
user’s current location to a set of night clubs (based on proximity) as
well as a night club’s relation to other night clubs (based on e.g.
music genre and proximity). Note that this notion of location-based
recommendation already includes the concept of location-based search.
While search delivers information to its user based on a query and thus
can be seen as a reactive way to present information (‘search results’),
recommendation provides results without requiring the user to execute a
concrete query. The effects of search and recommendation for the user,
though, remain the same, which is why in the course of this article we
will use these two terms synonymously. In the case of location-based
recommendation algorithms, we will from now on assume that the user’s
proximity to the recommended entities plays an important role in the
calculation process of the recommendation.

Besides the problem that already emerges from processes of reduction, a
problem occurs in the calculation of the results. At this stage all
entities are already reduced to a set of features, and the calculation
involves the computation of distance between these feature sets. While
there is extensive literature on metrics that can be used in order to
compute these distances,[^8] modern recommender systems
usually try to learn users’ habits and interests, then apply this
knowledge to the recommendation process by using *weighted metrics*.
These weighted metrics deploy different factors of influence for each
feature in the calculation process in order to resemble the information
the system has already learned about the user.[^9]

Finally, the results of the recommendation might consist of entities
nearby, entities that match the user’s interests to a high degree, as
well as entities that increase the chance of serendipity as they are
drawn from a number of other entities, and the system is not sure
whether they are of interest to the user or not.[^10]
These results all have in common that their relevance to the user has
been mathematically calculated, and that this calculation has followed a
model of the world that has been created by people who might have
different beliefs about the world than the user. This means that all
recommender systems not only resemble the user’s spatial properties or
interests but also the designer’s very own notion of relevance on all
the levels of calculation.

##The World as a Set of Apps and the New Spatiality

Taking into account the perspective of a smart phone user, we should
think over a few more problems arising from the conception of relevance
that are deeply intertwined with the idea of the *app*. The basic idea
of an app is to encapsulate one functionality into a single piece of
software and to distribute this software worldwide. This concept
concentrates the efforts of a single piece of software into the
optimization of its functionality, eventually reaching the point where
the piece of software becomes the de facto standard for the solution to
a specific problem.[^11] This single task’s degree of
perfection is one of the key benefits of the app and a big reason for
its success story.[^12]

However, providing one functionality per software piece also produces a
variety of problems. First of all, basic functionalities such as textual
communication are duplicated over a multitude of apps; the average smart
phone today has at least one app for standard text, one for Facebook
messages, and one for Twitter, not to mention the number of apps for
taking pictures or writing notes. All these apps have their rightful
purpose as they offer a certain approach towards one functionality and
therefore might serve a user better than an app with the same
functionality but a different approach. This in itself is not yet a
problem, but it starts to become a problem (for example for
communication) when the existing systems cannot communicate with each
other, or users cannot communicate across these platforms. You can refer
to this problem as the *lock-in effect.* [^13] Ultimately it forces users to work with a variety of apps that all
provide the same functionality, thus effectively undermining the whole
idea of the app.

The information that can be used to make a recommendation must be
gathered by the apps themselves, which means that every app can only
supply recommendations on the basis of its own investigations about the
user, and this significantly affects the quality of the recommendation.
If the recommendation calculation itself can only be done on the basis
of the information gathered by the single app, then important
information might be missing when recommending entities. Even more,
self-learning recommender systems will learn only a small subset of the
variety of the user’s interests (as they can only learn interests that
have to do with the functionality of the app itself) and therefore will
optimize their algorithms in a direction that no longer fully resembles
the user’s interests, so that the relevance of the recommended entities
decreases.

At the same time, the relevance of the recommended entities of each app
increases in the mathematical model of the app (which simply results in
the app optimizing its recommendations based on a model and the learned
characteristics and interests of the user). What then happens is that
each app develops its own optimized model of the world and offers this
view to the user, and the world gets functionally segmented based on the
optimizations of each app on the phone. Instead of showing the user the
relevant world, smart phone apps show the user a world that is optimized
based on her location and interests for each specific functionality,
each represented by a different app. The user becomes the inhabitant of
a functionally segmented environment, meaning that the relevant world
around the user cannot be modeled based on the concept of the
app.[^14]

If you turn from the single app and allow data acquired from functions
of different apps to merge into one single user profile, as with a
Google or Amazon account, then the recommendation quality may increase
again as the functional segmentation might not take place in such a
drastic way. However, new problems arise regarding a major concern with
all recommender systems: in order to work the way they are supposed to,
recommender systems create profiles from an extensive collection of data
acquired from users’ behavioral patterns, leading to very understandable
privacy concerns. In essence, to get rid of the problems of functional
segmentation, user profiles must be created that are shared among
several (not necessarily all) apps, giving away this potentially
valuable data to the third party that is maintaining the profile. In
order to avoid the functional segmentation, we have to give our data
away.

##New Spatial Relevance

One can still argue that the models of the world that are generated by
smart phones and apps are not intrinsically affecting the world of the
user, but as we have shown in earlier
publications,[^15] there is reasonable suspicion that
this functional segmentation, as well as the system designer’s beliefs
about the world, influence the users’ notion of relevance and also the
users’ behavior. In addition, there is an economic reason why the apps
work in such a way: the recommendation creates *a personalized
experience* that might greatly differ from your experience without the
app (unwanted people can be blocked, conflicting thoughts can get
filtered out, etc.[^16]) and that thus gives you a
more enjoyable user experience, resulting in an increase in the usage of
specific apps and lowering the inhibition threshold to pay for extra
services or advanced versions of the software itself.

Optimization of different functionalities through apps thus creates a
new spatial relevance. The idea that the sum of the apps on a mobile
device describes your world (at least the one reachable through the
device) to a certain extent simply stems from the experience that these
apps are being developed for almost all functionalities in life that can
be converted into an app (be it sport, gaming, dating, communication, or
work). It therefore is important to address the problems of relevance in
this anthropological context.

##Conclusion

Mobile devices show us a world that is highly optimized for every
function that is transferable to the concept of an app. We have outlined
how apps are able to optimize their functionality through recommendation
by learning about the user’s interests and characteristics, and we have
shown how this leads to a paradigm shift in the notion of (spatial)
relevance. *Relevant for the user* becomes an algorithmic mixture of the
subjective world view of the system designer, the user’s interests that
have been learned by the app, as well as the lack of information that
results from the encapsulation of functionality in each app. This new
notion of relevance simultaneously becomes a new viewpoint of the world
due to the duty of the mobile device to become our personal assistant
and our gateway to parts of the world that are not immediately
accessible to us. At the same time, the personalized experience that the
mobile device is offering us is compelling, which makes it easy for us
to sell away our very own notion of relevance for the notion(s) of
relevance created by the apps on the devices – and these foremost
address a notion of relevance based on the pragmatic idea of increased
user interaction resulting in more sales.

##References {..references}

Augé, Marc. *Non-Places: Introduction to an Anthropology of
Supermodernity*, London/New York: Verso, 1995.

Deza, Eleza and Michelle Marie Deza. *Encyclopedia of Distances*,
Heidelberg: Springer, 2009.

Gehmann, Ulrich and Martin Reiche. ‘Virtual Urbanity’, Hybrid City II
Conference, Athens, 2013, in press.

Oetzel, Günther. ‘On Technotopian Spaces’, in: Ulrich Gehmann (ed)
Virtuelle und ideale Welten [Virtual and Ideal Worlds], Karlsruhe: KIT
Publishing, 2012.

Liebowitz, S.J. and Stephen E. Margolis. ‘Path Dependence, Lock-in and
History’, *Journal of Law, Economics, and Organization* ****11 (1995):
205-226.

Reiche, Martin and Ulrich Gehmann. ‘How Virtual Spaces Re-Render the
Perception of Reality Through Playful Augmentation’, in Proceedings of
ACM International Conference on Cyberworlds, Darmstadt, 2012.

Schelsky, Helmut. ‘About the Social Consequences of Automatization’,
*Auf der Suche nach Wirklichkeit* [On the Search for Reality], 1979,
Munich, Goldmann.

Weisberg, Jacob. ‘Bubble Trouble, Is Web Personalization Turning Us Into
Solipsistic Twits?’ Slate, 10**June 2011,
http://www.slate.com/articles/news\_and\_politics/the\_big\_idea/2011/06/bubble\_trouble.html.

##Notes {.notes}

[^1]: Of course not completely independent of location, as smart phones
    still need access to power supply regularly and wireless
    connectivity for many of its main functions to work.

[^2]: E.g. through GPS, accelerometers, and near-field communication
    sensors.

[^3]: Helmut Schelsky, ‘About the Social Consequences of Automatization’,
    *Auf der Suche nach Wirklichkeit* [On the Search for Reality], 1979,
    Munich: Goldmann, 1979, pp. 118-147.

[^4]: Günther Oetzel, ‘On Technotopian Spaces’, in Ulrich Gehmann (ed.)
    *Virtuelle und ideale Welten* [Virtual and Ideal Worlds], Karlsruhe:
    KIT Publishing, 2012, pp. 65-83 (73-76 on the technogene space in
    particular).

[^5]: Marc Augé, *Non-Places: Introduction to an Anthropology of
    Supermodernity*, London/New York: Verso, 1995.

[^6]: See for instance Helmuth Plessner, *Conditio Humana*,
    Frankfurt: Suhrkamp, 2003.

[^7]: A feature space is an abstract space whose dimensions are properties
    of the entities. How the dimensions are chosen and what the
    dimensions resemble is highly dependent on the entities themselves.
    A text document for example could have the number of occurrences of
    words as dimensions, while a car could have the dimensions make,
    model, color, gearing, etc.

[^8]: Eleza Deza and Michelle Marie Deza, *Encyclopedia of Distances*,
    Heidelberg: Springer, 2009, p. 3f.

[^9]: For example if the user is in close physical proximity to some of
    the best techno night clubs in town but the system has learned that
    the user anticipates other genres, it might reflect this information
    when computing the recommendations, maybe resulting in some very
    close techno night clubs nearby as well as other clubs further away
    that better resemble the user’s interests. That way, spatial as well
    as learned information have been taken into account in the
    computational process of the recommender system.

[^10]: And by this, the system is able to learn more about the user as it
    can extract information about the behavior towards these unforeseen
    results.

[^11]: As is Facebook for the wider social network of many of its users.

[^12]: At this time, we see a multitude of app stores from many different
    companies and service providers, such as Apple, Google, Amazon,
    Intel, and much more.

[^13]: S.J. Liebowitz and Stephen E. Margolis, ‘Path Dependence, Lock-in
    and History’, *Journal of Law, Economics, and Organization* 11
    (1995): 205-226.

[^14]: Ulrich Gehmann and Martin Reiche, ‘Virtual Urbanity’, Hybrid City II
    Conference, Athens, 2013.

[^15]: Martin Reiche and Ulrich Gehmann, ‘How Virtual Spaces Re-Render the
    Perception of Reality Through Playful Augmentation’, in Proceedings
    of ACM International Conference on Cyberworlds, Darmstadt, 2012.

[^16]: Jacob Weisberg, 'Bubble Trouble, Is Web Personalization Turning Us
    Into Solipsistic Twits?’, Slate, 10 June 2011,
    http://www.slate.com/articles/news\_and\_politics/the\_big\_idea/2011/06/bubble\_trouble.html.



