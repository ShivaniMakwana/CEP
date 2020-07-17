# Data forwarding nodes
import uuid
import threading
import time
import random
from api import data_collection


class Spout:
    def __init__(self, spout_id, name, WAIT_TIME_SECONDS, bolt_list):
        self.spout_id = spout_id
        self.bolt_id = -1
        self.name = name
        self.WAIT_TIME_SECONDS = WAIT_TIME_SECONDS
        self.load = 1/WAIT_TIME_SECONDS
        self.bolt_list = bolt_list

    def generate_Data(self):
        return data_collection()

    def set_bolt(self, bolt):
        self.bolt_id = bolt.bolt_id

    def del_bolt(self, bolt):
        self.bolt_list.remove(bolt)
