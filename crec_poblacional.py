import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('./world_population.csv')
  country = input('Ingrese el nombre del país de interés: ')
  info_pais = utils.data_by_country(data, country)
  print(info_pais)
  
  if len(info_pais) > 0:
    country = info_pais[0]
    labels, values = utils.population(country)
    charts.generate_bar_chart(labels, values)
    
if __name__ == '__main__':
  run()