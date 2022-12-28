import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('./world_population.csv')
  countries, percentage = utils.percentage_by_country_v2(data)
  charts.generate_pie_chart(countries, percentage)
  
if __name__ == '__main__':
  run()