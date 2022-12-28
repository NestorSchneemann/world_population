import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('./world_population.csv')
  countries = utils.countries_by_continent(data)
  density = {}
  for country in countries:
    info_pais = utils.data_by_country(data, country)
    dens_country = float(info_pais[0]['Density (per km²)'])
    density[country] = dens_country

  labels = density.keys()
  values = density.values()  
  charts.generate_bar_chart(labels, values)
  
if __name__ == '__main__':
  run()