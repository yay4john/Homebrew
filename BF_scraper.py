# Import the required packages
import requests                     # get html, submit posts
from bs4 import BeautifulSoup       # parse and search through html
import pandas as pd                 # dataframes!
import json                         # convert string to dictionary
import html5lib                     # used to parse the html
import time                         # pause between scrapings, don't want to anger any IT people
import random                       # make the pause randomized, so the scraper looks less... scraper-y

# Create empty dataframes
dfBeers = pd.DataFrame(columns=['ID','Title','Style','Size','OG','FG','ABV','IBU',
    'Color','Views','Brewed','URL'])     # list of beers
dfBeerStats = pd.DataFrame(columns=['ID','Method','Boil Time','Pre Boil Size','Pre Boil Gravity',
    'Efficiency','Rating','Number of Reviews','Hop Utilization','Calories','Carbs'])    # vital stats
# recipe details
dfBeerFermentables = pd.DataFrame(columns=['ID','Amount','Fermentable','Cost','PPG','L','Bill %'])
dfBeerHops = pd.DataFrame(columns=['ID','Amount','Variety','Cost','Type','AA','Use','Time','IBU','Bill %'])
dfBeerMash = pd.DataFrame(columns=['ID','Amount','Description','Type','Temp','Time'])
dfBeerOther = pd.DataFrame(columns=['ID','Amount','Name','Cost','Type','Use','Time'])
dfBeerYeast = pd.DataFrame(columns=['ID','Name','Amount','Cost','Attenuation','Flocculation','Optimum Temp',
    'Starter','Fermentation Temp','Pitch Rate'])
dfBeerNotes = pd.DataFrame(columns=['ID','Notes'])

# Set URL
baseURL = 'https://www.brewersfriend.com/homebrew-recipes/'

# pass contact info in case the webmaster needs it
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36;'+
'John Cox/johnisaac.cs@icloud.com'}

# get the html and parse it
page = requests.get(baseURL, timeout=10.0, headers=headers).text
soup = BeautifulSoup(page, 'html5lib')

print(soup.prettify())