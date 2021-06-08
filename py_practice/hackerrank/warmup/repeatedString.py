from math import ceil

s = input()
n = int(input().strip())


def repeatedString(string, n):
    # Write your code here
    if string.count('a') == 0:
        print(0)
        return
    freq = dict()
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    x = n // len(string)
    for value in freq:
        freq[value] = freq[value] * x
    result = freq['a'] + len([a for a in s[:n % len(string)] if a == 'a'])
    print(result)


repeatedString(s, n)
