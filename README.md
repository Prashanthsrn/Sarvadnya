# Sarvadnya (सर्वज्ञ), an All-Knowing Chatbot!!

Chatbots have always been WoW stuff!! The recent evidence is: ChatGPT.

Now that they are more human-like with the latest LLMs (Large Language Models). But these LLMs are Pretrained on their own (HUGE) data. Mere mortals dont have any ways ($$, time, expertise) to train own LLMs.
Some do have facility to get fine-tuned on custom corpus, but limited. This repo explores this further. Wish to build that end-to-end MLOps for fine-tuning LLMs.

Goal: build fine-tuning on LLMs on own corpus:
- corpus can be documents: FAQs, manuals medical papers, etc (many tutorials are available to do this via Vector Databases)
- corpus can be tables, so need SQL/BI conversion from natural language  
- corpus can be graphs: social networks, need conversion to GraphGPT, Cypher

Graphs, actually Knowledge Graphs, would be essential for **Sarvadnya (All-Knowing)** chatbot. LLaamaIndex probably has connectors to all the above mentioned data types.
So, with LangChain as LLM front-end for NLU and NLG, LLaamaIndex can be the data ingestion or back-end db store.

Planning to leverage the combo for open-source stack.


## Rational

No one person can read a million articles comping every day in Pubmed. So is the velocity with legal judgments, research papers in any domain. How to comprehend, at least superficially if not fully,  semantically? At least narrow down, ie filter to get to some core documents for further manual study. Use AI ML in NLP for Information Retrieval and Text Mining techniques. Applications vertically are in many domains but horizontally for Automation for QnA and Hypothesis Generation.

Chatbot would be the front-end for Knowledge Graph for "WoW!!" experience. Chatbot is Turing real AI even if its adding some incremental benefit.

Solution can be domain agnostic, highly portable, for global impact and sustainable forever.

तमसो मा ज्योतिर्गमय : From Dark (hidden in text data) to Light (insights)

Application: Health-care for Sr Citizen via Voice is the next best thing

## Contours
- Given text corpus (any domain: legal cases, medical papers, research articles, etc)
- Build Knowledge Graph with nodes/edges populated using:
	- Linguistic features: POS/NER tags, Topic Models, etc
	- Domain Knowledge: Ontologies, dictionaries
- All thru configurations
- Able to fire queries to find relations, paths between concepts, subgraphs, similarity, anomaly detection, etc.
- LangChain based chatbot as front end or it can be graph visualization tool for RnD kind of queries

## Approaches
- Open source: (LangChain + LLaamaIndex)[https://python.langchain.com/en/latest/index.html] using HuggingFace free models (Open AI models are cheap also), for local, data-secure solution
- Google Cloud: End-yo-end VertexAI MLOps, easy deployment, for enterprise internal solution.


Why LangChain + LLaamaIndex:
- Local (secure), no over-the-net API/web calls
- Open source, Free
- Good integration with Voice Commands would be the next big thing
- Python!!
- Huge support, community, opportunities

KG + LLM: IKIGAI/Sp Know^/Wow!!: 
- World needs: huge corpus, global, domain
- Good at: ML, NLP professional experience
- Love doing: automation, part II
- Paid for: consult, train, passive service

^Specific Knowledge: rare, un-trainable, only through apprenticeship 


## Application: Elderly care
- Elderly can not type at normal chatbot, ie on mobile (WhatsApp) or Web (messenger), they are technologically challenged.
- Need voice command based system. It need not process complex linguistics of literature quality, but a simple, unambiguous, voice command system.
- Single, elderly, living alone is the target persona. Needs daily routine check, medication reminder, ordering necessary items, basic first level medical assistance, do some entertainment, help call doctor/relatives, appointments etc.
- Hindi, vernacular for wider reach, global impact, issue I care and seeing with parents.


`Not looking for Success, but Wonder!!`

## References

### Companies/Groups
- Machine and Language Learning Lab IISc http://malllabiisc.github.io/
- Google Knowledge Vault, LinkedIn Knowledge Graph, Microsoft Concept Graph, Wikidata etc.
- Semantic Web India http://www.semanticwebindia.com/ Enables organizations generate value from Data using AI, Knowledge Discovery
- Cambridge Semantics https://cambridgesemantics.com/
- Kenome https://www.kenome.io/ Partha Talukdar. Helping enterprises make sense of dark data using cutting-edge Machine Learning, NLP, and Knowledge Graphs.
- Tom Mitchell’s lab NELL:  a continuous learning system (Never Ending Language Learning) to read the web.
- Health bots: Babylon, Ada, Sensely.

### Github Repos
- Graph Neural Networks for Natural Language Processing https://github.com/svjan5/GNNs-for-NLP
- Neo4j Protobot: https://github.com/amirharati/neo4j_protobot


<!-- 
## Why me?
- Reasonable popularity due to Sketchnote and talks on ChatGPT or LLMs (Large Language Models)
- Specific Knowledge: Theoretical background of NLP/LLMs due to trainings, plus, professional experience on customizing LLMs on custom data, plus common-sense software solution-ing experience for 2 decades, including engineering industries. Rare-Global-Untrainable-Leverage-Brand.
- IKIGAI: I love, I like, World needs, Can get paid
 -->
 

<!-- ## Contours
- Theme: Automation MicroSaas
- Product: Micro SaaS, auto upgrade, Serverless, scale as you go
- Payment: Pay per use, Passive Income, forever
- Income: Passive, remote fully, global reach
- Working: Solo, remote, no team, no HR issues, salaries
- Input: scraping , docAI(GDE)->KG (neo4j)
- Output: Wow chatbot, APIs, Network effects, more connection, more $$
- Moat/Entry Barrier, IKIGAI, Sp Knowledge
- Give back: Talks, sketchnotes, Tech explanations
- Side outcomes: consultancy, open source contribution -->

## Mode: MicroSaas
- Own (no team), 
- Pay per use, 
- Passive sustainable income, 
- Why: IKIGAI, Specific Knowledge, 

## Checklist: MicroSaas
- Do you have unfair advantage: 
	- Network of founders, influences, for further reach 
	- Audience: folks who want this app and can pay
	- Being early
- Start With a Problem or many problems (don’t tell me your ideas)
- Move from Problems to Solutions, easy, debuggable
- Evaluate Your Solutions
- How is Your Solution Different?
- Talk to Potential Customers
- Start Marketing Before Coding
- Build MVP
- Solves any specific need (pain point) and not anything-and-everything, 
- Is it for specific people, 1000 true (paying) fans, say $30 or $3 a month
- Is it a daily need?

## Technology Stack
- LangChain 
- HuggingFace open/free LLMs,
- UI Web?
- Hosting?
- Code base: Github Sarvadnya for public, have app based private repo
- Google App Engine on GCP (new project, billing on) [ref](https://www.youtube.com/watch?v=03KgXhg-voY)
- Low grade Linux Ubuntu machines are cheap, and may run 24 hrs forever.
- For quick deployment use Streamlit Share


## Publications
- [SaaS LLM](https://medium.com/google-developer-experts/saasgpt-84ba80265d0f)
- [AskAlmanackBot](https://www.linkedin.com/feed/update/urn:li:ugcPost:7049347127029698560/)

## Learning Path
- [LangChain How to and guides](https://www.youtube.com/playlist?list=PL8motc6AQftk1Bs42EW45kwYbyJ4jOdiZ)
- [Building the Future with LLMs, LangChain, & Pinecone](https://www.youtube.com/watch?v=nMniwlGyX-c)
- [LangChain for Gen AI and LLMs - James Briggs](https://www.youtube.com/playlist?list=PLIUOU7oqGTLieV9uTIFMm6_4PXg-hlN6F)
- [Finetuning GPT-3 David Shapiro ~ AI](https://www.youtube.com/playlist?list=PLV3Fr1UUO9bFg3tKw_-6djIhgId1z74JU)
- [Build overpowered AI apps with the OP stack (OpenAI + Pinecone)](https://www.youtube.com/watch?v=-dZrNj2mVHo)
- [Learn about AI Language Models and Reinforcement Learning Kamalraj M M](https://www.youtube.com/playlist?list=PLbzjzOKeYPCpp3NCeQioevM0YpZa5VqcS)
- [GPT-4 & LangChain Tutorial: How to Chat With A 56-Page PDF Document (w/Pinecone)](https://www.youtube.com/watch?v=ih9PBGVVOO4)
- [LangChain - Data Independent](https://www.youtube.com/playlist?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5)

<!-- ## Follow
- [Practical AI by Ramsri](https://www.youtube.com/@PracticalAIbyRamsri) NLP, LLM, GPT, MicroSaaS
- [Dhramesh Shah](https://www.youtube.com/watch?v=fayBEXSKyoI) ChatSpot, ChatUX -->
