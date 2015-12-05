#!/usr/bin/python
from classes.book_data import BookData
from classes.document_analysis import DocumentAnalysis
from classes.browser_analysis import BrowserAnalysis
from classes.user_analysis import UserAnalysis
import sys
import getopt

bd = BookData('data/issuu_full.json')
dt = bd.build_data_frame()


def task_2(uuid):
    """Perform task from task 3
    :param uuid:
    """
    bs = DocumentAnalysis(dt)
    try:
        # By Countries
        result_countries = bs.countries_by_book(uuid)
        print("Views by country and Document UUID")
        print(result_countries)
        bs.counries_by_book_plot(result_countries, uuid)
        # By Continent
        print("Views by continent and Document UUID")
        result_continent = bs.continent_by_book(result_countries, uuid)
        bs.continent_by_book_plot(result_continent, uuid)
        print(result_continent)
    except Exception as err:
        print((str(err)))


def task_3():
    """Perform task from task 3 """
    ba = BrowserAnalysis(dt)
    try:
        ba.browser_usage_plot()
        ba.general_usage_plot()
    except Exception as err:
        print((str(err)))


def task_4(number):
    """Perform task from task 4
    :param number:
    """
    ra = UserAnalysis(dt)
    try:
        reader_popularity = ra.most_avid_readers(number)
        print(reader_popularity)
    except Exception as err:
        print((str(err)))


def task_5(user_uuid, book_uuid):
    ra = UserAnalysis(dt)
    try:
        find_user_books = ra.find_user_books(user_uuid)
        print("(a)list of all the document UUID read by that visitor")
        print(find_user_books)

        find_book_visitors = ra.find_book_visitors(book_uuid)
        print("(b)list of all the visitor UUIDs that read that document")
        print(find_book_visitors)

    except Exception as err:
        print((str(err)))


def task_6(user_uuid, book_uuid):
    ra = UserAnalysis(dt)
    try:
        user_books_alike = ra.user_visitors_alike(user_uuid)
        print("(Also Like)Similar users based on common book read")
        print(user_books_alike)

        user_book_alike_sorted = ra.users_alike_sorted(user_uuid, ra.sorter)
        print("(d)Sorted by readership profile for sorting the documents")
        print(user_book_alike_sorted)

        visitors_books_alike = ra.book_visitors_alike(book_uuid)
        print("(Also Like)Similar books based on user reader")
        print(visitors_books_alike)

        book_alike_sorted = ra.book_alike_sorted(book_uuid, ra.sorter)
        print("(e)Sorted by number of readers of the same document")
        print(book_alike_sorted)

    except Exception as err:
        print((str(err)))


def main(argv):
    user_uuid = ''
    doc_uuid = ''
    task_id = 0
    try:
        opts, args = getopt.getopt(argv, "hu:d:t:", ["user_uuid=", "doc_uuid=", "task_id="])
    except getopt.GetoptError:
        print('cw2 -u <user_uuid> -d <doc_uuid> -t <task_id>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('cw2.py -u <user_uuid> -d <doc_uuid> -t <task_id>')
            sys.exit()
        elif opt in ("-u", "--user_uuid"):
            user_uuid = arg
        elif opt in ("-d", "--doc_uuid"):
            doc_uuid = arg
        elif opt in ("-t", "--task_id"):
            task_id = arg
    if int(task_id) == 1:
        with open("../requirements.txt", 'r') as fin:
            print("Requirments.txt file content")
            print(fin.read())
    if int(task_id) == 2:
        if doc_uuid == '':
            print(" No doc_uuid supplied")
        else:
            task_2(doc_uuid)
            print("Histograms for per country been saved in : Graphs/results/countries_to_book_UUID.png")
            print("Histograms for per continent been saved in : Graphs/results/continent_to_book_UUI.png")
    elif int(task_id) == 3:
        task_3()
        print("Histograms of browser usage has been saved in 'Graphs/results/simple_browser_usage.png' ")
        print("Histograms of generalised browser usage has been saved in 'Graphs/results/general_browser_usage.png")
    elif int(task_id) == 4:
        print("10 most active readers")
        task_4(10)
    elif int(task_id) == 5:
        if (user_uuid == '') | (doc_uuid == ''):
            print("Provide user_uuid or/and doc_uuid")
            # 938601f24509a9f1 , 110727005030-000000009cca70787e5fba1fda005c85
        else:
            task_5(user_uuid, doc_uuid)
    elif int(task_id) == 6:
        if (user_uuid == '') | (doc_uuid == ''):
            print("Provide user_uuid or/and doc_uuid")
            # 938601f24509a9f1 , 110727005030-000000009cca70787e5fba1fda005c85
        else:
            task_6(user_uuid, doc_uuid)


if __name__ == "__main__":
    main(sys.argv[1:])
