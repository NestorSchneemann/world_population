import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig(f'./images/{name}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 140, 80]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)