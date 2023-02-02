import pyvisa
import time

# create the resource manager
rm = pyvisa.ResourceManager()

# Choose our digital multimeter address and open a connection
Keysight_34461 = rm.open_resource('TCPIP0::A-34461A-00000.local::inst0::INSTR')
Keysight_34461.write("status:measurement:enable 512; *sre 1")
Keysight_34461.write("conf:volt:DC auto, 0.003")
Keysight_34461.write("trigger:source bus")
Keysight_34461.write("trace:feed sense1; trace:feed:control next")
Keysight_34461.write("initiate")
Keysight_34461.assert_trigger()
time.sleep(1)
print(Keysight_34461.query('fetch?'))
Keysight_34461.write("trace:clear; trace:feed:control next")
Keysight_34461.write("*rst; status:preset; *cls")


