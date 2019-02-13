# Website Insights


![website_screen_1]

The project has four main components:
+ [**Scrapy**](https://scrapy.org/) crawler to parse websites for data like posts and comments
+ [**NLTK**](http://www.nltk.org/) processing pipeline to extract nouns and adjectives using POS (Part Of Speech) tagger
+ Aggregation in Python using [**Pandas**](https://github.com/pandas-dev/pandas) to generate word frequencies and word co-occurences
+ [**D3**](https://d3js.org/) force simulations to vizualize the co-occurences

The nodes are colored according to part of speech category, their sizes according to the occurrence frequencies. The links between nodes are gradient coloured according to the co-occurrence frequencies.

With this information, you can figure out what topics are being discussed in a website and what are the common context in which the topics are being discussed and also the sentiment surrounding it.

![website_screen_3]

[website_screen_1]: https://raw.githubusercontent.com/rahul-pande/website_insights/master/_screenshots/knowledge_graph.png
[website_screen_3]: https://raw.githubusercontent.com/rahul-pande/website_insights/master/_screenshots/graph_subset_2.png

