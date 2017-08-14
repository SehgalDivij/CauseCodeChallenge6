### CauseCode Assignment

Added Scraper to scrape user profile info from profiles present at  about.me

### Assumptions

Following assumptions are being made about the test environment:

    1. Django's `built-in development server` will be used to run the application.

    2. A version of python3(3.5.x or further) will be used for the application.

    3. The machine running this application has internet connectivity available.

## What the application does

A web scraper that fetches profiles from the website `www.about.me/{user_name}` and saves them to the database

Example user names to search against:

    maxkarren
    bonniethanos
    shimite
    sanjaychauhan

    The application will work fine user names outside of this list that exist on about.me's website.

## How to make use of this application

Make a POST Request to the url

        www.localhost:8000/api/about_me/profiles/

    with the following body:

        {
            "username":"user_name here"
        }

If the profile has not been fetched before, it will be fetched from their website and added to the database.

If the profile has already been fetched once, it will be fetched from the database.

## Running This Application

    1. Clone the repository

    2. Install dependencies from `requirements.txt` file using the command:

        pip install -r requirements.txt

    3. Run the following commands to setup the SQLite Database:

        python manage.py makemigrations
        python manage.py migrate

    4. Run the application:

        python manage.py runserver

    In case `python3.x` as well as `python2` are installed on the system, use `python3` instead of `python` and `pip3` instead of `pip` to make sure `python3` is used to run the application as well as `pip3` is used to install dependencies for the application.
