import getpass
import telnetlib

HOST = '192.168.56.109'

print("Successful in making socket")

port = 23

print("Successfully bind socket in port: " + str(port))

user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

print('Telnet Connected to the Client Host')
tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

