import requests
import hashlib
import sys


def req_api_data(char):
    url = "https://api.pwnedpasswords.com/range/"+char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def pswrd_count(hashes, hash_tail):
    hash_values = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hash_values:
        if h == hash_tail:
            return count
    return 0


def pwned_api_check(pswrd):
    shapassword = hashlib.sha1(pswrd.encode('utf-8')).hexdigest().upper()
    first5, last = shapassword[:5], shapassword[5:]
    response = req_api_data(first5)
    return pswrd_count(response, last)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count != 0:
            print(f"{password} was found {count} many times. change passwrd")
        else:
            print(f"{password} was found {count} many time. good passwrd")
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))