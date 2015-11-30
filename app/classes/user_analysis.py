import operator


class UserAnalysis:

    __labels = ["ts", "visitor_uuid", "visitor_source", "visitor_device", "visitor_useragent",
                "visitor_ip", "visitor_country", "visitor_referrer", "env_type", "env_doc_id", "event_type",
                "event_readtime", "subject_type", "subject_doc_id", "subject_page"]

    def __init__(self, book_data):
        self.__book_data = book_data[self.__labels]

    def find_user_books(self, visitor_uuid):
        """ Find User Books read by user uuid"""
        readers = self.__book_data[(self.__book_data['event_type'] == "pagereadtime") | (self.__book_data['event_type'] == "read")]
        user_books = readers[readers['visitor_uuid'] == visitor_uuid]
        return user_books[['env_doc_id']].drop_duplicates().to_dict()

    def user_visitors_alike(self, visitor_uuid):
        """find similar users based on common book read """
        user_readers = self.find_user_books(visitor_uuid)
        user_similar = {}
        for key, uuid in user_readers.items():
            for book in list(uuid.values()):
                user_similar[book] = list(self.find_book_visitors(book).values())[0].values()
        return user_similar

    def users_alike_sorted(self, visitor_uuid, sorter):
        """Find how many times user read same book and sort them by sorting function param """
        user_similar = self.user_visitors_alike(visitor_uuid)
        user_readership = {}
        for key, user_list in user_similar.items():
            for user in user_list:
                if user in user_readership:
                    user_readership[user] += 1
                else:
                    user_readership[user] = 1
        return sorted(list(user_readership.items()), key=operator.itemgetter(1), cmp=sorter)[:10]

    def find_book_visitors(self, book_uuid):
        """Find Book readers by book uuid"""
        readers = self.__book_data[(self.__book_data['event_type'] == "pagereadtime") | (self.__book_data['event_type'] == "read")]
        user_books = readers[readers['env_doc_id'] == book_uuid]
        return user_books[['visitor_uuid']].drop_duplicates().to_dict()

    def book_visitors_alike(self, book_uuid):
        """Find similar books based on users other read books"""
        book_readers = self.find_book_visitors(book_uuid)
        book_similar = {}
        for key, uuid in book_readers.items():
            for user in list(uuid.values()):
                book_similar[user] = list(self.find_user_books(user).values())[0].values()
        return book_similar

    def book_alike_sorted(self, book_uuid, sorter):
        """Find how many users have read each book and sort them by sorter function parameter """
        book_similar = self.book_visitors_alike(book_uuid)
        book_readership = {}
        for key, book_list in book_similar.items():
            for book in book_list:
                if book in book_readership:
                    book_readership[book] += 1
                else:
                    book_readership[book] = 1
        return sorted(list(book_readership.items()), key=operator.itemgetter(1), cmp=sorter)[:10]

    def sorter(self, x, y):
        """Sorting Function"""
        return y - x

    def most_avid_readers(self, number_of):
        """ Select best Reader and pick any number of them"""
        readers = self.__book_data[self.__book_data['event_type'] == "pagereadtime"]
        reader_popularity = readers[['visitor_uuid', 'event_readtime']].groupby('visitor_uuid').aggregate(sum)
        reader_popularity = reader_popularity.sort(['event_readtime'], ascending=False)[:10]
        return reader_popularity

    def best_readers_data(self, number_of):
        """ Get Data of most active users """
        readers_time = self.most_avid_readers()[:number_of]
        readers_list = readers_time['event_readtime'].to_dict()
        readers_data = {}
        for key, value in readers_list.items():
            readers_data[key] = self.__book_data[self.__book_data['visitor_uuid'] == key][:1].to_dict()
            readers_data[key]['total_time'] = readers_list[key]
        return readers_data
