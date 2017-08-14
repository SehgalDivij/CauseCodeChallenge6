### CauseCode Assignment

Added Scraper to scrape user profile info from profiles present at  about.me

## About

A web scraper that fetches profiles from the website `www.about.me/{user_name}` and saves them to the database

Example user names to search against:

    maxkarren
    bonniethanos
    shimite
    sanjaychauhan

## Using This

Make a POST Request to the url

        www.localhost:8000/api/about_me/profiles/

    with the following body:

        {
            "username":"user_name here"
        }

If the profile has not been scraped before, it will be fetched from their website and added to the database.

If the profile has already been scraped once, it will be fetched from the database.
