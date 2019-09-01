"""
You have 2 second identify the shuffled words and send the whole correct list using comma as delimiter.
Send the answer back using https://ringzer0ctf.com/challenges/126/[string] 




----- BEGIN WORDS -----
slugabeds,catalepsies,noirymdm,semanticist,liutglacir,falsifiable,crossties
----- END WORDS -----
"""

import random,os
import requests

PHPSESSID = ''
WORDLIST_PATH = ''
answer = []
wordlist = {}

with open(WORDLIST_PATH, 'r') as f:
    for line in f:
        if len(line[:-1]) not in wordlist:
            wordlist[len(line[:-1])] = set()
        wordlist[len(line[:-1])].add(line[:-1])

def get_words():
    cookies = {'PHPSESSID': PHPSESSID}
    r = requests.get('https://ringzer0ctf.com/challenges/126',  cookies=cookies)
    text = r.text.replace("<br />","")
    word_pre = text.split("----- BEGIN WORDS -----")[1]
    words = word_pre.split("----- END WORDS -----")[0][4:-4]
    words = words.split(',')
    print(words)
    return words

def shuffle_word(word):
    chars = list(word)
    random.shuffle(chars)
    return ''.join(chars)

def check_word(word):
    if word in wordlist:
        answer.append(word)
        return True
    else:
        return False

def main():
    words = get_words()
    for word in words:
        print(word)
        if word in wordlist[len(word)]:          
            answer.append(word)
        else:
            print('everyday im shuffling')
            while True:
                shuffled_word = shuffle_word(word)
                if shuffled_word in wordlist[len(word)]:          
                    answer.append(shuffled_word)
                    break

    answer_str = ','.join(answer)
    print(answer_str)
    cookies = {'PHPSESSID': PHPSESSID}
    url = f'https://ringzer0ctf.com/challenges/126/{answer_str}'
    r = requests.post(url,  cookies=cookies)
    print(r.text)
    
main()