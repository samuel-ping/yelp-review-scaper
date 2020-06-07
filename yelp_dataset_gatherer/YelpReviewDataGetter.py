import requests
from csv import writer
from bs4 import BeautifulSoup
from MostPopulatedCitiesInEachStateRetriever import getMostPopulatedCities

# 1. Separate list of abbreviations from cities
def YelpDatasetGetter():
    citiesList = getMostPopulatedCities()

    tempReview = []  # temporarily stores review data

    with open("outputs/yelpReviewsDataset.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        headerrow = ["restaurantName", "rating", "reviewText"]
        csv_writer.writerow(headerrow)

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
                    try:
                        restaurantName = restaurantListing.find(
                            "a",
                            class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE",
                            # )
                            # print(restaurantName)
                        ).getText()
                        print(restaurantName)
                    except AttributeError:
                        continue
                    restaurantURLEnding = restaurantListing.find("a")["href"]
                    restaurantURL = "https://yelp.com" + restaurantURLEnding
                    print("Scraping", restaurantURL)

                    restaurantPage = requests.get(restaurantURL)
                    restaurantPageSoup = BeautifulSoup(
                        restaurantPage.text, "html.parser"
                    )
                    reviewsRawList = restaurantPageSoup.findAll(
                        "li",
                        class_="lemon--li__373c0__1r9wz margin-b3__373c0__q1DuY padding-b3__373c0__342DA border--bottom__373c0__3qNtD border-color--default__373c0__3-ifU",
                    )
                    for review in reviewsRawList:
                        tempReview.append(restaurantName)
                        reviewRating = review.find(
                            "div", class_="i-stars__373c0__1BRrc"
                        )["aria-label"][
                            0
                        ]  # gets the number of stars in the rating (1-5)
                        tempReview.append(reviewRating)
                        reviewText = review.find("span", {"lang": "en"}).getText()
                        tempReview.append(reviewText)
                        csv_writer.writerow(tempReview)
                        tempReview = []

                    # break  # testing
                # break  # testing
            # break  # testing
        # print(tempReview)


if __name__ == "__main__":
    YelpDatasetGetter()
