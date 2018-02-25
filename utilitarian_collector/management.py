import socket

import os

import sys

import errno

from utilitarian_collector.servers import run


def execute_from_cli(argv=None):

    #TODO: handle args so it is easy to set up on different addres and port!


    try:
        run('127.0.0.1', 4059, threading=True)

    except socket.error as e:
        # Use helpful error messages instead of ugly tracebacks.
        ERRORS = {
            errno.EACCES: "You don't have permission to access that port.",
            errno.EADDRINUSE: "That port is already in use.",
            errno.EADDRNOTAVAIL: "That IP address can't be assigned to.",
        }
        try:
            error_text = ERRORS[e.errno]
        except KeyError:
            error_text = e

        print("Error: %s" % error_text)
        # Need to use an OS exit because sys.exit doesn't work in a thread
        os._exit(1)

    except KeyboardInterrupt:
        sys.exit(0)


