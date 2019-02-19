from test5 import send_greeting
from test5 import add_new_user

def test_send_valid_greeting():
 expected = 'Thank you Mr.William Gates'
 assert send_greeting("William Gates") == expected

def test_send_invalid_greeting():
 assert send_greeting("William Gates") != 'invalid greeting!'

def test_add_new_valid_user():
 assert add_new_user("Paul Allen", "800,000", "3", "400000") == {"Name": "Paul Allen", "Total": "800,000",
                                                                 "Gift Number": "3", "Average": "400000"}

def test_add_new_invalid_user():
 assert add_new_user("Paul Allen", "800,000", "3", "400000") != {"Name": "Paul Allen", "Total": "500,000",
                                                                 "Gift Number": "2", "Average": "100000"}