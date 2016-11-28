#!/usr/bin/env python

import pygame
import dataformatter
import socket

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

UDP_IP = raw_input("IP: ")
UDP_PORT = int(raw_input("PORT: "))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            l3x = j.get_axis(0) * 128  # -128-128 range
            l3y = j.get_axis(1) * 128  # -128-128 range
            r3x = j.get_axis(2) * 128  # -128-128 range
            r3y = j.get_axis(3) * 128  # -128-128 range
            l2 = j.get_axis(12) * 256  # 0-256 range
            r2 = j.get_axis(13) * 256  # 0-256 range

            dataTranslator = dataformatter.JoystickDataPacketTranslator()
            dataTranslator.interpretDataString(dataTranslator.createDataString(l3x, l3y, r3x, r3y, l2, r2))
            dataString = dataTranslator.createDataString(l3x, l3y, r3x, r3y, l2, r2)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(dataString, (UDP_IP, UDP_PORT))
