def get_population():
  keys = ['col', 'bol']
  values = ['300', '400']
  return keys, values


def data_by_country(data, country):
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  return result


def population(dict):
  poblacion = {}
  for i in dict:
    if 'Population' in i:
      if i != 'World Population Percentage':
        j = i.replace(' Population', '')
        poblacion[j] = int(dict[i])
  labels = list(poblacion.keys())
  labels.reverse()
  values = list(poblacion.values())
  values.reverse()
  return labels, values


def countries_by_continent(data):
  continent = input('Escribe el continente de interes: ')
  countries = []
  for i in range(len(data)):
    if data[i]['Continent'] == continent:
      countries.append(data[i]['Country/Territory'])
  return countries


def percentage_by_country(data):
  countries = []
  percentage = []
  for i in data:
    countries.append(i['Country/Territory'])
    numero = float(i['World Population Percentage'])
    percentage.append(numero)
  return countries, percentage

def percentage_by_country_v2(data):
  percentage_dict = {item['Country/Territory']: item['World Population Percentage'] for item in data}
  countries = percentage_dict.keys()
  percentages = percentage_dict.values()
  return countries, percentages