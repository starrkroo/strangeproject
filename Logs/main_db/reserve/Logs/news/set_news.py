#!/usr/bin/env python3

# kkeys

from os import getcwd

VERSION    = input("Enter new version: ")
KOINS_NAME = 'KvantoKoins {}'.format(VERSION)

file = 'information_about_news.txt'

news = []
print("Enter news:\n\n----------------------------- ")
while True:
  try:
    conf = input()
  except KeyboardInterrupt:
    break
  news.append(conf)
  del conf

with open(file, 'a') as f:
  f.write('\n{}\n{}\n{}'.format('='*30, KOINS_NAME, '='*30))
  string = ''
  for k in news:
    f.write('\n\n----->\t{}'.format(k))

print('{}/../current_version/version.py'.format(getcwd()))

with open('{}/../current_version/version.py'.format(getcwd()), 'w') as f:
  f.write('VERSION = "{}"'.format( KOINS_NAME ))

