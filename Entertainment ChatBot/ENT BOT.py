import requests
import bs4

def findFormat(lst, word):
    for i, v in enumerate(lst):
        if word in v:
            index = lst[i].find(word)
            return index
        else:
            return-1

class Movie():
    genre_lst = []
    def __init__(self):
        m_Title = soup.find('title')
        title = m_Title.text
        title = title[:len(title)-18]

        m_Genre = soup.find('div', class_="media-body").ul
        m_Genre = str(m_Genre.find_all('a'))
        m_Genre = m_Genre.split(',')
        m_genre_index = findFormat(m_Genre, 'genres=')
        m_genre_index_limit = findFormat(m_Genre, 'a>')
        while m_genre_index != -1:
            m_genre_str = str(m_Genre)
            print(m_genre_str[m_genre_index + 12:m_genre_index_limit])
            m_Genre = m_Genre[1:]
            self.genre_lst.append(m_genre_str)
            m_genre_index_limit = findFormat(m_Genre, 'a>')
            m_genre_index = findFormat(m_Genre, 'genres=')

        self.genre = self.genre_lst
        self.title = title

res = requests.get('https://www.rottentomatoes.com/m/rockos_modern_life_static_cling').text
soup = bs4.BeautifulSoup(res, 'lxml')
the_great_hack = Movie()


#print(findFormat(m_Genre, 'genres='))
print(the_great_hack.genre)
print(the_great_hack.title)
#print(the_great_hack.genre)
