# NoZeroDay
A journal app that enforces No Zero Day mindset when doing challenges or striving to be better.

Start the server with 
`docker-compose up`

You can modify the postgresql's info in settings.py located in the project's folder. Note that if the postgresql doesn't have that database specific table, it will automatically create one, if not, create it by yourself and supply your own desired credentials. Double check your migrations too.
