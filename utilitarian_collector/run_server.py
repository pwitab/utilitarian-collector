from socketserver import UDPServer

from utilitarian_collector.handlers import BaseDLMSHandler
from utilitarian_collector.servers import run, UDPRequestHandler

if __name__ == "__main__":
    #os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')
    run('127.0.0.1', 4059, UDPRequestHandler, UDPServer, threading=True)
