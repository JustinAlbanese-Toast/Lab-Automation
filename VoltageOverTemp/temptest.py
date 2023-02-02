from F4t_control import (F4TController, RampScale, TempUnits)
import time

# setup a temperature sweep profile
temp_units = TempUnits['C']
start = 40                  #starting temperature
stop = 50                   #stopping temperature 
step = 1                    #Degree increase per step   
ramp_time_min = 2.0
soak_time_min = 1.0
temps = range(start,stop+step,step)

# instantiate the environmental chamber
x = F4TController(host='172.16.52.26', port=5025, timeout=1)
print(x.get_id())
print(x.get_temperature())
# configure unit for sweeping temperature
x.set_ramp_time(ramp_time_min)
x.set_ramp_scale(RampScale.MINUTES)
# ensure chamber is enabled:
x.set_output(1,'ON')
# ensure units 
x.set_units(temp_units)

for temp in temps:
    print('ramping to temperature {}'.format(temp))
    x.set_temperature(temp)
    # wait for ramp time to finish
    #time.sleep(ramp_time_min*60)
    time.sleep(1)
    x._clear_buffer()
    while abs(float(x.get_temperature()) - temp) > 0.2:
        time.sleep(1.0)
    # begin soak
    print('beginning soak at temp ' + x.get_temperature())
    time.sleep(soak_time_min*60)

# turn off unit
print('completed sweep!')
x.set_output(1,'OFF')
x.set_temperature(22)
# cleanup for socket connection is handled automatically