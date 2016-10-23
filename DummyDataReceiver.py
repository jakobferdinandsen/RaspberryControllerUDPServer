import socket
import dataformatter

UDP_IP = raw_input("IP: ")
UDP_PORT = int(raw_input("PORT: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
formatter = dataformatter.JoystickDataPacketTranslator()
while True:
    data, addr = sock.recvfrom(1024)
    formatter.interpretDataString(data)
    print formatter.l2