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

3. Start elastic search by running `cd plugins && tar -xzf elasticsearch-5.6.3.tar.gz && ./elasticsearch-5.6.3/bin/elasticsearch` then visit ![http://localhost:9200/](http://localhost:9200/) on your browser, if you see something like the image below, then u successfully started elasticsearch

![screenshot](https://user-images.githubusercontent.com/8668661/32416287-38b279da-c247-11e7-8c15-5b22fcd07c9a.png)

4. Start Django Server in another terminal window by running `python manage.py runserver` then visit ![http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your browser.

5. Optional: Start kibana by running `cd plugins && tar -xzf kibana-5.6.3-darwin-x86_64.tar.gz && ./kibana-5.6.3-darwin-x86_64/bin/kibana` then visit ![http://localhost:5601/](http://localhost:5601/) you should see a dashboard like the image below

![screenshot](https://user-images.githubusercontent.com/8668661/32416395-91f8a108-c248-11e7-841d-ed18ab618029.png)

## Note
```
ElasticSearch & kibana are bundled in this repo, making the repo a bit heavyweight
```


## Test Case
Name | Value  
:--- | :--- 
Test Suite ID | TS001 
Test Case ID | TC001
Test Case Summary | This test is to verify that you can run a search using the search box.
Prerequisites | 1. Elastic Search Server must be up and running.<br>2. Data must have been indexed in Elastic Search
Test Procedure | 1.	Type a keyword and hit enter.
Expected Result | 1. User is suppose to get a filtered result from the elastic search in a json format.
Actual Result | 
Status | 
Remarks | This is a test case for Elastic search example
Created By | Kolawole Balogun
Date of Creation | 05/11/2017
Executed By | 
Date of Execution | 
Test Environment | 