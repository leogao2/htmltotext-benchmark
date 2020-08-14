# htmltotext-benchmark

The goal of this repository is to provide a dataset of html-to-text extractions performed by hand across as many languages as possible, along with a benchmarking script to be able to provide a quantitative measure of text extraction quality by major html-to-text converters. 

# Motivation

There are a ton of different html-to-text libraries floating around, but there are only a handful of tests comparing them, none of which look at a wide array of languages. The goal of this repository is to be able to provide a common benchmark for all these libraries. 

# Contributing

To contribute, please download the html file to `benchmarkdata/<iso language code>/html/<unique file name>.html` and put your resulting text in `benchmarkdata/<iso language code>/text/<unique file name>.txt`. 

For the file name, please begin with the type of website (this doesn't have to be one of the ones listed here, but try to keep consistency), followed by the name of the source. After that you can use any naming scheme you want (sequential ids, uuids, sha1sums, slug of the url etc) as long as the html and txt have the **same** name. 

Examples of acceptable naming:
 - `news-tagesschau-coronavirus-grossbritannien-1`
 - `blog-leogao-55ca6286e3e4f4fba5d0448333fa99fc5a404a73`
 - `forum-aialignmentforum-FoiiRDC3EhjHx7ayY`

There is no canonical workflow for downloading/labelling right now (the `labelling_helper.py` script is the closest thing, but you dont *have* to use it), but if you figure one out please make a pull request with the relevant scripts/tools! 

Ideally, we would have a wide variety of different types of websites. Some extractors focus heavily on, say, news articles, which makes them worse at blogs or forums or so on. 

## Using the `labelling_helper.py` script

First edit the script and change `lang = 'de'` to whichever language you're doing so the script saves stuff in the right place. Also, you can change `os.system('vim tmp')` to any other editor (like `code tmp` for VS Code, or `emacs tmp` or `gedit tmp`)

To use the script, enter a url, press enter and then enter the name, and press enter again (see previous section for info on naming). Then it should pop up vim so you can edit an automatically extracted text. Delete any extraneous text, add in stuff that should be there (i.e that show up in the browser but not in the extraction), etc. Then save and close, and you'll be able to enter another url and name. 
