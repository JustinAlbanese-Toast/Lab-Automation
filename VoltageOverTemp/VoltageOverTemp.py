import pyvisa
import time
from F4t_control import (F4TController, RampScale, TempUnits)
import csv

# create the resource manager
rm = pyvisa.ResourceManager()

# instantiate the unit
x = F4TController(host='172.16.52.26',timeout=1)

# list the devices available on network
print(rm.list_resources())

# Choose our equipments address and open a connection
Keysight_34461 = rm.open_resource('TCPIP0::A-34461A-00000.local::inst0::INSTR')

# print out the device info
print(Keysight_34461)

# IDN query prints out device info such as manufacturer or serial number
print(Keysight_34461.query('*IDN?'))

# reset the device
Keysight_34461.write("*rst; status:preset; *cls")

interval_in_ms = 500
number_of_readings = 10
Keysight_34461.write("status:measurement:enable 512; *sre 1")
Keysight_34461.write("conf:volt:DC auto, 0.003")
Keysight_34461.write('FORM:DATA:ASCII,4')
# Keysight_34461.write("sample:count %d" % number_of_readings)
Keysight_34461.write("trigger:source bus")
# Keysight_34461.write("trigger:delay %f" % (interval_in_ms / 1000.0))
# Keysight_34461.write("trace:points %d" % number_of_readings)
Keysight_34461.write("trace:feed sense1; trace:feed:control next")
Keysight_34461.write("initiate")
Keysight_34461.assert_trigger()
time.sleep(1)
currenttime = time.strftime('%H:%M:%S')
voltage = Keysight_34461.query('fetch?')
temp = x.get_temperature(cloop=1)
print(Keysight_34461.query('fetch?'))
print(x.get_temperature(cloop=1))
with open('DataDump.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([currenttime, temp, voltage.strip()])
    file.close


Keysight_34461.write("trace:clear; trace:feed:control next")
Keysight_34461.write("*rst; status:preset; *cls")
rm.close