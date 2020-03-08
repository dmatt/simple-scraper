import requests
import re
from bs4 import BeautifulSoup

def paginate_responses(url, paginator):
  page = 1
  next = True
  responses = []
  while next:
    resp = get_response(url+paginator.format(page))
    if resp.status_code == 200:
      responses.append(resp)
      page += 1
    else:
      next = False
  return responses

def get_response(url):
  resp = requests.get(url)
  return resp

def get_text(responses):
  text = ''
  for r in responses:
    text += r.text
  return text

def get_soup(text):
  return BeautifulSoup(text, 'html.parser')

def pretty_print(soup):
  print(soup.prettify())

def request_to_soup(url, paginator):
  responses = paginate_responses(url, paginator)
  text = get_text(responses)
  soup = get_soup(text)
  return soup

def strip_spaces(string):
  return re.sub('\s+',' ', string)

def scrape(
  url,
  keyword,
  paginator,
  parents,
  child
):
  soup = request_to_soup(url.format(keyword), paginator)
  parents = soup.find_all(*parents)
  children = [strip_spaces(p.find(*child).text) for p in parents]
  return children
