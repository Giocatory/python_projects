from abc import ABCMeta, abstractmethod
import socket


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass
    
    @abstractmethod
    def close(self):
        pass


class SocketStream(IStream):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def read(self):
        self.sock.connect((self.host, self.port))
        return self.sock.recv(1024)
    
    def write(self, data):
        self.sock.send(data)
    
    def close(self):
        self.sock.close()
    


connect  = SocketStream('164.132.206.181', 28015)
print(connect.read())
connect.close()