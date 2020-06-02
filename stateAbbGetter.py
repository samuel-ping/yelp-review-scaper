import requests
from csv import writer
from bs4 import BeautifulSoup

# retrieves and returns the name of states/territories and their abbreviations in a list
def getStateAbbreviations():
    stateAbbPage = requests.get(
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010")
    soup = BeautifulSoup(stateAbbPage.text, "html.parser")

    stateAbbTable = soup.find(id="tbl_1")
    stateAbbRows = stateAbbTable.findAll("tr")

    pair = []  # temporarily stores each state/territory and abbreviation pair

    # with open("statesAbbreviations.csv", "w") as csv_file:
    #     csv_writer = writer(csv_file)

    #     for row in stateAbbRows:  # iterates through all of the rows in the list
    #         # iterates through the two columns in each list (state/territory and its abbreviation)
    #         for cols in row.findAll(class_="poms-para"):
    #             col = cols.getText()  # gets state/territory/abbreviation from element
    #             pair.append(col)  # temporarily stores the content
    #         csv_writer.writerow(pair)  # adds pair to csv file
    #         pair = []  # resets pair to blank

    data = []

    for row in stateAbbRows:  
            for cols in row.findAll(class_="poms-para"):
                col = cols.getText()
                pair.append(col)
            data.append(pair)
            pair = []
    
    return data

def getMostPopulatedCities(stateAbbreviations):
    page = requests.get("https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population")
    soup = BeautifulSoup(page.text, "html.parser")

    tempRow = []
    data = []

    rows = soup.findAll("tr")

    for row in rows:
        cols = row.findAll("td")
        for cell in cols:
            cellContent = cell.getText()
            print("-----------------")
            print(cellContent)

# recursively removes integers and parentheses in string
def removeIntsParenths(s):
    if(len(s) == 0):
        return ""

    # removes parentheses
    if s[0]=="(" or s[0] == ")":
        return removeIntsParenths(s[1:])

    # removes numbers
    try:
        int(s[0])
        return removeIntsParenths(s[1:])
    except ValueError:
        return s[0] + removeIntsParenths(s[1:])
    

if __name__ == "__main__":
    stateAbbreviations = getStateAbbreviations()
    getMostPopulatedCities(stateAbbreviations)