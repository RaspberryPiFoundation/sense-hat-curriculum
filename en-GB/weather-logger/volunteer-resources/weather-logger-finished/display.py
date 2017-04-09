import pygal

temp = []

file = open('weather.txt', 'r')

for line in file.read().splitlines():
  if line:
    temp.append( float(line) )
file.close()

weatherchart = pygal.Line()
weatherchart.title = 'Weather'
weatherchart.x_labels = range(1, len(temp) + 1)
weatherchart.add('temp', temp)
weatherchart.render()

