from threading import Thread;
import socket;
from time import sleep;
import argparse;
data='';
def args():
	mx=argparse.ArgumentParser();
	mx.add_argument("-ht","--host",help="Host to Create, ex:- 127.0.0.1");
	mx.add_argument("-p","--port",help="Port to bind");
	fval=mx.parse_args();
	if(fval.host and fval.port):
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		print("Listening.....\n");
		sock.bind((fval.host,int(fval.port)));
		sock.listen(3);
		global data;
		data,add=sock.accept();
		print("Connected.....\n");
		sta();
	else:
		print("Please Provide Proper Values, Type --help");

def send():
	while True:
		inp=input();
		if(inp=='quitx'):
			sock.close();
			break;
		elif(inp==''):
			continue;
		else:
			enco=inp.encode('utf-8');
			si=str(len(inp)).encode('utf-8');
			if(data.send(si)):
				sleep(0.100);
				data.send(enco);
	sock.close();
def recv():
	while True:
		val=data.recv(40).decode();
		if(int(val)>0):
			newval=str(data.recv(int(val)).decode());
			if(newval=="quitx"):
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
		
