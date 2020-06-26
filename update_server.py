#!/usr/bin/python3

import urllib.request
from html.parser import HTMLParser
import os
import pickle

VERSION_FILE = 'version.pickle'
SERVER_BINARY = 'server.jar'


class Parser(HTMLParser):
  _data = {}

  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      for key, value in attrs:
        if key == 'href' and value.endswith('.jar'):
          self._data['url'] = value

  def handle_data(self, data):
    if data.startswith('minecraft_server') and data.endswith('.jar'):
      self._data['filename'] = data

  def Get(self):
    return self._data


def main():
  previous = None
  if os.path.exists(VERSION_FILE):
    with open(VERSION_FILE, 'rb') as f:
      previous = pickle.load(f)

  parser = Parser()
  with urllib.request.urlopen(
      'https://www.minecraft.net/en-us/download/server') as f:
    parser.feed(f.read().decode('utf-8'))

  current = parser.Get()
  if current != previous or not os.path.exists(SERVER_BINARY):
    urllib.request.urlretrieve(current['url'], SERVER_BINARY)
    if previous == None or 'filename' not in previous:
      print('Updated to %s' % current['filename'])
    else:
      print('Updated from %s to %s' %
            (previous['filename'], current['filename']))
  else:
    print('%s already up to date.' % current['filename'])

  with open(VERSION_FILE, 'wb') as f:
    pickle.dump(current, f)


if __name__ == '__main__':
  main()
