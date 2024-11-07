target_url = "https://quotes.toscrape.com/"

import requests
import html_to_json
import json

html_response = requests.get(url=target_url)

raw_text = html_response.text

json_dict = html_to_json.convert(raw_text)

with open("data.json", "w") as file:
   json.dump(json_dict, file, indent=2)
