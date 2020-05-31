# Yelp Review Scraper

## What I eventually want this to be:

This is intended to be part of my Food Mood project. I eventually want to make something (an API?) where you input the user's location and mood, and you get a list of restaurants curated to those inputs. I hope to use a machine learning model that can perform emotion analysis on a number of Yelp reviews from restaurants around the location input, and get the restaurants most tailored towards the mood input.

I created this repo as my first step, to create a dataset of Yelp Reviews (to train my model) by using Python and a webscraper (probably BeautifulSoup). I know there are already Yelp review datasets out there but I wanna at least try this first and see how it goes!

## My Journal

- So the first thing I notice is when I just search for restaurants, I get the following URL: https://www.yelp.com/search?cflt=restaurants&find_loc={CITY}%2C+{STATE}
- What if I got a list of all the states and cities, and just ran that through the link? Then with the corresponding list of restaurants, scraped their reviews? Look like its time for the good 'ol nested for loop to come help me out! Seems easy enough... apart from the fact that scraping all of those reviews would take who know how long. And its probably not easy anyways.
- URL when looking at a restaurant on Yelp: https://www.yelp.com/biz/the-salt-house-new-hope, https://www.yelp.com/biz/entrata-hopewell

  - Looks like the URL contains the name of the restaurant then the city its in. I wonder if there are any exceptions? But yeah, wow its really organized and nice!
  - https://www.yelp.com/biz/{RESTAURANT-NAME}-{CITY}

- So I've been looking into ways of getting a list of states and their cities. I was originally thinking about getting a list of all states and ALL of their cities, but I also know that's kinda impractical for me. I found a nice link on Encyclopaedia Britannica that has a list of states and cities: https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068 I'm not sure what the significance of these cities are, but they seem to be prominent cities.
- And then I found this: https://en.wikipedia.org/wiki/List_of_largest_cities_of_U.S._states_and_territories_by_population
  - I like this because its the top 5 populated cities by state, and I know why these cities are listed.
- So now I'm thinking that I'm going to scrape that Wikipedia page for the states and their corresponding top five most populated cities and put that into a .csv file or something. Then I'll see where to go from there! I think this'll be a good warmup before the massive Yelp scraping.
  - Issue #1: Wikipedia page doesn't have state abbreviations. I'll have to either make a file manually for that or scrape a list online. Or just find one online.
  - Issue #2: Wikipedia page includes territories. Thus, I can include them in my dataset, if their abbreviations work in the Yelp search
    - https://secure.ssa.gov/apps10/poms.nsf/lnx/0901501010 is gov website for states + territories and their abbreviations, nice!
- I think my dataset will have the following sections: ["abbreviation","city1","city2","city3","city4","city5"]
  - Don't need the full name of the state/territory because its never used in the Yelp search as far as I can see
- State & abbreviation scraper done!

### For future reference:
- multithreading: https://docs.python.org/3/library/multiprocessing.html https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e
-machine learning stuff: https://www.youtube.com/watch?v=P0o5U9pq8_s&t=202s
