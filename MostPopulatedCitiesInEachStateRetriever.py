import requests
from csv import writer
from bs4 import BeautifulSoup
from StateAbbreviationsGetter import getStateAbbreviations

# returns dataset with state abbreviations and top 5 most populated cities from each state
def getMostPopulatedCities():
    stateAbbreviations = getStateAbbreviations()
    page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population"
    )
    soup = BeautifulSoup(page.text, "html.parser")

    # stateAbbreviation city1 city2 city3 city4 city5
    finalData = [
        ["stateAbbreviation", "city1", "city2", "city3", "city4", "city5"]
    ]  # pre-initializing headers

    tempRow = []

    table = soup.find("tbody")
    rows = table.findAll("tr")

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
                currentCell = cleanUp(currentCell)

                if len(currentCell) != 0:
                    tempRow.append(currentCell)

            finalData.append(tempRow)
            tempRow = []
        else:
            continue

    return finalData


# same function as above, but returns it in a .csv file
def getMostPopulatedCitiesCSV():
    stateAbbreviations = getStateAbbreviations()
    page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population"
    )
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("tbody")
    rows = table.findAll("tr")

    tempRow = []

    with open("outputs/citiesList.csv", "w") as csv_file:
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
                    currentCell = cleanUp(currentCell)

                    if len(currentCell) != 0:
                        tempRow.append(currentCell)

                csv_writer.writerow(tempRow)
                tempRow = []
            else:
                continue


def cleanUp(s):
    s = removeNumbers(s)
    s = removeBrackets(s)
    s = removeTrailingJunk(s)
    return s


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
    # if you just want to get a list of the state abbreviations, just use the line: getStateAbbreviations()
    print("Getting most populated cities...")
    getMostPopulatedCitiesCSV()
    print("All done!")
