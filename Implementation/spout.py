# Data forwarding nodes
import uuid
import threading
import time
import random


class Spout:
    def __init__(self, spout_id, name, WAIT_TIME_SECONDS):
        self.spout_id = spout_id
        self.bolt_id = -1
        self.name = name
        self.WAIT_TIME_SECONDS = WAIT_TIME_SECONDS

    def generate_Data(self):
        return (round(random.uniform(30, 40), 2))

    def set_bolt(self, bolt):
        self.bolt_id = bolt.bolt_id
