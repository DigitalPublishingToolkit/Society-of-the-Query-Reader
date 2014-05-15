##Exploratory Search and Extended Cognition in Health Information Interaction

##Martin Feuz

While researching expert Tetris players, cognitive scientists David
Kirsh and Paul Maglio made the following interesting observation: these
players typically rely on rotating the falling objects to more easily
identify their shape or moving them to the far right to determine and
set up their exact position for high-drops. The researchers name these
moves *epistemic action*, as their interpretation of such actions in the
world is that they improve cognition. ‘Certain cognitive and perceptual
problems are more quickly, easily, and reliably solved by performing
actions in the world than by performing computational actions in the
head alone.’[^1]

What does epistemic action have to do with search interaction, you may
ask? Actually, a lot! Search for information about health, for example, is conducted in high
volumes and affects people’s decision-making processes, so we should
take it seriously. Health search interactions are of an exploratory
nature and different in kind from other searches. Current black-boxed
search engine mechanisms may do more harm than good in these exploratory
search interactions. More profoundly, supporting exploratory health
search interactions effectively requires shifting models of
interactivity and cognitive processes from an information processing
model of mind towards understanding cognition as extending into and
performing through the artifactual and social environment.

###The Context: Health Search and Search Engines

According to Pew Research from June 2009, 57 percent of adults turn to
the internet as a source of health information; for 60 percent,
information found online influenced their decision-making process
regarding treatment options.[^2] By the end of 2010, Pew
reports that ‘searching for health information, an activity that was
once the primary domain of older adults, is now the third most popular
online activity for all internet users 18 and
older’.[^3]

Before we dive into specific ways in which search engines play a
substantial role in health information search, a bit of
contextualization is needed. This context will help illustrate how the
development of search engines and interactions with them in the context
of health information search is problematic.

Search engines have played a vital role since the early days of the web.
This is mainly due to the fact that the web lacks an inherent indexing
and categorizing mechanism. While some organizations have tried to
compile a directory using human experts, this approach quickly runs into
deep problems. On the one hand this method simply can’t cope with the
rapid growth of the web and thus runs the risk of becoming incomplete.
On the other hand the complexity and dynamics of the web lead to
ontological problems with categorizing the information found. Subsequent
search engine providers started to build automated indexing and ranking
mechanisms. The index is the part of a search engine that search
crawlers continuously update by scanning the web for new websites and
new content on those indexed websites. Ranking, on the other hand, is
concerned with matching a user's search query with the index and, based
on a set of rules, presenting the user with a selection of search
results. At the core of ranking lies the trade-off between precision and
recall. Precision is concerned with the accuracy of the match between
search query and retrieved search results, while recall is concerned
with the number of relevant search results produced. When the precision
of the match between search query and results is increased, recall is
reduced and vice versa. We will see that this tension is of ongoing
concern in the development and improvement of search engines.

While better suited to cope with the enormous growth of the web, early
automated search engines nevertheless suffered from a number of
problems. Key among the issues was that their ranking mechanism chiefly
relied on a relatively crude statistical keyword matching process
between search query and indexed webpages. With the growth of content on
the web, this produced enormous amounts of search results (recall). More
often than not, it was a strenuous effort to find useful, relevant
search results.

While the front end of most search engines has not seemed to change much
in recent years,[^4] the back end has changed
substantially. Search results for a given search query are nowadays
automatically filtered by a number of variables that remain hidden from
immediate user interaction. The goal of this filtering is to further
increase the relevancy of search results. Among others, search results
are typically filtered based on the search user’s geo-location derived
from her IP (Internet Protocol) address. Thus, if a user enters
‘restaurant’ as a search query on Google, the search engine assumes that
the user is looking for a restaurant within the city she currently
accesses the internet from. This geographic sensitivity may obviously be
useful in some cases but largely depends on context. However, a more
substantial and unidentifiable change to the ranking mechanism began
some time ago when Google, among others, began personalizing users'
search results, promising to deliver more relevant results to the user
whose query is now contextualized by her search history and other data
previously compiled into a personal profile. In order to produce this
context, vast amounts of personal information need to be collected,
organized, and made actionable. Within the quickly receding limitations
of storage space and computing power, profiles can never be too
comprehensive, detailed, or up-to-date. Google for example, compiles
personal profiles in three dimensions: the knowledge person (what an
individual is interested in, based on search and click-stream
histories), the social person (whom an individual is connected to, via
email, social networks, and other communication tools), and the
embodied person (where an individual is located in physical space and
the states of the body).[^5] Together, these three
profiles promise to provide a detailed, comprehensive, up-to-date
context for each search query with the potential to deliver precise
results that reflect not only the information ‘out-there’, but also the
unique interest a user has at any given moment. Personalized search does
not simply aim to provide a view of existing reality, which is
problematic enough.[^6] Rather, personalized search
promises an ‘augmented reality’ in which machine intelligence interprets
the user’s individual relationship to reality and then selects what’s
good for that relationship. As a result, it has become highly unlikely
that two users see the same search results for a particular search query
even when accessed from the same IP address.[^7]
Unfortunately, many search engine users do not seem to be aware of this
development.[^8]

To fully understand the implications of search personalization, it is
necessary to take a more nuanced focus in light of different types of
search interactions and today’s typical search engine interface. Andrei
Broder suggests differentiating between three types of search
interactions, which, while crude, is a useful taxonomy for our purposes
here.[^9] First, navigational search queries are used
when users want to find the URL for a specific website. Second,
transactional search queries, such as checking flight prices, can be
performed on a number of different but nevertheless specific websites.
Third, informational search queries may find information on multiple
websites and are useful when the search goal may not always be clear at
the beginning but could emerge through the search process itself. Thus,
with this type of search activity, people are typically trying to learn
aspects about a topic of interest and exploring new knowledge domains.
This kind of search could include anything from school or university
research for an essay, to a person thinking of moving into a new
professional domain or learning more about a health issue, as is the
focus of this text. From such a perspective it starts to become clear
that search results personalization, with its self-referential
mechanisms – termed by some an echo chamber[^10] or
filter bubble[^11] ^^– is especially problematic for
informational search queries. This is because it is precisely the user's
intention to move beyond already familiar knowledge and explore novel
terrain. Thus, the analysis and argument I develop will focus on this
type of search interaction.

###Exploratory Search

Recently researchers have developed and characterized the notion of
informational search as ‘exploratory search’,[^12]
which is the term I will use from now on.

>Exploratory search can be used to describe an information-seeking
problem context that is open-ended, persistent, and multi-faceted; and
to describe information-seeking processes that are opportunistic,
iterative, and multi-tactical. In the first sense, exploratory search is
commonly used in scientific discovery, learning, and decision-making
contexts. In the second sense, exploratory tactics are used in all
manner of information seeking and reflect seeker preferences and
experience as much as the goal.[^13]

Exploratory search interactions are characterized by a number of typical
features. To start with, very often there is a complex information
problem at hand and a desire to learn about it. Also, people engaging in
exploratory search may be unfamiliar with the knowledge domain their
search goal relates to, including a lack of understanding of dominant
and peripheral actors within that domain. Furthermore, people may not
have good knowledge about relevant keywords, concepts, and information
sources that might be relevant to formulate search queries and evaluate
search results. Lastly, it is also possible that exploratory searchers
might not have a specific search goal in mind initially. The goal may
only evolve and become clearer through a process of learning about a
specific knowledge domain, its concepts, and actors within it. Given
these characteristics, the exploratory search process typically develops
over the course of multiple sessions, which may last days, weeks, or
months.

###The Interface and Models of Interaction

Many search engine interfaces are typically built on a ‘commonly
accepted’ set of action grammars and handles suggested by the Human
Computer Interaction (HCI) domain.[^14] The action
grammar applied more often than not aims to describe a context-free meta
syntax and thereby suggests universal applicability and usability. In
the case of universal search engines such as Google or Bing, the
interface is typically made of a single search box with a search button
on an otherwise almost empty page. A user enters her search query,
clicks on the search button, and is then presented with the most
relevant search results for that search query. Typically, the user then
has a few general refinement options available to further narrow the
search. What remains hidden are the numerous assumptions at work that
lead to the ranking of the most relevant search results, mentioned
above. This approach arguably works well for simple navigational tasks
in web search. While there have been a number of useful attempts to
change the dominant search interaction paradigm, sadly these ventures
have died after some time. I can only speculate on the reasons why they
weren’t successful, but a key determining factor seems much less related
to the interaction paradigm than to index comprehensiveness, explained
earlier. The computation-intensive processes for approaching
comprehensiveness and accuracy require Google and other popular
universal search engine providers to invest massively in hardware and
human expertise. This appears to be an increasingly high entry barrier
for potential competitors entering the global search engine sector. Danny Hillis, a well-known
supercomputing pioneer and founder of the Long Now Foundation, has
argued in *The New York Times* that ‘Google has constructed the biggest
computer in the world, and it’s a hidden asset’.[^15]

The core of the problem of why today’s search engine interfaces don’t
support exploratory search well lies in both a specific perspective on
the model of interaction as well as the model of cognitive processes
assumed by search interaction designers. Today’s search engine
interfaces can be described as relying on a few core assumptions that
resonate strongly with an information-processing model of the mind.
Cognition is typically represented and described as a purely mental
process consisting of ‘identifying an information need, followed by the
activities of query specification, examination of retrieval results, and
if needed, reformulation of the query, repeating the cycle until a
satisfactory result set is found’.[^16] Alternate
models of the search process, such as Marcia Bates’ berrypicking, have
made very useful contributions to a more interactive style of search by
including iterative aspects of the process, including learning and
shifting focus and goals.

[IMG1]
("Fig. 1. Berrypicking Model (Bates).")

While the model itself seems a bit formal, Bates more recently clarified
her perspective by stating: ‘In my view, our understanding of
information seeking is not complete as long as we exclude the biological
and anthropological from our study.’[^17]
Unfortunately, such an understanding has not yet been adopted by the
information seeking research community.[^18] Further
arguments about why models with a more embodied understanding and style
of interactivity are particularly desirable in the realms of health
search interaction will be developed in the next section.

###Methods and Issues of Evidence-Based Medicine

In order to appreciate why a lack of supporting exploratory types of
search interaction is particularly problematic when searching for health
and medical information, we need to briefly unpack the methods on which
such knowledge is produced and some of the issues this generates.

For the past four decades, Evidence-Based Medicine (EBM) has slowly but
increasingly become dominant as a knowledge paradigm and clinical
practice approach in Western medicine. This paradigm is evident in the
forms of new institutions such as the Cochrane Collaboration and the
National Institute for Clinical Excellence in the U.K., new journals,
recurring editorials in leading medical journals, as well as the
adoption of EBM-methods, such as randomized controlled trials in
mainstream medical research.[^19] Greenhalgh and
Donald define Evidence-Based Medicine as follows:

>The use of mathematical estimates of the risk of benefit and harm,
derived from high-quality research on population samples, to inform
clinical decision-making in the diagnosis, investigation or management
of individual patients.[^20]

This sounds all good and well; however, as research transpires through
the growing body of systematic reviews, the scientific robustness of
medical evidence increasingly reveals some of the problematic
foundations and processes whereby medical knowledge has been and
continues to be generated and distributed. Ben Goldacre, a physician and
EBM researcher, has framed these issues as the ‘broken information
architecture of Medicine’.[^21] This phrase refers to
his analysis, which exposes the fact that there is a fundamental gap in
the publishing of negative trial results.[^22] Put
differently, the structural bias towards publishing mostly positive
trial results leads to an overstatement of the benefits of treatments.
To understand why, it is useful to consider the recent research by John
Ioannidis, a leading meta-analytic medical researcher with an interest
in the quality of medical research. In his study ‘Contradicted and
Initially Stronger Effects in Highly Cited Clinical Research’, he
analyzed actual medical publication patterns and how initial research
findings were only slowly corrected over time.[^23]
For this, he studied 49 of the most important published research
findings that were influential in popularizing treatments, ‘such as the
use of hormone-replacement therapy for menopausal women, vitamin E to
reduce the risk of heart disease, coronary stents to ward off heart
attacks’. What he found was that ‘41% of these findings had been
convincingly shown to be wrong or significantly
exaggerated’.[^24] This problem may be explained to a
large extent by selective reporting of research results and publication
bias. The former is the choice of data that scientists document, whereas
the latter is the ‘tendency of scientists and scientific journals to
prefer positive data over null results’.[^25] While in
some cases this choice merely means an ineffective treatment for some
patients, in others it has grave consequences by actually increasing
morbidity.[^26]

From our previous discussion on search interaction models, it is
becoming evident that such issues in evidence-based medicine may not be
easily identified or explored with either navigational or transactional
search interaction approaches nor with the tools search engines provide
to assess the relevancy of search results and their sources of
authority. This is because these types of search interactions presume
the search user to fully understand the knowledge domain at the outset
and thus to be able to identify relevant information via the mere
listing of search results. Instead, an exploratory model of search
interaction would, for example, support the identification of central
and peripheral actors in a knowledge domain and thus provide
multifarious means of assessing contextual relevancy.

###Cognitive Conceptions of Human Decision-Making

Having briefly reflected on the methods and issues underlying
contemporary evidence-based medicine, I posit that a more open-ended and
exploratory form of health information interaction is strongly
desirable. Desirable on the one hand due to the inherent question of the
kinds of lives that are deemed valuable and desirable to
live,[^27] and on the other hand for allowing more
engaged patient participation. Decision-making, and the ways in which it
can be supported, thus figures as a core element within interactivity.
We can turn to shared decision-making processes[^28] that aim to support exploratory
interaction and decision-making. This approach will also allow us to
illustrate the cognitive assumptions underlying the design of decision
support provisioning, which also informs much contemporary human
computer interaction design.

Shared decision-making processes often make use of different kinds of
decision aids. Typically these are pamphlets that present information
about treatment options for a specific illness in a structured format.
For example the pamphlets incorporate if-then scenarios for when
deciding on a certain treatment option and the probable health
implications, including potential side effects. Where available, such
information is augmented by quantitative probabilities, which aim to
support the decision-making process by trading off the probabilities of
different treatment options along with healing or side effects
prospects.

Decision aids belong to the larger field of decision support systems and
span across academic disciplines such as economics, psychology,
statistics, and computer sciences. A decision support system (DSS) can
be defined as a formal system designed to support the evaluation of
decision alternatives and assess the likely consequences following each
course of action; it thereby aids at arriving at optimal decisions.

Two aspects from the above definition of DSS require attending to: the
‘formal’ and the ‘optimal’, both of which resonate strongly with some of
the earliest work on decision-making in administrative organizations by
Herbert Simon, an economist and highly influential researcher in the
field of decision-making processes. The ‘formal’ is related to the
positivism-oriented style of Simon’s work, focused on ‘scientific
authority by means of reproducibility’. ‘Optimal’, in the spirit of his
book, is to be understood normatively, as he makes clear that his
(developing) theory of administrative behavior is not a ‘description of
how administrators decide so much as a description of how good
administrators decide’.[^29] Coupled with such
normative formalisms are his conceptions of rationality, which in this
context he sees as means-ends chains ‘concerned with the selection of
preferred behavior alternatives in terms of some system of values
whereby the consequences of behavior can be
evaluated’.[^30] He proposes the concept of bounded
rationality: instead of maximizing strategies in light of pre-given sets
of choices, human individual decision-makers follow satisficing
strategies. Characteristic of bounded rationality for him is when
decision-makers employ heuristics, or rules of thumb decisions in the
‘face of the limits of human knowledge and
reasoning’.[^31] For example, one such heuristic that
seems to be readily applied by doctors today is ‘err on the safe side’,
by which is meant, in case of doubt recommend medical intervention. As
the literature suggests, the logic behind this heuristic is mainly a way
to avoid being taken to court in case a patient does fall
ill.[^32] To sustain his arguments for bounded
rationality, Simon points to four decades of progress in psychology
research to describe ‘difficult problem-solving and decision-making in
terms of basic symbol-manipulating processes’[^33] and
also what has come to be called an information processing theory of the
mind.

While Simon aimed to differentiate his view on rational decision-making
from those of game theoretic approaches to strategic decision-making,
his concept of bounded rationality nevertheless remains within very
strong theoretical boundaries concerning cognitive processes. For his
concept of bounded rationality, the environment within which
decision-making takes place, as well as, more importantly, the cognitive
capacities and mechanisms of individuals, introduce significant
constraints that need to be recognized in order to fully understand and
successfully design for decision-making strategies.

Secondly and more fundamentally, bounded rationality operates within the
confines of a cognitive theory that follows an information processing
model of cognition and mind, also known as cognitivism. This model of
cognition assumes that knowledge, understanding, and sensations operate
as clear mental representations upon which cognitive processes then
perform mental changes. Importantly, cognitive processes are
conceptualized as symbolic computations, including semantic meaning.
Cognitivism, as a theoretical framework within psychology, developed as
a reaction to, and yet largely an extension of behaviorism, the dominant
psychological approach for much of the early 20th century. In contrast
to behaviorism, which reduced all thinking to behavior that could in
various ways be conditioned by stimuli, cognitivism holds that thinking
influences behavior and cannot thus be behavior itself. Nevertheless,
cognitivism shares behaviorism's positivist orientation by assuming that
cognition can be fully explained by following the scientific method and
experimentation. Furthermore, typically the brain is conceptualized as a
machine-like device that is the sole and sufficient locus of human
cognition.[^34]

###Rethinking Cognition in Exploratory Healthcare Information Interaction

Crucially, and in contrast to classic cognitive theories discussed
above, from the perspective of the Extended Mind Thesis (EMT) cognition
is not delimited by processes that occur within our skin and skull, but
extends into and operates through the social and artifactual
environment. As evidence suggests such artifactual and social ecologies
play a productive and significant role in cognitive processes, as well
as in human development and evolution more fundamentally. The thesis of
the Extended Mind for Andy Clark and David Chalmers, who first
formulated it, is that ‘when parts of the environment are coupled to the
brain in the right way, they become parts of the
mind’.[^35] At the heart of such considerations, and
in relation to EMT, lies the insight that meaningful interaction with
the world seems to rely profoundly on intentional interactivity
facilitated by various means and channels of perception in action.

I can usefully illustrate the role of the artifactual environment in
cognition for EMT in its simplest form with the example of Tetris
players. Epistemic action from within the cognitive sciences field is an
area relevant to exploratory health search interaction. As Kirsh and
Maglio argue, epistemic actions ‘are actions performed to uncover
information that is hidden or hard to compute mentally’ as
differentiated from pragmatic actions ‘performed to bring one physically
closer to a goal’.[^36] Kirsh and Maglio observed
players of Tetris, an interactive video game for which the player must
arrange objects of various shapes in order to fill in rows at the bottom
of the screen. Whenever a row is fully filled, it disappears and makes
space available. When rows cannot be fully filled, they will build up,
creating less space to maneuver the falling objects. While the objects
fall from the top of the screen, the player can either rotate or move
them from left to right. What Kirsh and Maglio observed was that
‘certain cognitive and perceptual problems are more quickly, easily, and
reliably solved by performing actions in the world than by performing
computational actions in the head alone’.[^37] The
authors’ interpretation of such actions in the world is that they
improve cognition. Exemplary epistemic action, as mentioned in the
beginning, occurred when users turned objects to more easily identify
their shape or moved them to the far right to determine the exact
position for a high drop. From their study, the authors conclude that
standard information processing models of Tetris cognition are unable to
explain many of the actions performed by the players and also make them
seem unmotivated and superfluous. Furthermore, they find that such
'traditional accounts are limited because they regard action as having a
single function: to change the world. By recognizing a second function
of action – an epistemic function – we can explain many of the actions
that a traditional model cannot.’[^38]

Similar types of epistemic action can easily be imagined as useful
interactions in the context of exploratory search – for example, the
ability to explore the sources of authority a given search result entry
enjoys, or its dominance as a search result on a timeline. Such
epistemic actions would provide multifarious means to make sense of
search results and assess their contextual relevancy, or, as Venturini
puts it, to gain a second-degree objectivity.[^39]

The field of behavioral economics has also recognized and come to
exploit opportunistically the ways in which human cognition operates
through and participates in artifactual ecologies. The field has been
popularized by Richard Thaler, an economist and behavioral scientist,
and Cass Sunstein, a legal scholar and behavioral economist, as a
suitable means to address ‘solving’ contemporary social and health
related issues. Interventions following this approach are based on the
idea that the artifactual environment can be designed to ‘nudge’ people
to behave in ways thought to be more beneficial for them than others.
For example, healthy foods could be placed at the beginning of a long
array of food displays in a school canteen rather than at the end. This
tactic, it is believed by proponents of behavioral economics, will make
it more likely that students will choose healthy foods than otherwise.
Such an approach also goes by the term
‘choice-architecture’.[^40] Typically, evidence for
the performance of such an approach is experimental. Indeed, as
Gigerenzer, a psychologist, and Berg, an economist, argue, the evidence
base is rather thin because rather than researching how people actually
make decisions, it only looks at what decisions they make and then
generalizes from such experimental evidence.[^41] From
a more political perspective, one critique is that ‘nudge’ interventions
are seen as ‘liberal paternalism’ because they are designed and imposed
top-down. Due to their nebulous presence, nudge tactics also do not
invite participation, reflection, and thus do not incite learning and
long-term behavioral change.

As this and other diverse research projects have come to suggest and
support,[^42] cognition emerges out of a much more
complex entanglement of internal and external processes, involving
perception, attention, memory, and the material and cultural
environment.[^43] Such a perspective makes clear that
black-boxing parts of the assumptions that underlie the design of
interactions comes at the cost of people's ability to make sense of them
contextually.

The Extended Mind Thesis thus provides an interesting and potentially
productive perspective for rethinking and engaging with the issues
identified above, such as the ways in which search results are filtered,
ranked, and presented in a black-boxed way. Rethinking interactivity in
these areas with EMT in mind reopens problem- and design-spaces and
raises interesting questions about the relationship of action to
cognition in these specific areas, along with how we might approach the
challenge to redesign interfaces that match the potential for the web’s
complexity.[^44]

###References

Bates, Marcia J. ‘Toward an Integrated Model of Information Seeking and
Searching’, *The New Review of Information Behaviour Research* 3 (2002):
1-15.

Broder, Andrei. ‘A Taxonomy of Web Search’, *ACM SIGIR Forum* 36.2
(2002): 3-10.

Castiglione, Chris. 'Matthew Fuller: Search Engine Alternatives',
Institute of Network Cultures, 14 November 2009,
http://networkcultures.org/wpmu/query/2009/11/14/matthew-fuller-search-engine-alternatives/.

Clark, Andy. *Supersizing the Mind: Embodiment, Action, and Cognitive
Extension*, Oxford: Oxford University Press, 2008.

Feuz, Martin, Matthew Fuller and Felix Stalder. ‘Personal Web Searching
in the Age of Semantic Capitalism: Diagnosing the Mechanisms of
Personalisation’, *First Monday* 16.2 (2011).

Fox, Susannah and Sydney Jones. *The Social Life of Health Information*,
Pew Research Center, 2009.

Freedman, David H. ‘Lies, Damned Lies, and Medical Science’, *The
Atlantic*, November 2010,
http://www.theatlantic.com/magazine/archive/2010/11/lies-damned-lies-and-medical-science/8269/.

Goldacre, Ben. ‘The Information Architecture of Medicine is Broken’, 29
February 2012, http://www.youtube.com/watch?v=AK\_EUKJyusg.

\_\_\_\_\_. *Bad Pharma. How Drug Companies Mislead Doctors and Harm
Patients*, London: Fourth Estate Harper Collins, 2012.

Greenhalgh, Trisha. *How to Read a Paper: The Basics of Evidence-Based
Medicine*, Oxford: Blackwell, 2010.

Harford, Tim. ‘Why We Do What We Do‘, *Financial Times*, 28 January
2011,
http://www.ft.com/cms/s/2/76e593a6-28eb-11e0-aa18-00144feab49a.html\#axzz1lAG3KbL5.

Harnish, Robert M. and Denise D. Cummins. *Minds, Brains, and Computers:
A Historical Introduction to the Foundations of Cognitive Science*,
Oxford: Blackwell Publishers, 2000.

Hearst, Marti A.*Search User Interfaces*, Cambridge: Cambridge
University Press, 2009.

Hollan, James, Edwin Hutchins, and David Kirsh. ‘Distributed Cognition:
Toward a New Foundation for Human-Computer Interaction Research’, *ACM
Transactions on Computer-Human Interaction*7.2 (2000): 174-196.

Introna, Lucas and Helen Nissenbaum. ‘Shaping the Web: Why the Politics
of Search Engines Matters’, *The Information Society* 16.3 (2000):
169-180.

Ioannidis, John P. ‘Contradicted and Initially Stronger Effects in
Highly Cited Clinical Research’, *JAMA*, 294.2 (2005): 218-228.

Kirsh, David and Paul Maglio. ‘On Distinguishing Epistemic from
Pragmatic Action’, *Cognitive Science* 18 (1994): 513-549.

Lehrer, Jonah. ‘The Truth Wears Off’, *The New Yorker*, 13 December
2010,
http://www.newyorker.com/reporting/2010/12/13/101213fa\_fact\_lehrer.

Marchionini, Gary and Ryen White. ‘Find What You Need, Understand What
You Find’, *International Journal of Human Computer Interaction* 23.3
(2007): 205-237.

Markoff, John and Saul Hansell. 'Hiding in Plain Sight, Google Seeks
More Power', *New York Times*, 14 June 2006,
http://www.nytimes.com/2006/06/14/technology/14search.html?pagewanted=1&\_r=1.

McPherson, Klim, John E. Wennberg, Ole B. Hovind, and Peter Clifford.
‘Small-Area Variations in the Use of Common Surgical Procedures: An
International Comparison of New England, England, and Norway’, *The New
England journal of medicine* 307.21 (1982): 1310-4.

Noë, Alva. *Out of Our Heads*, New York: Farrar, Straus and Giroux, 2009.

Pan, Bing, Helen Hembrooke, Thorsten Joachims, Lori Lorigo, Gery Gay,
Laura Granka. ‘In Google We Trust: Users’ Decisions on Rank, Position,
and Relevance’, *Journal of Computer Mediated Communication* 12.3
(2007): 801-823.

Pariser, Eli. *The Filter Bubble: What the Internet is Hiding From You*,
London: Penguin UK, 2011.

Pratt, Craig M. and Lemuel A. Moye. ‘The Cardiac Arrhythmia Suppression
Trial: Background, Interim Results and Implications’, *The American
Journal of cCrdiology*, 65.4 (1990): 20-29,
http://circ.ahajournals.org/content/91/1/245.short.

Rogers, Richard. *Digital Methods*, Cambridge: MIT Press, 2013.

Rose, Nikolas. *Politics of Life Itself*, Woodstock: Princeton
University Press, 2006.

Simon, Herbert A. *Administrative Behavior*, New York: Free Press, 1976.

Spink, Amanda and Michael Zimmer. *Web Search: Multidisciplinary
Perspectives*, Berlin: Springer-Verlag, 2010.

Sunstein, Cass. *Echo Chambers: Bush v. Gore, Impeachment, and Beyond*,
Princeton: Princeton University Press, 2001.

Stalder, Felix and Christine Mayer. ‘The Second Index. Search Engines,
Personalization and Surveillance’, in K. Becker and F. Stalder (eds)
*Deep Search: The Politics of Search Beyond Google*, Innsbruck:
Studienverlag, 2009.

Studdert, David M., et al. ‘Defensive Medicine Among High-Risk
Specialist Physicians in a Volatile Malpractice Environment’, *JAMA*,
293.21 (2005): 2609-2617.

Thaler, Richard H. and Cass R. Sunstein. *Nudge: Improving Decisions
about Health, Wealth, and Happiness*, London: Penguin Books, 2009.

Timmermans, Stefan and Marc Berg. *The Gold Standard: The Challenge of
Evidence-Based Medicine and Standardization in Health Care*,
Philadelphia: Temple University Press, 2003.

Venturini, Tommaso. ‘What Is Second-Degree Objectivity and How Could it
Be Represented’
http://www.medialab.sciences-po.fr/publications/Venturini-Second\_Degree\_Objectivity\_draft1.pdf.

White, Ryen W. and Resa A. Roth. ‘Exploratory search: Beyond the
Query-Response Paradigm’, *Synthesis Lectures on Information Concepts,
Retrieval, and Services* 1.1 (2009): 1-98.

Zickuhr, Kathryn.*Generations 2010*, Pew Research Center, 16 December
2010.

###Notes

[^1]: David Kirsh and Paul Maglio, ‘On Distinguishing Epistemic from
    Pragmatic Action’, *Cognitive science* 18 (1994): 513.

[^2]: Susannah Fox and Sydney Jones, *The Social Life of Health
    Information*, Pew Research Center, 11 June 2009.

[^3]: Kathryn Zickuhr,*Generations 2010*, Pew Research Center, 16 December
    2010.

[^4]: Richard Rogers, *Digital Methods*, Cambridge: MIT Press, 2013.

[^5]: Felix Stalder and Christine Mayer, ‘The Second Index. Search
    Engines, Personalization and Surveillance’, in Konrad Becker and
    Felix Stalder (eds) *Deep Search: The Politics of Search Beyond
    Google*, Innsbruck: Studienverlag, 2009.

[^6]: Lucas Introna and Helen Nissenbaum, ‘Shaping the Web: Why the
    Politics of Search Engines Matters’, *The Information Society*16.3
    (2000): 169-180.

[^7]: Martin Feuz, Matthew Fuller and Felix Stalder, ‘Personal Web
    Searching in the Age of Semantic Capitalism: Diagnosing the
    Mechanisms of Personalisation’, *First Monday* 16.2 (2011).

[^8]: Bing Pan, Helene Hembrooke, Thorsten Joachims, Lori Lorigo, Geri
    Gay, Laura Granka, ‘In Google We Trust: Users’ Decisions on Rank,
    Position, and Relevance’, Journal of Computer Mediated Communication
    12.3 (2007): 801-823.

[^9]: Andrei Broder, ‘A Taxonomy of Web Search’, *ACM SIGIR Forum* 36.2
    (2002): 3-10.

[^10]: Cass Sunstein, *Echo Chambers: Bush v. Gore, Impeachment, and
    Beyond*, Princeton: Princeton University Press, 2001.

[^11]: Eli Pariser, *The Filter Bubble: What the Internet is Hiding from
    You*, London: Penguin UK, 2011.

[^12]: Ryen W. White and Resa A. Roth, ‘Exploratory Search: Beyond the
    Query-Response Paradigm’, *Synthesis Lectures on Information
    Concepts, Retrieval, and Services* 1.1 (2009): 1-98.

[^13]: Gary Marchionini and Ryen White, ‘Find What You Need, Understand
    What You Find’, *International Journal of Human Computer
    Interaction* 23.3 (2007): 205-237.

[^14]: Action grammar and handles refer to the standardized styles and
    design metaphors suggested by the professional Human Computer
    Interaction domain.

[^15]: John Markoff and Saul Hansell, 'Hiding in Plain Site, Google Seeks
    More Power', *New York Times*, 14 June 2006,
    http://www.nytimes.com/2006/06/14/technology/14search.html?pagewanted=1&\_r=1.

[^16]: Marti A. Hearst,*Search User Interfaces*, Cambridge: Cambridge
    University Press, 2009.

[^17]: Marcia J. Bates, ‘Toward an Integrated Model of Information Seeking
    and Searching’, *The New Review of Information Behaviour Research* 3
    (2002): 1-15.

[^18]: Amanda Spink and Michael Zimmer, *Web Search: Multidisciplinary
    Perspectives*, Berlin: Springer-Verlag, 2010.

[^19]: Stefan Timmermans and Marc Berg, *The Gold Standard: The Challenge
    of Evidence-Based Medicine and Standardization in Health Care,*
    Philadelphia: Temple University Press, 2003.

[^20]: Trisha Greenhalgh, *How to Read a Paper: The Basics of
    Evidence-Based Medicine*, Oxford: Blackwell, 2010.

[^21]: Ben Goldacre ‘The Information Architecture of Medicine is Broken’,
    29 February 2012, http://www.youtube.com/watch?v=AK\_EUKJyusg.

[^22]: Ben Goldacre, *Bad Pharma. How Drug Companies Mislead Doctors and
    Harm Patients*, London: Fourth Estate Harper Collins, 2012.

[^23]: John P. Ioannidis, ‘Contradicted and Initially Stronger Effects in
    Highly Cited Clinical Research’, *JAMA*, 294.2 (2005): 218-228.

[^24]: David H. Freedman, ‘Lies, Damned Lies, and Medical Science’, *The
    Atlantic*, November 2010,
    http://www.theatlantic.com/magazine/archive/2010/11/lies-damned-lies-and-medical-science/8269/.

[^25]: Jonah Lehrer, ‘The Truth Wears Off’, *The New Yorker*, 13 December
    2010,
    http://www.newyorker.com/reporting/2010/12/13/101213fa\_fact\_lehrer.

[^26]: Craig M. Pratt and Lemuel A. Moye, ‘The Cardiac Arrhythmia
    Suppression Trial: Background, Interim Results and Implications’
    *The American Journal of Cardiology*, 65.4 (1990): 20-29,
    http://circ.ahajournals.org/content/91/1/245.short.

[^27]: Nikolas Rose, *Politics of Life Itself*, Woodstock: Princeton
    University Press, 2006.

[^28]: Klim McPherson, John E. Wennberg, Ole B. Hovind, and Peter Clifford,
    ‘Small-Area Variations in the Use of Common Surgical Procedures: An
    International Comparison of New England, England, and Norway’, *The
    New England Journal of Medicine*, 307.21 (1982): 1310.

[^29]: Herbert A. Simon, *Administrative Behavior*, New York: Free Press,
    1976, p. 73.

[^30]: Simon, *Administrative Behavior*, p. 84.

[^31]: Simon, *Administrative Behavior*, p. 119.

[^32]: Studdert et al., ‘Defensive Medicine Among High-Risk Specialist
    Physicians in a Volatile Malpractice Environment’, *JAMA* 293.21
    (2005): 2609-2617.

[^33]: Simon, *Administrative Behavior*, p. 120.

[^34]: Robert M. Harnish and Denise D. Cummins, *Minds, Brains, and
    Computers: A Historical Introduction to the Foundations of Cognitive
    Science*, Oxford: Blackwell Publishers, 2000.

[^35]: Andy Clark, *Supersizing the Mind: Embodiment, Action, and Cognitive
    Extension*, Oxford: Oxford University Press, 2008.

[^36]: David Kirsh and Paul Maglio, ‘On Distinguishing Epistemic from
    Pragmatic Action’, *Cognitive science* 18 (1994): 513-549.

[^37]: Kirsh and Maglio, ‘On Distinguishing Epistemic from Pragmatic
    Action’: 513.

[^38]: Kirsh and Maglio, ‘On Distinguishing Epistemic from Pragmatic
    Action’: 513.

[^39]: Tommaso Venturini, ‘What is Second-Degree Objectivity and How Could
    It Be Represented’,
    http://www.medialab.sciences-po.fr/publications/Venturini-Second\_Degree\_Objectivity\_draft1.pdf.

[^40]: Richard H. Thaler and Cass R. Sunstein, *Nudge: Improving Decisions
    about Health, Wealth, and Happiness*, London: Penguin Books, 2009.

[^41]: Tim Harford, ‘Why We Do What We Do‘, *Financial Times*, 28 January
    2011.
    http://www.ft.com/cms/s/2/76e593a6-28eb-11e0-aa18-00144feab49a.html\#axzz1lAG3KbL5.

[^42]: Alva Noë, *Out of our Heads*, New York: Farrar, Straus and Giroux,
    2009.

[^43]: James Hollan, Edwin Hutchins, and David Kirsh, ‘Distributed
    Cognition: Toward a New Foundation for Human-Computer Interaction
    Research’, *ACM Transactions on Computer-Human Interaction* 7.2
    (2000): 174-196.

[^44]: See Matthew Fuller's presentation at Society of the Query Conference
    2009. Chris Castiglione, 'Matthew Fuller: Search Engine
    Alternatives', Institute of Network Cultures, 14 November 2009,
    http://networkcultures.org/wpmu/query/2009/11/14/matthew-fuller-search-engine-alternatives/.



