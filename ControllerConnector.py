#!/usr/bin/env python

import pygame
import dataformatter
import socket

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

l2Calibrated = False
r2Calibrated = False
calibrated = False

UDP_IP = "192.168.10.168"
UDP_PORT = "5555"

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            l3x = j.get_axis(0) * 128  # -128-128 range
            l3y = j.get_axis(1) * 128  # -128-128 range
            r3x = j.get_axis(2) * 128  # -128-128 range
            r3y = j.get_axis(3) * 128  # -128-128 range
            l2 = (j.get_axis(12) + 1) * 128  # 0-256 range
            r2 = (j.get_axis(13) + 1) * 128  # 0-256 range

            if l2 == -1.0 and not (l2Calibrated):
                l2Calibrated = True
            if r2 == -1.0 and not (r2Calibrated):
                r2Calibrated = True

            if r2Calibrated and l2Calibrated and not (calibrated):
                calibrated = True

            dataTranslator = dataformatter.JoystickDataPacketTranslator()

            dataTranslator.interpretDataString(dataTranslator.createDataString(l3x, l3y, r3x, r3y, l2, r2))

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(dataTranslator.createDataString(l3x, l3y, r3x, r3y, l2, r2), (UDP_IP, UDP_PORT))
