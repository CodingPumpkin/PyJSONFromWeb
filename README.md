# PyJSONFromWeb

This project is my solution for a test task.

## Note:
Since no additional info has been provided for this task I made it as I see fit. I really hope that at the very least this project showcases some of my coding abilities.

## What has been done?
A short python script has been written. 
The script in question uses `requests`, `html_to_json` and `json` modules to parse contents of a web page with a given url into a json file (data.json). After I gave it a thought I decided to add another output file contents.json which contains what I consider to be relevant information about quotes from the page. Module `BeautifulSoup4` or `bs4` for short handles search for particular tags and extraction of values from particular attributes.

## Where does the data come from?
The data for json file is taken from web source https://quotes.toscrape.com/ as specified in the task description.

## How has the data been collected?
The data is collected via requests module which allows one to send http requests using Python. Method get sends a GET request to the url specified as the parameter. This method returns an object of `requests.models.Response` class. Among other properties and methods this object has getter method `text` which returns contents of the page in unicode.

## Why have these tools been chosen?
As a rule I tend to use modules to solve problems like these. Because unless my task is to get an exercise in a particular topic (like reinvent an algorithm or re-implement a certain functionality) I find it rational to stick to using solutions made by more professional programmers. It does not mean that I do not wish to become one of them. It only means that I try to get the job done before I start tuning all the fine parts.
The second step in choosing which tools to employ is taking a look at which of them seem to be the most standard. If I am new to a topic I try to stick to using well-documented and well-known modules and libraries. First of all, it almost guarantees better compatibility with end-user's system or environment (i.e. if I use a package from my package manager instead of building a library myself chances are that the other person is not to experience difficulties with finding it and setting it up on their system). Secondly, in this case I have much easier job finding references for the modules.
Thus, as `requests`, `json` and `bs4` modules are pretty commonly used for such problems I have experienced no trouble deciding to use them in this project. `html_to_json`, on the other hand, has faced a competitor - `xmltojson` module. However, I find it  more sensible in this scenario to use more specific tool for such a basic task. 

## Additional info
All of the modules used in this project are listed in `requirements.txt`.
Please, use the following command to install them: 
```
pip install -r /path/to/requirements.txt
```
