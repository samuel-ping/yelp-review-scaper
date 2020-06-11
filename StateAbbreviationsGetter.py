import requests
from csv import writer
from bs4 import BeautifulSoup

# retrieves and returns the name of states/territories and their abbreviations in a list
def getStateAbbreviations():
    stateAbbPage = requests.get("https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010")
    soup = BeautifulSoup(stateAbbPage.text, "html.parser")

    stateAbbTable = soup.find(id="tbl_1")
    stateAbbRows = stateAbbTable.findAll("tr")

    pair = []  # temporarily stores each state/territory and abbreviation pair
    data = []  # data that will be returned eventually

    # iterates through all of the rows in the list
    for row in stateAbbRows:
        # iterates through the two columns in each list (state/territory and its abbreviation)
        for cols in row.findAll(class_="poms-para"):
            col = cols.getText()  # gets state/territory/abbreviation from element
            pair.append(col)  # temporarily stores the content
        data.append(pair)  # adds pair to csv file
        pair = []

    return data


# same function as above, but writes output into a .csv file instead of returning it
def getStateAbbreviationsCSV():
    stateAbbPage = requests.get("https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010")
    soup = BeautifulSoup(stateAbbPage.text, "html.parser")

    stateAbbTable = soup.find(id="tbl_1")
    stateAbbRows = stateAbbTable.findAll("tr")

    pair = []

    with open("outputs/statesAbbreviations.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        for row in stateAbbRows:

            for cols in row.findAll(class_="poms-para"):
                col = cols.getText()
                pair.append(col)
            csv_writer.writerow(pair)
            pair = []
