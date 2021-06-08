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

def target_combination():
    import itertools
    from functools import partial

    X = [10, 20, 20, 20]
    Y = [10, 20, 30, 40]
    Z = [10, 30, 40, 20]
    target = 70

    def check_sum_array(N, *nums):
        if sum(nums) == N:
            return (True, nums)
        else:
            return (False, nums)

    pro = itertools.product(X,Y,Z)
    func = partial(check_sum_array, target)
    sums = list(itertools.starmap(func, pro))

    result = set()
    for s in sums:
        if s[0] == True:
          result.add(s[1]) 
    pprint(result)

def letter_combinations():
    from itertools import product

    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    digit_string = '47'
    items = list()
    for digit in digit_string:
        items.append(string_maps[digit])
    combinations = product(*items)
    pprint([c for c in combinations])


print(*[3,5])
