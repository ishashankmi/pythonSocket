from threading import Thread;
import socket;
from time import sleep;
import argparse;
global sock;
def args():
	mx=argparse.ArgumentParser();
	mx.add_argument("-ht","--host",help="Host To Connect");
	mx.add_argument("-p","--port",help="Port to Bind");
	fval=mx.parse_args();
	if(fval.host and fval.port):
		global sock;
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		sock.connect((fval.host,int(fval.port)));
		print("\nConnected....\n");
		sta();
	else:
		print("Please provide proper values, type --help");

def send():
	while True:
		inp=input();
		enco=inp.encode('utf-8');
		si=str(len(inp)).encode("utf-8");
		if(inp=='quitx'):
			if(sock.send(si)):
				sleep(0.100);
				sock.send(enco);
				sock.close();
				break;
		elif(inp==''):
			continue;
		else:
			if(sock.send(si)):
				sleep(0.100);
				sock.send(enco);
def recv():
	while True:
		val=sock.recv(40).decode();
		if(int(val)>0):
			newval=str(sock.recv(int(val)).decode());
			if(newval=='quitx'):
				sock.close();
				break;
			else:
				print("=> "+newval);

def sta():
	t1=Thread(target=send);
	t2=Thread(target=recv);
	t1.start();
	t2.start();

if __name__=="__main__":
	try:
		args();
	except Exception as e:
		print(e);
