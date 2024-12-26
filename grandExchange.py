import pandas
import requests
import json

Loop = True
BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='

def getItemByName(itemName):
    with open('GE_JSON.json') as file:
        data = json.load(file)
    try:
        inputItemID = str(data[itemName.capitalize()])
    except:
        print("\nNo item with this name was found\n")
    else:
        getItemById(inputItemID)

def getItemById(itemId):
    try:
        response = requests.get(BASE_URL + itemId)
        itemData = response.json()
    except:
        print("\nNo item with this id was found\n")
    else:
        print("\nName - " + str(itemData['item']['name']) + " | Id - " + str(itemData['item']['id']) + "\n")
        print("Current - " + str(itemData['item']['current']))
        print("Today - " + str(itemData['item']['today']))
        print("Past 30 Days - " + str(itemData['item']['day30']))
        print("Past 90 Days - " + str(itemData['item']['day90']))
        print("Past 180 Days - " + str(itemData['item']['day180']) + "\n")

while Loop:
    innerLoop = True
    inputType = input("\nWould you like to search by id or name? ").lower()    

    match inputType:
        case "id":
            itemIDString = input("\nPlease enter the id of the item you want data for? ")
            getItemById(itemIDString)
        case "name":
            itemNameString = input("\nPlease enter the name of the item you want data for? ")
            getItemByName(itemNameString)
        case _:
            print("\nYou can only search by entering 'id' or 'name' ")
            continue

    while innerLoop:
        possibleBreak = input("Would you like to search for another item? [YES/NO] ").lower()

        match possibleBreak:
            case "yes":
                innerLoop = False
            case "no":
                Loop = False
                innerLoop = False
            case _:
                print("\nPlease choose a valid option \n") 