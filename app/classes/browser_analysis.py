import matplotlib.pyplot as plt
import pandas as pd


class BrowserAnalysis:

    __main_browsers = ["opera", "dalvik", "safari", "chrome", 'trident', 'mozilla']
    __labels = ["ts", "visitor_uuid", "visitor_source", "visitor_device", "visitor_useragent",
                "visitor_ip", "visitor_country", "visitor_referrer"]

    def __init__(self, book_data):
        self.__document_data = book_data
        self.__document_data = self.__document_data[self.__labels]

    def browser_usage(self):
        """ Group dataframe by visitor browser and counts distinct"""
        browser_usage = self.__document_data['visitor_useragent'].value_counts()
        return browser_usage

    def browser_usage_plot(self):
        """ Create a histogram plot based on browser usage"""
        browser_usage = self.browser_usage()
        browser_usage.plot(kind='bar')
        plt.savefig('Graphs/simple_browser_usage.png')

    def general_usage(self):
        """Perform more robust calculation of browser usage"""
        browser_usage = self.browser_usage()
        browser_usage_data = browser_usage.to_dict()
        general_usage = {}
        for browser in self.__main_browsers:
            for key, value in browser_usage_data.items():
                if browser in key.lower():
                    if browser in general_usage:
                        general_usage[browser] += value
                    else:
                        general_usage[browser] = value
        return general_usage

    def general_usage_plot(self):
        """ Create plot based on general usage"""
        general_usage = self.general_usage()
        general_usage_data = pd.Series(list(general_usage.values()), list(general_usage.keys()))
        general_usage_data.plot(kind='bar')
        plt.savefig('Graphs/general_browser_usage.png')
