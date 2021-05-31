from pprint import pprint


def fill_combo():
    nums = []
    for num in range(10):
        num = str(num).zfill(3)
        nums.append(num)
    print(nums)


def string_freq():
    strs = 'a b c a a a'
    word_list = strs.split()
    word_freq = [word_list.count(word) for word in word_list]
    result = list(zip(word_list, word_freq))
    pprint(result)


def get_google_top_news():
    from urllib.request import urlopen

    from bs4 import BeautifulSoup as soup

    news_url = "https://news.google.com/news/rss"
    with urlopen(news_url) as client:
        xml_page = client.read()
    soup_page = soup(xml_page, 'xml')
    news_list = soup_page.findAll('item')
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print('*' * 60)


get_google_top_news()
