import unittest
from classes.book_data import BookData
from classes.document_analysis import DocumentAnalysis


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        """Prepare for tests"""
        self.book_uuid = "110727005030-000000009cca70787e5fba1fda005c85"
        self.user_uuid = "938601f24509a9f1"
        bd = BookData('data/issuu_full.json')
        self.dt = bd.build_data_frame()

    def test_task_2_1(self):
        """Check if outut is correct"""
        bs = DocumentAnalysis(self.dt)
        result_countries = bs.countries_by_book(self.book_uuid)
        result_continent = bs.continent_by_book(result_countries, self.book_uuid)
        self.assertEqual(result_continent, {'EU': 2, 'NA': 1, 'SA': 23, 'OC': 1})

    def test_task_2_2(self):
        bs = DocumentAnalysis(self.dt)
        """ Test if expetion is raised  for bad uuid"""
        result_countries = bs.countries_by_book(self.book_uuid)
        self.assertRaises(Exception, bs.continent_by_book(result_countries, "110727005030-00"))


if __name__ == '__main__':
    unittest.main()
