import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def testing_connection():
    # URL for the website
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

    # Handling errors
    try:
        selecting_data(urlopen(url))
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('Error 404 - The server could not be found!', e)


def selecting_data(html):
    # Using BeautifulSoup for best view HTML code
    # And using html.parse for parse text in html
    bs = BeautifulSoup(html, 'html.parser')

    # Selecting a table in the HTML
    movies = bs.select('.lister-list tr')

    creating_csv(movies)


def creating_csv(movies):
    # Creating vars for datas
    titles = []
    directors = []
    years = []
    ratings = []

    # Loop for the movies
    for movie in movies:
        # Passing the values for vars
        # Each value is extract to the html value
        titles.append(movie.find('td', class_='titleColumn').find('a').get_text())
        directors.append(movie.find('td', class_='titleColumn').find('a')['title'])
        years.append(movie.find('td', class_='titleColumn').find('span').get_text()[1:5])
        ratings.append(movie.find('td', class_='imdbRating').find('strong').get_text())

    # Creating a DataFrame with pandas
    data_frame = pd.DataFrame({
        "Title": titles,
        "Year": years,
        "Rating": ratings,
        "Director": directors
    })

    # Creating a csv with values in DataFrame
    data_frame.to_csv('the_best_movies.csv')


def __init__():
    testing_connection()


__init__()
