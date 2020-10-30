import os
import sqlite3
import glob
import sqlalchemy


class Config:

    engine = create_engine('sqlite://movie_dbase.sqlite'echo=False)
    Session = sessionmaker(bind = engine)
    session = Session()
    Base = declarative_base()
    metadata = MetaData(engine)

    class movie_table(object):
        def __init__(self, title, genre, description, director, actors, year, runtime, rating, votes, revenue, score, rank):
            self.title = title
            self.genre = genre
            self.description = description
            self.director = director
            self.actors = actors
            self.year = year
            self.runtime = runtime
            self.rating = rating
            self.votes = votes
            self.revenue = revenue
            self.score = score
            self.rank = rank

        def __repr__(self):
            return f'{self.title, self.genre, self.description, self.director, self.actors, self.year, self.runtime, self.rating, self.votes, self.revenue, self.score, self.rank}'

        def table_definition(table_name):
            table_definition.table_define = Table(table_name, metadata,
            Column('Title', str),
            Column('Genre', str),
            Column('Description', str),
            Column('Director', str),
            Column('Actors', str),
            Column('Year', int),
            Column('Runtime', float),
            Column('Rating', float),
            Column('Votes', int),
            Column('Revenue (Millions)', float),
            Column('Score', int),
            Column('Rank', int)
            )

            metadata.create_all(engine)

            mapper(movie_table,table_definition.table_define,non_primary=True)

            table_define_dummy = Table('dummy_table', metadata,
            Column('Title', str),
            Column('Genre', str),
            Column('Description', str),
            Column('Director', str),
            Column('Actors', str),
            Column('Year', int),
            Column('Runtime', float),
            Column('Rating', float),
            Column('Votes', int),
            Column('Revenue (Millions)', float),
            Column('Score', int),
            Column('Rank', int)
            )

            metadata.create_all(engine)

            mapper(movie_table, table_define, dummy)

            def create_table(folder_of_files):
                files = glob.glob(os.path.join(folder_of_files, "*.csv"))

                for file_name in files:

                    csv_data = pd.read_csv(file_name)
                    csv_data = csv_data.values.tolist()
                    table_name_from_file = file_name.split('/')[8][:-4]
                    table_definition(table_name_from_file)

                    for row in csv_data:
                        ins = table_definition.table_define.insert().values(
                          title = row[0]
                          genre = row[1]
                          description = row[2]
                          director = row[3]
                          actors = row[4]
                          year = row[5]
                          runtime = row[6]
                          rating = row[7]
                          votes = row[8]
                          revenue = row[9]
                          score = row[10]
                          rank = row[11]
                        )
                        con = engine.connect()
                        con = engine.execute(ins)

    create_table("path of folder where csv files are stored")