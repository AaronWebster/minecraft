#!/usr/bin/python3

import urllib.request
from html.parser import HTMLParser
import os
import dbus
import re
import pickle

VERSION_FILE = 'version.pickle'
SERVER_BINARY = 'server.jar'


def ReadConfig(filename=None):
    config = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith('#'):
                key, value = line.strip().partition('=')[::2]
                config[key] = value
    return config


def BroadcastMessage(message):
    sysbus = dbus.SystemBus()
    systemd1 = sysbus.get_object('org.freedesktop.systemd1',
                                 '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
    for unit in manager.ListUnits():
        unit_name = str(unit[0])
        if re.match('minecraft@.*.service', unit_name):
            service = sysbus.get_object(
                'org.freedesktop.systemd1', object_path=manager.GetUnit(unit_name))
            interface = dbus.Interface(
                service, dbus_interface='org.freedesktop.DBus.Properties')
            config = ReadConfig(os.path.join(interface.Get(
                'org.freedesktop.systemd1.Service', 'WorkingDirectory'), 'server.properties'))
            os.system('/usr/local/bin/mcrcon -P %s -p "M#necraftRkon" "say %s"' %
                      (config['rcon.port'], message))


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
            BroadcastMessage(
                'Server updated to %s. Restart imminent.' % current['filename'])
        else:
            BroadcastMessage('Server updated from %s to %s.  Restart imminent.' % (
                previous['filename'], current['filename']))

    with open(VERSION_FILE, 'wb') as f:
        pickle.dump(current, f)


if __name__ == '__main__':
    main()
