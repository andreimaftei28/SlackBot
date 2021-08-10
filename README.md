# SlackBot
### is a bot that posts a random codewars kata to a designated slack channel at intervals

## Features

- **Scrapping tool** - Scrapes https://www.codewars.com/ and returns a list of exercises saved to a json file
- **Random exercise generator** - Reads a JSON file and returns a 'random' exercise, respecting 2 conditions : different difficulty from the previous and always a different exercise
- **Slack Bot** - Posts a message to a slack channel
- **Scheduler** - Runs the slack bot to send a message to a slack channel at different time intervals...

## Requirements and Installation

**Via Cloning The Repository**

```
# Make sure you have python installed
python --version

# Clone the app
git clone https://github.com/andreimaftei28/SlackBot.git

# Switch to directory
cd SlackBot

# Create virtual env(make sure you have virtualenv installed)
virtualenv --python=python3 venv

# Activate virtual env
source venv/bin/activate

#  Create .env file and copy contents of .env.example and provide details
touch .env

# Install Package dependencies
pip3 install -r requirements.txt

#Start the application

- Run the app - **python3 app.py **

```

## Technologies

- [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
  
- [Selenium](https://selenium.dev/) - Selenium automates browsers. That's it!

- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - Beautiful Soup is a library that makes it easy to scrape information from web pages.

- [Slack API](https://pypi.org/project/slackclient/) - Slack API clients for Web API and RTM API.

- [APScheduler](https://jestjs.io/) - In-process task scheduler with Cron-like capabilities.
