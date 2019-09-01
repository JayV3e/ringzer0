"""
RingZer0 Team Online CTF
Number game (rewrited by TheIndian):
Please, guess 10 numbers (between 0 to 10000) in less than 30 seconds.
number>
"""

import pexpect,time

hostname = "challenges.ringzer0team.com"
username = "number"
password = "Z7IwIMRC2dc764L"
port = 10130
PROMPT = 'number>'

child = pexpect.spawn(f'ssh {username}@{hostname} -p {port}')
child.expect("number@challenges.ringzer0team.com's password:")
child.sendline(password)
child.expect("number>",timeout=1)

def check_number(n,minimum_number,maximum_number):
    print(f"checking {n}")
    child.sendline(str(n))
    try:
        child.expect("number>number>",timeout=1)
        response= str(child.before).split('too ')[1].split("\\")[0]
    except:
        child.expect("number>",timeout=1)
        print(child.before)
        check_number(5000,0,10000)
    print(response)
    if response == "big":
        number_too_big(n,minimum_number,maximum_number)
    if response == "small":
        number_too_small(n,minimum_number,maximum_number)


def number_too_big(n,minimum_number,maximum_number):
    maximum_number = n
    print(f'{minimum_number} vs {maximum_number}')
    new_number = maximum_number - ((maximum_number - minimum_number) / 2)
    check_number(int(new_number),minimum_number,maximum_number)

def number_too_small(n,minimum_number,maximum_number):
    minimum_number = n
    print(f'{minimum_number} vs {maximum_number}')
    new_number = minimum_number + ((maximum_number - minimum_number) / 2)
    check_number(int(new_number),minimum_number,maximum_number)

check_number(5000,0,10000)
print(f"checking {n}")
child.sendline(str(n))
child.expect("number>",timeout=1)
print(child.before)
response= str(child.before).split('too ')[1].split("\\")[0]
print(response)
if response == "big":
    number_too_big(n,minimum_number,maximum_number)
if response == "small":
    number_too_small(n,minimum_number,maximum_number)
if "Game" in child.before:
    check_number(5000,0,1000)
else:
    print('oops')
    print(child.before)
    child.close()
child.close()


