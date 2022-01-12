# tweeter-app
twitter scraper using twint and other python libs

# Architecture (Parts that made up the project)
- Database (MongoDB)
- API (Django and DajngoRestFramework)
- Cron job
- Clean DB Script

# 1. Database
A database that were the scraped data is saved

# 2. API
An API that enable to perform CRUD operaions across the database

# 3. Cron Job
A separate script that scrape twitter and populate the Database on every given time

# 4. Clean DB script
A script that clean up the database every 24 hours (this feature is to manage our database storage)
