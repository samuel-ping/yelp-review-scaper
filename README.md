# Yelp Review Scraper

## What this is

This is part of my Food Mood project. I eventually want to make something (an API?) where you put in the user's location and mood, and you get a list of restaurants curated to those inputs. I hope to use a machine learning model that can perform emotion analysis on a number of Yelp reviews from restaurants around the location input, and get the restaurants most tailored towards the mood input.

At the moment, this Python script compiles a dataset of the top five most populated cities in each state in the US, and its next step is to scrape Yelp reviews from the restaurants in these cities.

## Notes

- URL when searching for restaurants: https://www.yelp.com/search?cflt=restaurants&find_loc={CITY}%2C+{STATE}
- URL when looking at a restaurant on Yelp: https://www.yelp.com/biz/the-salt-house-new-hope
  - Looks like the URL contains the name of the restaurant then the city its in.
    - https://www.yelp.com/biz/{RESTAURANT-NAME}-{CITY}
- And then I found this: https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population
  - I like this because its the top 5 populated cities by state, and I know why these cities are listed.
- So now I'm thinking that I'm going to scrape that Wikipedia page for the states and their corresponding top five most populated cities and put that into a .csv file or something. Then I'll see where to go from there! I think this'll be a good warmup before the massive Yelp scraping.
  - Issue: Wikipedia page doesn't have state abbreviations.
    - https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010 is gov website for states + territories and their abbreviations.
- Dataset has the following sections: ["abbreviation","city1","city2","city3","city4","city5"]
  - Don't need the full name of the state/territory because its never used in the Yelp search as far as I can see.
