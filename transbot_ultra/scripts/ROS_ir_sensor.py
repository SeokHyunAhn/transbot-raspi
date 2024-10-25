#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Bool

# GPIO setup
pins = [2, 3, 4, 17, 27]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize ROS node
rospy.init_node('ir_sensor_publisher')
pub = rospy.Publisher('/ir_sensor_state', Bool, queue_size=10)

booooool = False

# Main loop
while not rospy.is_shutdown():
    state_out = []
    time.sleep(1)
    
    for pin in pins:
        state_in = GPIO.input(pin)
        state_out.append(state_in)
    
    # Print the sensor states as a list
    print(f"Sensor states: {state_out}")

    results = sum(state_out)
    # White = 1, Black = 0
    print(f"Sum of sensor states: {results}")

    if results <= 3:
        booooool = True
    else:
        booooool = False
    
    # Publish only if booooool is True
    if booooool:
        rospy.loginfo("Publishing True to /ir_sensor_state topic")
        pub.publish(booooool)
