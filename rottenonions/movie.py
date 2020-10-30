import pandas as pd
import sqLite3

from config import Config

MOVIE_ARRAY_DELIMTER = ','

"""
Movie object interface
"""
class Movie:
    # Movie attributes
    _title = None
    _genre = None
    _description = None
    _director = None
    _actors = None
    _year = None
    _runtime = None
    _rating = None
    _votes = None
    _revenue = None
    _score = None
    _rank = None

    """
    Movie init
    :param pd: Pandas dataframe
    """
    def __init__(self, data: dict = None) -> None:
        super().__init__()

        # Load data from dataframe
        if data is not None:
            self.title = str(data['Title'])
            self.genre = str(data['Genre']).split(MOVIE_ARRAY_DELIMTER)
            self.description = str(data['Description'])
            self.director = str(data['Director'])
            self.actors = str(data['Actors']).split(MOVIE_ARRAY_DELIMTER)
            self.year = int(data['Year'])
            self.runtime = float(data['Runtime (Minutes)'])
            self.rating = float(data['Rating'])
            self.votes = int(data['Votes'])
            self.revenue = float(data['Revenue (Millions)'])
            self.score = int(data['Metascore'])
            self.rank = int(data['Rank'])

    """
    title property getter
    """
    @property
    def title(self) -> str:
        return self._title

    """
    title property setter
    """
    @title.setter
    def title(self, x: str):
        if not len(x):
            raise Exception('Invalid title provided')

        self._title = str(x)

    """
    genre property getter
    """
    @property
    def genre(self) -> [str]:
        return self._genre

    """
    genre property setter
    """
    @genre.setter
    def genre(self, x: [str]):
        if not len(x):
            raise Exception('Invalid title provided')

        self._genre = x

    """
    description property getter
    """
    @property
    def description(self) -> str:
        return self._description

    """
    description property setter
    """
    @description.setter
    def description(self, x: str):
        if not len(x):
            raise Exception('Invalid description provided')

        self._description = str(x)

    """
    director property getter
    """
    @property
    def director(self) -> str:
        return self._director

    """
    director property setter
    """
    @director.setter
    def director(self, x: str):
        if not len(x):
            raise Exception('Invalid director provided')

        self._director = str(x)

    """
    actors property getter
    """
    @property
    def actors(self) -> [str]:
        return self._actors

    """
    actors property setter
    """
    @actors.setter
    def actors(self, x: [str]):
        if not len(x):
            raise Exception('Invalid actors provided')

        self._actors = x

    """
    year property getter
    """
    @property
    def year(self) -> int:
        return self._year

    """
    year property setter
    """
    @year.setter
    def year(self, x: int):
        if x < 0:
            raise Exception('Invalid year provided')

        self._year = int(x)

    """
    runtime property getter
    """
    @property
    def runtime(self) -> float:
        return self._runtime

    """
    runtime property setter
    """
    @runtime.setter
    def runtime(self, x: float):
        if x < 0:
            raise Exception('Invalid runtime provided')

        self._runtime = float(x)

    """
    rating property getter
    """
    @property
    def rating(self) -> float:
        return self._rating

    """
    rating property setter
    """
    @rating.setter
    def rating(self, x: float):
        if x < 0:
            raise Exception('Invalid rating provided')

        self._rating = float(x)

    """
    votes property getter
    """
    @property
    def votes(self) -> int:
        return self._votes

    """
    votes property setter
    """
    @votes.setter
    def votes(self, x: int):
        if x < 0:
            raise Exception('Invalid votes provided')

        self._votes = int(x)

    """
    revenue property getter
    """
    @property
    def revenue(self) -> float:
        return self._revenue

    """
    revenue property setter
    """
    @revenue.setter
    def revenue(self, x: float):
        if x < 0:
            raise Exception('Invalid revenue provided')

        self._revenue = float(x)

    """
    score property getter
    """
    @property
    def score(self) -> int:
        return self._score

    """
    score property setter
    """
    @score.setter
    def score(self, x: int):
        if x < 0:
            raise Exception('Invalid score provided')

        self._score = int(x)

    """
    rank property getter
    """
    @property
    def rank(self) -> int:
        return self._rank

    """
    rank property setter
    """
    @rank.setter
    def rank(self, x: int):
        if x < 0:
            raise Exception('Invalid rank provided')

        self._rank = int(x)

    def __hash__(self) -> int:
        return hash(self.title) ^ hash(self.year)

    def __eq__(self, obj: object) -> bool:
        return self.__hash__() == obj.__hash__()

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) directed by {self.director}"

"""
Movie database model
"""
class MovieDatabase:

    con = sqlite3.connect("data/portal_mammals.sqlite")

    # Pandas dataframe object
    _df = None

    def __init__(self):
        self._df = pd.read_sql_query("SELECT * FROM movies", con)
        self._df.fillna(0, inplace=True)
        self._df.astype({
            'Rank': int,
            'Title': str,
            'Genre': str,
            'Description': str,
            'Director': str,
            'Actors': str,
            'Year': int,
            'Runtime (Minutes)': int,
            'Rating': float,
            'Votes': int,
            'Revenue (Millions)': float,
            'Metascore': int,
        })
    con.close()

    """
    Get movie from database
    :param title: of movie to find (str)
    :param year: of movie to find (int)
    :return: Movie object or None on fail
    """
    def get(self, title: str, year: int) -> Movie:
        m = self._df.loc[(self._df['Title'] == title) & (self._df['Year'] == year)]
        return Movie(m.to_dict('r')[0])

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    def __next__(self):
        i = next(self._it)
        return Movie(i[1].to_dict())

    def __iter__(self):
        self._it = self._df.iterrows()
        return self
