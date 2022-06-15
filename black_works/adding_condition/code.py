#!/usr/bin/env python3

counter = 2

# создавать протокол при написании комадны /changePriceList

something = ['for something', 'for another']
conditions = ''

query = input('Example => \n<text>\n: ')
if query and query != '':
  counter += 1
  something.append(query)

for k in range(0, counter):
  conditions += '{}) {}\n'.format(k+1, something[k])

print(conditions)
  
