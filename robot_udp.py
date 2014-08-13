import socket
import array

UDP_IP = "127.0.0.1"
UDP_PORT = 1995

def udp_test(speed, direction):
    msg = (array.array('b', [speed,direction])).tostring()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg, (UDP_IP, UDP_PORT))

def main():
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "Sending (10,20) to server."
    udp_test(10,20)
    return 0

if __name__ == '__main__':
    main()
