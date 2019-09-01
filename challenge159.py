"""
You have 3 seconds to break this hash
Send the answer back using https://ringzer0ctf.com/challenges/159/[clear_text] 




----- BEGIN HASH -----
b96cf2e7cc90ac5179de2f720fc6aa07166b7862
----- END HASH -------
"""

import random,os,hashlib
import requests
import re

PHPSESSID = ''
WORDLIST_PATH = ''


def get_hash_str():
    cookies = {'PHPSESSID': PHPSESSID}
    r = requests.get('https://ringzer0ctf.com/challenges/159',  cookies=cookies)
    text = r.text.replace("<br />","")
    hash_pre = text.split("----- BEGIN HASH -----")[1]
    hash_str = hash_pre.split("----- END HASH -----")[0]
    regex = re.compile(r'[\n\r\t]')
    s = regex.sub("", hash_str)
    return s

def main():
    
    words = []
    myDict = {}
    with open(WORDLIST_PATH, 'r') as f :
        words = f.readlines()
        for word in words:
            hash_object = hashlib.sha1(str.encode(word))
            hex_dig = hash_object.hexdigest()
            myDict[hex_dig] = word[:-2]
    hash_str = get_hash_str().splitlines()[0]
    print(hash_str)
    print(myDict.get(hash_str))

main()

