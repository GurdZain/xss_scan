import os
import requests
import argparse


class Scan():
    def __init__(self, url):
        self.url = url
        self._get_vector_list()
        # self._run()

    def _get_vector_list(self):
        with open('vector.txt') as f:
            self.vector_list = f.readlines()

    def _scan(self, scan_url):
        res = requests.get(scan_url)
        print 1

    def _run(self):
        # get vector list and group url
        for vector in self.vector_list:
            scan_url = self.url + vector
            if self._scan(scan_url):
                print scan_url


def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the url that you scan")
    return parser.parse_args()


if __name__ == '__main__':
    parse = arg()
    Scan(parse.url)
