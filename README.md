# htmltotext-benchmark

The goal of this repository is to provide a dataset of html-to-text extractions performed by hand across as many languages as possible, along with a benchmarking script to be able to provide a quantitative measure of text extraction quality by major html-to-text converters. 

# Motivation

There are a ton of different html-to-text libraries floating around, but there are only a handful of tests comparing them, none of which look at a wide array of languages. The goal of this repository is to be able to provide a common benchmark for all these libraries. 

# Contributing

To contribute, please download the html file to `benchmarkdata/<iso language code>/html/<unique file name>.html` and put your resulting text in `benchmarkdata/<iso language code>/text/<unique file name>.txt`. 

For the file name, please begin with the type of website (this doesn't have to be one of the ones listed here), followed by the name of the source. After that you can use any naming scheme you want (sequential ids, uuids, sha1sums, slug of the url etc) as long as the html and txt have the **same** name. 

Examples of acceptable naming:
 - `news-tagesschau-coronavirus-grossbritannien-1`
 - `blog-leogao-55ca6286e3e4f4fba5d0448333fa99fc5a404a73`
 - `forum-aialignmentforum-FoiiRDC3EhjHx7ayY`

There is no canonical workflow for downloading/labelling right now, but if you figure one out please make a pull request with the relevant scripts/tools! 

Ideally, we would have a wide variety of different types of websites. Some extractors focus heavily on, say, news articles, which makes them worse at blogs or forums or so on. 
