import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('./world_population.csv')
  continent = input('Escribe el nombre del continente de tu interes ')
  data = list(filter(lambda item: item['Continent'] == continent, data))
  countries, percentage = utils.percentage_by_country_v2(data)
  charts.generate_pie_chart(continent, countries, percentage)
  
if __name__ == '__main__':
  run()