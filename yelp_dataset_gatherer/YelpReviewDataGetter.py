import requests
from csv import writer
from bs4 import BeautifulSoup
from MostPopulatedCitiesInEachStateRetriever import getMostPopulatedCities

# 1. Separate list of abbreviations from cities
def YelpDatasetGetter():
    citiesList = getMostPopulatedCities()

    tempReviewsList = []  # temporarily stores all the reviews per restaurant

    for row in citiesList[1:]:
        currentState = row[0]
        for currentCity in row[1:]:
            searchURL = (
                "https://www.yelp.com/search?cflt=restaurants&find_loc="
                + currentCity
                + "%2C+"
                + currentState
            )

            restaurantSearchPage = requests.get(searchURL)
            restaurantSearchPageSoup = BeautifulSoup(
                restaurantSearchPage.text, "html.parser"
            )

            restaurantsList = restaurantSearchPageSoup.findAll(
                "li",
                class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU",
            )

            # gets URL for each restaurant listing
            for restaurantListing in restaurantsList[5:]:
                restaurantURLEnding = restaurantListing.find("a")["href"]
                restaurantURL = "https://yelp.com" + restaurantURLEnding
                print(restaurantURL)

                restaurantPage = requests.get(restaurantURL)
                restaurantPageSoup = BeautifulSoup(restaurantPage.text, "html.parser")
                reviewsRawList = restaurantPageSoup.findAll(
                    "li",
                    class_="lemon--li__373c0__1r9wz margin-b3__373c0__q1DuY padding-b3__373c0__342DA border--bottom__373c0__3qNtD border-color--default__373c0__3-ifU",
                )

                for review in reviewsRawList:
                    reviewText = review.find("span", {"lang": "en"}).getText()
                    tempReviewsList.append(reviewText)

                break  # testing
            break  # testing
        break  # testing
    print(tempReviewsList)


if __name__ == "__main__":
    YelpDatasetGetter()
