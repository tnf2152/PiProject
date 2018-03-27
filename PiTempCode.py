# This is the python code that is being used in the Pi Temperature Project.
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices'
device_folder = glob.glob(base_dir +28*)[0]
device_file = device_folder + '/w1_slave'

# These 3 different variables point to the location of sensor data.

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

# The read_temp function must return YES in the first line, this means there is a line with the temperature.

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
    if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      temp_f = temp_c * 9.0 / 5.0 + 32.0
      return temp_c, temp_f
    
    # This converts the number to Celsius and Fahrenheit temperature.
    
    while True:
      print(read_temp())
      time.sleep(1)
      
      # This prevents the def read_temp from going into a continuous loop by putting the script to sleep for a second every time it is read.
      
