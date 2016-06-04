# What's on BBC iPlayer

![Imgur](http://i.imgur.com/4TWmGc6.png)

## About :tv:

This is the server repo for my solution. For front-end repo, please click [here](https://bitbucket.org/junyuanxue/iplayer-movies-frontend).

This server is built with Django REST framework which serves as a RESTful API for front-end Angular app to consume.

As you'd like to keep this challenge private, I decided not to deploy the app.

## Approach and problems encountered :thought_balloon:

I decided to solve the problem with a decoupled app consist of a Django server and an [Angular front-end](https://bitbucket.org/junyuanxue/iplayer-movies-frontend), as it seems to match the architecture your company use (Django back-end with client-side JavaScript framework). Also, as this is my first time using Django, I thought it'd be easier for testing and dependency management when I have 2 separate repos rather than having Angular sitting inside Django. Decoupling would also made the app flexible for future extensions.

Inside the Django server, I have created 2 services (see `movies/services` directory) to make external API calls. `movie_service` calls the [BBC API](http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json) to get a list of available movies from iPlayer, then `rating_service` will take the title of the movie as part of the query string and make a request to the [Movie Database API](https://www.themoviedb.org/documentation/api) for the movie rating. Once `movie_service` gets the rating from `rating_service`, it will format movie data and make it ready to be rendered as json inside `/movies/` views.

One problem I encountered was as the BBC API does not provide an ISBN or release year (it does provide first broadcast date, which sadly does not help much), I could only search in the Movie Database by title. With some movies, for example _Emma_, I would get multiple results. For now I can get the correct movies by just letting `movie_service` select the first movie from all the matches returned by the Movie Database, but that might not work for some other programmes that come up in the future. Also, the server seems to be quite slow when making the 2 requests and returning the parsed data, and as a result it takes a long time before the front-end loads all the movies.

Another challenge was having never used Django before this project and I was getting used to the framework and testing while building the server. As I am making external API calls, I decide not to use a database as I want a most updated list of available movies from BBC every time I use the app. This has certainly made things much easier for me as I only needed to worry about calling external APIs and returning parsed data in a GET `/movies/` request.

For the Angular front-end, I used a service to request a list of movies from the server and rendered them into `Movie` objects using a factory. The list will then be passed into the controller and finally displayed on the index page. The Angular app is served up with Node.

The index page colour theme is inspired by the [BBC iPlayer website](http://www.bbc.co.uk/iplayer/a-z/a). I have also used BBC's programme IDs to link each movie to its iPlayer page. However you might notice BBC is not always accurate with their pid and you would be taken to the wrong version of _The Secret Life of Walter Mitty_. :)

## To run the app :arrow_forward:

Clone the server repo:
```
$ git clone https://junyuanxue@bitbucket.org/junyuanxue/iplayer-movies-server.git
$ cd iplayer-movies-server
```
Create and start your virtual environment:
```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```

You'll need an API key for the [Movie Database API](https://www.themoviedb.org/documentation/api). Once you've registered and acquired your token, set up your local environment variables:
```
$ export MOVIE_DB_API_KEY=your_api_key_here
```
Then run the server:
```
$ python manage.py runserver
```
If you go to `http://localhost:8000/movies/` you'll then see a lovely json file containing a list of movies with their ratings.

To see these movies more beautifully displayed, clone the front-end repo and install dependencies:
```
$ git clone https://junyuanxue@bitbucket.org/junyuanxue/iplayer-movies-frontend.git
$ cd iplayer-movies-frontend
$ npm install
$ bower install
```
Then run the app:
```
$ npm start
```
Visit `http://localhost:3000` and voilà! Click on the links to watch. :sunglasses:


## Testing :white_check_mark:

The server has been tested with unittest. I used Mock to mock out services inside views and the external API calls inside services.

To run the tests:
```
$ ./manage.py test
```

## Tools used in this repo :wrench:
* Django REST framework
* requests
* unittest
* Mock

## Author :cat:
Junyuan Xue

[Github](https://github.com/junyuanxue)
| [CV](https://github.com/junyuanxue/cv)
| [Projects](https://github.com/junyuanxue/cv#projects)
