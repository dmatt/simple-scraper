from scrape import scrape

# Input some things for the site you want to scrape
keyword = 'butts'
paginator = '&sp={}'
url = 'https://www.loc.gov/search/?c=150&q={}&st=list'
parents = ('span', 'item-description-title')
child = ('a')

results = scrape(
  url,
  keyword,
  paginator,
  parents,
  child
)
for r in results:
  print(r, '\n')
print("Total results: ", len(results))

# Click run▸ in repl.it