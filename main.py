import utils

data = [
  {
    'Country': 'Colombia',
    'Population': '50 millones'
  },
  {
    'Country': 'Bolivia',
    'Population': '30 millones'
  }
]

def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  print(utils.A)

  country = input('elige un pais: ')
  result = utils.population_by_country(data, country)
  print(result)

if __name__ == '__main__':
  run()