import socket
import dataformatter

UDP_IP = "192.168.43.234"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
formatter = dataformatter.JoystickDataPacketTranslator()
while True:
    data, addr = sock.recvfrom(1024)
    formatter.interpretDataString(data)
    print formatter.l3x
    print formatter.l3y
    print formatter.r3x
    print formatter.r3y
    print formatter.l2
    print formatter.r2