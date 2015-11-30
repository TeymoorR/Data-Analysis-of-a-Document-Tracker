import pandas as pd


class BookData:

    def __init__(self, filename):
        self.__source_file = filename

    def build_data_frame(self):
        """ Return pandas object Read Issue data from file."""
        book_data = pd.read_json(self.__source_file)
        return book_data
