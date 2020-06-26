from __future__ import division
from __future__ import print_function

import os
import socket
import sys
import time

from absl import app
from absl import flags
from absl import logging

FLAGS = flags.FLAGS

flags.DEFINE_string('name', os.getenv('MINECRAFT_SERVER_NAME'), 'Server name.')
flags.DEFINE_integer('port', os.getenv('MINECRAFT_SERVER_PORT'), 'Server port.')
flags.DEFINE_float('interval_seconds', 1.0, 'Advertise interval in seconds.')


def main(argv):
  del argv  # Unused.
  BROADCAST_IP = '224.0.2.60'
  BROADCAST_PORT = 4445

  if not FLAGS.name:
    logging.fatal('Missing required --name or MINECRAFT_SERVER_NAME environment variable.')

  if not FLAGS.port:
    logging.fatal('Missing required flag --port or MINECRAFT_SERVER_PORT environment variable.')


  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  logging.info('Advertising Minecraft server "%s" on port %d.', FLAGS.name,
               FLAGS.port)
  logging.info('Advertise interval: %f seconds', FLAGS.interval_seconds)

  message = str.encode('[MOTD]%s[/MOTD][AD]%d[/AD]' % (FLAGS.name, FLAGS.port))
  while True:
    try:
      sock.sendto(message, (BROADCAST_IP, BROADCAST_PORT))
      time.sleep(FLAGS.interval_seconds)
    except:
      logging.info('Shutting down.')
      break


if __name__ == '__main__':
  app.run(main)
