import pandas
import requests
import json

with open('GE_JSON.json') as file:
    data = json.load(file)

inputItemString = input("Which item do you want data for? ")

inputItemID = data[inputItemString.capitalize()]

BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
response = requests.get(BASE_URL + str(inputItemID))

itemData = response.json()

print("Current - " + str(itemData['item']['current']))
print("Today - " + str(itemData['item']['today']))
print("Past 30 Days - " + str(itemData['item']['day30']))
print("Past 90 Days - " + str(itemData['item']['day90']))
print("Past 180 Days - " + str(itemData['item']['day180']))


