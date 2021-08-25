from requests import get
from json import loads



def random_quote(): 
  response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
  quote = ('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))
  return quote