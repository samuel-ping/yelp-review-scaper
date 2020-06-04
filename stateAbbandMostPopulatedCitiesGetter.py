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

    data = []

    for row in stateAbbRows:
        for cols in row.findAll(class_="poms-para"):
            col = cols.getText()
            pair.append(col)
        data.append(pair)
        pair = []

    return data


def getMostPopulatedCities(stateAbbreviations):
    page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population"
    )
    soup = BeautifulSoup(page.text, "html.parser")

    # stateAbbreviation city1 city2 city3 city4 city5
    finalData = [["stateAbbreviation", "city1", "city2", "city3", "city4", "city5"]]

    tempRow = []
    data = []

    table = soup.find("tbody")
    rows = table.findAll("tr")

    with open("citiesList.csv", "w") as csv_file:
        csv_writer = writer(csv_file)
        headerrow = ["stateAbbreviation", "city1", "city2", "city3", "city4", "city5"]
        csv_writer.writerow(headerrow)
        for row in rows[1:]:
            columns = row.findAll("td")
            currentStateHMTL = columns[0].find("a")
            currentState = currentStateHMTL["title"]

            # checks if current state is in state abbreviations list
            containsState = False
            for stateAndAbbreviation in stateAbbreviations:
                if currentState in stateAndAbbreviation:
                    containsState = True
                    currentStateAbbreviation = stateAndAbbreviation[1]
                    break

            if containsState:
                tempRow.append(currentStateAbbreviation)
                # iterates through rest of columns
                for cell in columns[1:-1]:
                    currentCell = cell.getText()
                    currentCell = removeBrackets(currentCell)
                    currentCell = removeNumbers(currentCell)
                    currentCell = removeTrailingJunk(currentCell)

                    if len(currentCell) != 0:
                        tempRow.append(currentCell)

                csv_writer.writerow(tempRow)
                finalData.append(tempRow)
                tempRow = []
            else:
                continue


# recursively removes integers (including commas) in string
def removeNumbers(s):
    if s is None or len(s) == 0:
        return ""

    if s[0] is ",":
        return removeNumbers(s[1:])

    try:
        int(s[0])
        return removeNumbers(s[1:])
    except ValueError:
        return s[0] + removeNumbers(s[1:])


# removes parentheses, brackets
def removeBrackets(s):
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("[", "")
    s = s.replace("]", "")
    return s


# removes newlines and trailing spaces
def removeTrailingJunk(s):
    return s.rstrip()


if __name__ == "__main__":
    stateAbbreviations = getStateAbbreviations()
    getMostPopulatedCities(stateAbbreviations)
