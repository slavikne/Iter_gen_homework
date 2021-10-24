import json
import csv

BASE_URL = 'https://en.wikipedia.org/wiki/'

class WikiIterate:
        def __init__(self, path, url):
            self.file = open(path)
            self.countries = json.load(self.file)
            self.url = url
            self.cursor = -1
        def __iter__(self):
            return self

        def __next__(self):
            self.cursor += 1
            if self.cursor == len(self.countries):
                self.file.close()
                raise StopIteration
            country = self.countries[self.cursor]['name']['official'].replace(' ', '_')
            link_wiki = self.url + country
            with open('link_wiki.csv', 'a', encoding='utf-8') as file_csv:
                datawriter = csv.writer(file_csv, delimiter=',')
                datawriter.writerow([self.countries[self.cursor]['name']['official'], link_wiki])
            return self.cursor

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()


if __name__ == '__main__':
    with WikiIterate('countries.json', BASE_URL) as wiki_iter:
        while True:
            try:
                wiki_iter.__next__()
            except:
                print('Файл создан')
                break


