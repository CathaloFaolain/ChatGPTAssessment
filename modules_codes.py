import requests
from bs4 import BeautifulSoup
import pandas as pd
# Make a request
page = requests.get(
    "https://hub.ucd.ie/usis/W_HU_REPORTING.P_DISPLAY_QUERY?p_code1=ALL&p_code2=S147&p_query=CB216-1&p_parameters=")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list
tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select('a'):
    tags.append(element.text)


df = pd.DataFrame(tags)
df.to_csv("MODULES_MME.csv")