# What's on BBC iPlayer

![Imgur](http://i.imgur.com/4TWmGc6.png)

## About :tv:

This is a simple web app that fetches and displays a list of available movies from the BBC iPlayer API with their ratings, which are provided by the Movie Database API.

The server is built with Django REST framework which serves as a RESTful API for the [front-end Angular app](https://github.com/junyuanxue/iplayer-movies-frontend) to consume.

## To run the app :arrow_forward:

Clone the server repo:
```
$ git clone https://github.com/junyuanxue/iplayer-movies-server.git
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
$ git clone https://github.com/junyuanxue/iplayer-movies-frontend.git
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
* BBC iPlayer API
* Movie Database API

## Author :cat:
Junyuan Xue

[Github](https://github.com/junyuanxue)
| [CV](https://github.com/junyuanxue/cv)
| [Blog](https://spinningcodes.wordpress.com/)
