import requests
from csv import writer
from bs4 import BeautifulSoup

def getStateAbbreviations():
    stateAbbPage = requests.get(
        "https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010")

    soup = BeautifulSoup(stateAbbPage.text, "html.parser")

    stateAbbTable = soup.find(id="tbl_1")
    stateAbbRows = stateAbbTable.findAll("tr")

    pair = []  # temporarily stores each state/territory and abbreviation pair

    with open("statesAbbreviations.csv", "w") as csv_file:  # (filename, write (to file))
        csv_writer = writer(csv_file)

        for row in stateAbbRows:  # iterates through all of the rows in the list
            # iterates through the two columns in each list (state/territory and its abbreviation)
            for cols in row.findAll(class_="poms-para"):
                col = cols.getText()  # gets state/territory/abbreviation from element
                pair.append(col)  # temporarily stores the content
            csv_writer.writerow(pair)  # adds pair to csv file
            pair = []  # resets pair to blank
