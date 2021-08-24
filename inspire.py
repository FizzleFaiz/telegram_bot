from requests import get
from json import loads

response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')


def random_quote(): 
  quote = ('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))
  return quote