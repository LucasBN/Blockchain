import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def get_chain():
    URL = "http://192.168.1.226:5000/chain"
    r = requests.get(URL)
    data = r.json()
    print('\n------------------------------------------------------------------------\n\n')
    for block in data['chain']:
        print(block)
    print('\n\n------------------------------------------------------------------------\n')


def mine():
    URL = "http://192.168.1.226:5000/mine"
    r = requests.get(URL)
    data = r.json()
    print('\n------------------------------------------------------------------------\n\n')
    print(data['message'])
    print('\n\n------------------------------------------------------------------------\n')

def new_transaction():

    url = 'http://192.168.1.226:5000/transactions/new' # Set destination URL here
    post_fields = {
	   'sender': 'lucas',
       'recipient': 'olvier',
       'amount': 10
    }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)

while True:
    print('What would you like to do? ')
    option = input()
    if option == "chain":
        get_chain()
    if option == "mine":
        mine()
    if option == "add transaction":
        #print('Sender: ')
        #sender = input()
        #print('Recipient: ')
        #recipient = input()
        #print('amount: ')
        #amount = input()
        new_transaction()
