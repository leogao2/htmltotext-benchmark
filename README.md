# htmltotext-benchmark

The goal of this repository is to provide a dataset of html-to-text extractions performed by hand across as many languages as possible, along with a benchmarking script to be able to provide a quantitative measure of text extraction quality by major html-to-text converters. 

# Motivation

There are a ton of different html-to-text libraries floating around, but there are only a handful of tests comparing them, none of which look at a wide array of languages. The goal of this repository is to be able to provide a common benchmark for all these libraries. 

# Contributing

To contribute, please download the html file to `benchmarkdata/<iso language code>/html/<any unique file name>.html` and put your resulting text in `benchmarkdata/<iso language code>/text/<any unique file name>.txt`. You can use any naming scheme you want (sequential ids, uuids, sha1sums, etc) as long as the html and txt have the **same** name. 

There is no canonical workflow for downloading/labelling right now, but if you figure one out please make a pull request with the relevant scripts/tools! 

Ideally, we would have a wide variety of different types of websites. Some extractors focus heavily on, say, news articles, which makes them worse at blogs or forums or so on. 
