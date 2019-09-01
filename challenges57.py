"""
You have 3 seconds to break this hash
Send the answer back using https://ringzer0ctf.com/challenges/57/[clear_text] 




----- BEGIN HASH -----
ae85ae8ed2cd9427922c1dbf7aba3425a77cc46c
----- END HASH -----

----- BEGIN SALT -----
be314c7d24fc3ebf41d738d9f288e6a73cb7a7b5eec4aa2edc9fa88bd3369b04
----- END SALT -----
"""

import requests
import re
import json
import hashlib

PHPSESSID = ''
WORDLIST_PATH = ''

with open(WORDLIST_PATH, 'r') as f :
    words = f.read()
    salt = b'55f55417741248f16eeb6ae86e2b4e8fdc61d607b77f5c83dc9381ee9ea2dc6b'

    for word in words:
        
        hashed = has
        hlib.pbkdf2_hmac('sha1',word.encode(),salt,1)
        print(hashed)

cookies = {'PHPSESSID': PHPSESSID}
r = requests.get('https://ringzer0ctf.com/challenges/126',  cookies=cookies)
text = r.text.replace("<br />","")
hashb = text.split("----- BEGIN WORDS -----")[1]
hashe= hashb.split("----- END WORDS -----")[0].replace(" ","")
hash = re.sub(r'\W+', '',hashe )

saltb = text.split("----- BEGIN SALT -----")[1]
salte= saltb.split("----- END SALT -----")[0].replace(" ","")
salt = re.sub(r'\W+', '',salte )

print(hash,salt)