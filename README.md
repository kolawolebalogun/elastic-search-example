# Elastic Search Example
 This django program is to achieve the following:
 
 * Reads all the data files in `elasticsearchapp/util/data` directory and index them in Elastic Search.
 * A Django GET type API in which takes query parameter ('q') and search within the indexed data in Elastic search.
 * A Simple HTML page with 1 search text box in it, and hit the above API from the search box text.
 
 
## Requirement

Django Admin Locking Example has been tested in the following environments

* Python (3.6)
* Django (1.11.7)
* Java (1.8.0_121)


## Installation

Clone repository with `git clone https://github.com/kolawolebalogun/elastic-search-example.git && cd elastic-search-example`

1. First you create a virtual environment with `virtualenv venv` and enter it with `source venv/bin/activate` in order to keep everything contained. 

2. You run `pip install -r requirements.txt` to install all dependencies

3. Start elastic search by running `./plugins/elasticsearch-5.6.3/bin/elasticsearch` then visit ![http://localhost:9200/](http://localhost:9200/) on your browser, if you see something like the image below, then u successfully started elasticsearch
![screenshot](https://user-images.githubusercontent.com/8668661/32416287-38b279da-c247-11e7-8c15-5b22fcd07c9a.png)

<!-- Start Django Server by running `python manage.py runserver` then visit ![http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your browser. -->
