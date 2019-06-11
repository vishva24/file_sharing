import socket
import sys
import select
from thread import *

h = []
tracker = []
a = 0
list_of_files = []
def clientThread(conn, addr):
	a1 = "Enter file names you would like to share(enter -1 if not any)\n"
	t_l = len(a1)
	conn.send(str(t_l))
	buf = conn.recv(100)
	if(buf == "OK"):
		conn.send(a1)
	t_l = conn.recv(100)
	conn.send("OK")
	buf = conn.recv(int(t_l))
	global a
	global list_of_files
	global h
	global tracker
	tracker.insert(a,addr)
	if buf == '-1':
	  	pass
	else:
		while True:
			list_of_files.append(buf)
	   		t_l = conn.recv(100)
	    		conn.send("OK")
	    		f_name = conn.recv(int(t_l))
	    		if (f_name == "-1"):
				break
			else:
	    			list_of_files.append(f_name)
		h.insert(a,list_of_files)
		list_of_files = []
	 	a += 1
	print("Client thread")
	t_l = conn.recv(100)
	conn.send("OK")
	response = conn.recv(int(t_l))
	if (response == 'R'):
	 	print("Wants to access files")
		length = conn.recv(100)
		conn.send("OK")
		b = conn.recv(int(length))
		if b:
	    		access(conn,b)
	    	conn.close()
	elif(response == 'T'):
		t_l = len(str(tracker[a - 1][1]))
		conn.send(str(t_l))
		if(conn.recv(100) == "OK"):
			conn.send(str(tracker[a - 1][1]))
		conn.close()

def access(conn, b):
	peer = find_file(b)
	if (peer != -1):
		print("Sending data of {} peer ".format(tracker[peer]))
		t_l = len(str(tracker[peer]))
		conn.send(str(100))
		if(conn.recv(100) == "OK"):
			conn.send(str(tracker[peer][0]))
			conn.recv(100)
			conn.send(str(tracker[peer][1]))
	else:
		conn.send(str(len("ERROR!!")))
		if(conn.recv(100) == "OK"):
			conn.send("ERROR!!")
def find(ad):
    for i in tracker:
        if (i == ad):
            	return i
    return -1

def find_file(b):
    for i in range(len(h)):
	for j in h[i]:
		print(j)
    		if (j == b):
                	return i
    return -1

Psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Psocket.bind(('', 12345))
Psocket.listen(5)
a = 0
while True:
    conn, addr = Psocket.accept()
    print("{} connect".format(addr))
    start_new_thread(clientThread,(conn, addr))
