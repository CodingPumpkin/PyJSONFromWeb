# PyJSONFromWeb

This project is my solution for a test task.

## What has been done?
A short python script has been written. 
The script in question uses ``requests``, ``html_to_json`` and ``json`` modules to parse contents of a web page with a given url into a json file (data.json).

## Where does the data come from?
The data for json file is taken from web source https://quotes.toscrape.com/ as specified in the task description.

## How has the data been collected?
The data is collected via requests module which allows one to send http requests using Python. Method get sends a GET request to the url specified as the parameter. This method returns an object of ``requests.models.Response`` class. Among other properties and methods this object has getter method ``text`` which returns contents of the page in unicode.

## Why have these tools been chosen?


