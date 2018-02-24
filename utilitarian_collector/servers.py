import logging
import socketserver
import threading

from dlms_cosem.wrappers import UDPWrapper

from utilitarian_collector.handlers import BaseDLMSHandler

logger = logging.getLogger(__name__)


class UDPRequestHandler(socketserver.BaseRequestHandler):

    _amr_handler_cls = BaseDLMSHandler

    def handle(self):
        data = self.request[0]
        cur_thread = threading.current_thread()
        print(
            "Received Datagram in in thread {} from {}:{} :".format(
                cur_thread.name,
                self.client_address[0],
                self.client_address[1],
            )
        )
        udp_wrapper = UDPWrapper.from_bytes(data)
        handler = self._amr_handler_cls(udp_wrapper.dlms_data)
        handler.process_data()


def run(address, port, handler, server_cls, threading=False):
    server_address = (address, port)

    if threading:
        print('Threaded server')
        amr_server_cls = type('AMRServer', (socketserver.ThreadingMixIn, server_cls), {})
    else:
        amr_server_cls = server_cls

    print(amr_server_cls)

    server = amr_server_cls(server_address, UDPRequestHandler)

    if threading:
        server.daemon_threads = True

    print('Running server on {0}:{1}'.format(address, port))
    server.serve_forever()

