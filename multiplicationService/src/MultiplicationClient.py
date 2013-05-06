#!/usr/bin/env python

import sys
sys.path.append('../gen-py')

from tutorial import MultiplicationService
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = MultiplicationService.Client(protocol)

  # Connect!
  transport.open()

  product = client.multiply(4,5)
  print '4*5=%d' % (product)
  

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)
