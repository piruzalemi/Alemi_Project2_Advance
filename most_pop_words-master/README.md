# most_pop_words

- A simple python script for ingesting data from txt files that contain the most popular/ commonly used words in each language and stores them in a mongo database, each language is it's own collection. 

- Then a simple api that can serve the data by calling the mongo database. The url is setup for you can pull data from one language at a time 

for example:
```
.../api/v1/<language>
```
where language is the variable in the url that you would specify to get the language you want to see.
thus for english the url would look like:	 
```
.../api/v1/en_full
```
