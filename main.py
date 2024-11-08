target_url = "https://quotes.toscrape.com/"

import requests
import html_to_json
import json
from bs4 import BeautifulSoup

def parse_contents(raw_text):
    soup = BeautifulSoup(raw_text, features="html.parser")
    contents_dict = {}
    temp_list = []
    for anchor_quotes in soup.findAll('div', {"class": "quote"}):
        temp_obj = {}
        anchor_text = anchor_quotes.find('span', {"class": "text"})
        temp_obj['quote'] = str(anchor_text.string)
        anchor_author = anchor_quotes.find('small', {"class": "author"})
        temp_obj['author'] = str(anchor_author.string)
        anchor_tags = anchor_quotes.find('meta', {"class":"keywords"})
        temp_obj['tags'] = str(anchor_tags["content"]).split(',')
        temp_list.append(temp_obj)
    contents_dict['quotes'] = temp_list
    return contents_dict

#Send request and get a responce object containing data from and about the page
html_response = requests.get(url=target_url)

#Get text from response object
raw_text = html_response.text

#Convert text written in HTML to JSON
json_dict = html_to_json.convert(raw_text)

#Create a json dict for contents
json_contents_dict = parse_contents(raw_text)

#Save the results to respective files
with open("data.json", "w") as file:
    json.dump(json_dict, file, indent=2)
with open("contents.json", "w") as file:
    json.dump(json_contents_dict, file, indent=2)


