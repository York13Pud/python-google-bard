# --- Import the required libraries:
from bardapi import Bard
import keyring


# --- Get the token from Apple KeyChain:
TOKEN = keyring.get_password("Google Bard", "Google Bard")


# --- Initialise an instance of Bard that uses the above token:
bard = Bard(token = TOKEN)


# --- Make a request to Google Bard with a question:
response = bard.get_answer("Please provide me with an 'hello world' program that is written in objective-c and swift")


# --- Show the content of the response, a.k.a the answer:
print(response["content"])