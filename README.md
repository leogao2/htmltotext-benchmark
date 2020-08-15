# htmltotext-benchmark

The goal of this repository is to provide a dataset of html-to-text extractions performed by hand across as many languages as possible, along with a benchmarking script to be able to provide a quantitative measure of text extraction quality by major html-to-text converters. 

# Motivation

There are a ton of different html-to-text libraries floating around, but there are only a handful of tests comparing them, none of which look at a wide array of languages. The goal of this repository is to be able to provide a common benchmark for all these libraries. 

# Contributing


## Manual contibuting

To contribute, please download the html file to `benchmarkdata/<iso language code>/html/<unique file name>.html` and put your resulting text in `benchmarkdata/<iso language code>/text/<unique file name>.txt`. You can also use the script (see below)

## Using the `labelling_helper.py` script

labelling_helper.py is a helper script to make transcribing benchmark data from webpages faster.

Usage:

```
python labelling_helper.py language --editor texteditor

positional arguments:
  lang             target language

optional arguments:
  -h, --help       show this help message and exit
  --editor EDITOR  text editor to use, default is vim
```

Examples:

```
python labelling_helper.py en --editor nano
python labelling_helper.py fr
python labelling_helper.py zh --editor emacs
```

Once the script is running, you'll be prompted to enter a url. Enter the url for your chosen webpage, press enter, and then enter a filename. Press enter again (see below section for info on naming). Then an automatically extracted text from your url should pop up in your selected text editor so you can correct it. Delete any extraneous text, (we want to be removing any boilerplate/UI elements; for more details, see Guidelines section below) and add in text that should be there (i.e text that shows up in the browser but not in the extraction). Finally, save and close, and you'll be able to enter another url and name. 

## Naming

For the file name, please begin with the type of website (this doesn't have to be one of the ones listed here, but try to keep consistency), followed by the name of the source. After that you can use any naming scheme you want (sequential ids, uuids, sha1sums, slug of the url etc) as long as the html and txt have the **same** name. 

Examples of acceptable naming:
 - `news-tagesschau-coronavirus-grossbritannien-1`
 - `blog-leogao-55ca6286e3e4f4fba5d0448333fa99fc5a404a73`
 - `forum-aialignmentforum-FoiiRDC3EhjHx7ayY`

There is no canonical workflow for downloading/labelling right now (the `labelling_helper.py` script is the closest thing, but you dont *have* to use it), but if you figure one out please make a pull request with the relevant scripts/tools! 

## Guidelines

Keep:
 - Comments (if applicable&possible)
 - Date posted, username for forums
 - Transcribe bullet points and numbered lists if possible

Don't keep:
 - UI components: "Click to Reply", "Login / register", etc
 - Boilerplate stuff like cookie notices that pop up at the tops/bottoms of pages

In general, keep anything that would be useful for GPT-x training.

## Which websites to pick

Ideally, we would have a wide variety of different types of websites. Some extractors focus heavily on, say, news articles, which makes them worse at blogs or forums or so on. 
