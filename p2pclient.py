import socket
from thread import *

def get_file(tracker):
	f_n = raw_input("\nEnter file name you want to access: ")
	conn.send(str(len(f_n)))
	if(conn.recv(100) == "OK"):
		conn.send(f_n)
	access()		
	p_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p_conn.connect((tracker[0], int(tracker[1]) + 1))
	filepath = raw_input(str("file(in server) : "))
	p_conn.send(filepath.encode())
	buf =p_conn.recv(1024).decode()
	if buf == 'file not found':
		print(buf)
		exit()
	new_file = raw_input(str("new file : "))
	file = open(new_file, 'wb')
	print(buf)
	file.write(buf)
	file.close()
	print("file has been received successfully")
	exit()
def transfer_file(port_t):
    print("Port number: {}".format(port_t))
    Psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Psocket.bind(('',port_t))
    Psocket.listen(5)
    c,ad = Psocket.accept()
    filename = c.recv(100).decode()
    try:
        file = open(filename , 'rb')
    except IOError:
        buf = "file not found"
        c.send(buf.encode())
        print("Error : cant find file")
	exit()
    else:
        file_data = file.read(1024)
	file_size = len(file_data)
     	print(file_data)
        c.send(file_data.encode())
        print("data has been transmitted")
	file.close()
	exit()

def server():
	a = 0
    	print('Welcome to P2P FILE Sharing Networking')
	t_l = conn.recv(100)
	conn.send("OK")
	print(conn.recv(100))
	f_name = raw_input("\nEnter: ")
	if(f_name == '-1'):
		t_l = len(f_name)
		conn.send(str(t_l))
		if(conn.recv(100) == "OK"):
			conn.send(f_name)
	else:
		t_l = len(f_name)
		conn.send(str(t_l))
		if(conn.recv(100) == "OK"):
			conn.send(f_name)
		while True:
			if (f_name == '-1'):
				break
			else:
				print("Enter -1 to stop")
				f_name = raw_input("Enter name: ")
				t_l = len(f_name)
		    		conn.send(str(t_l))
				if(conn.recv(100) == "OK"):
					conn.send(f_name)
	response = raw_input("\nEnter R to recv: ")
	t_l = len(response)
	conn.send(str(t_l))
	if(conn.recv(100) == "OK"):
		conn.send(response)
	if(response == "R"):
	    	start_new_thread(get_file(tracker),(tracker,))
	elif(response == "T"):
		t_l = conn.recv(100)
    		conn.send("OK")
    		pp = conn.recv(int(t_l))
    		port_t = int(pp) + 1
		print(port_t)
		start_new_thread(transfer_file(port_t),(port_t,))
def access():
	t_l = conn.recv(100)
	conn.send("OK")
	reply = conn.recv(int(t_l))
	conn.send("OK")
	if (reply != "ERROR!!"):
		r = conn.recv(100)
		global tracker
		tracker.insert(0,reply)
		tracker.insert(1,r)
		print("Connecting to {} peer".format(reply))

	else:
		exit()
conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = '10.30.7.69'
SPort = 12345
tracker = []
conn.connect((IP, SPort))
server()
