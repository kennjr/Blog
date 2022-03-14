import urllib.request
import json


class Quote:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author


def get_random_quote():
    rand_quote_url = "http://quotes.stormconsultancy.co.uk/random.json"

    with urllib.request.urlopen(rand_quote_url) as url:
        #  we use the url.read() fun to read the response and store it in the var get_movies_data
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote = get_quote_response["quote"]
        author = get_quote_response["author"]

        quote = Quote(quote, author)

    return quote
