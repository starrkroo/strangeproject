#!/usr/bin/env python3

increaseEarning = 10

items = {'starrk': 13, 'another_user': 36}

from time import ctime
print(ctime().split(' ')[3])

def counting():
  global increaseEarning
  while True:
    if ctime().split(' ')[3] == '14:36:00':
      for k in items.values():
        print(k + increaseEarning)
      break

if __name__ == '__main__':
  counting()
