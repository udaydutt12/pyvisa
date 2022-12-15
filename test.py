import pyvisa as visa
import socket

try:
  rm = visa.ResourceManager() 
  dev = 'GPIB0::9::INSTR'
  session = rm.open_resource(dev)
  print('\n Open Successful!')
  print('IDN:' +str(session.query('*IDN?')))
  #session.baud_rate = 57600
  #session.read_termination = '\n'
  #session.write_termination = '\n'
  print('CP?:', session.write('CP?'))

except Exception as e:
  print('[!] Exception:' +str(e))