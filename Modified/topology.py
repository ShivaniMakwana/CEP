from spout import Spout
from bolt import Bolt
from thread import myThread
import threading
import time

bolt1 = Bolt(1, 'bolt1', 32, 38, 8)
bolt2 = Bolt(2, 'bolt2', 30, 35, 8)
bolts = [bolt1, bolt2]

spout1 = Spout(1, 'spout1', 0.2, bolts)
spout2 = Spout(2, 'spout2', 0.25, bolts)
spout3 = Spout(3, 'spout3', 0.5, [bolt2])

# Create new threads
thread1 = myThread(1, "Thread-1", spout1, bolt1)
thread2 = myThread(2, "Thread-2", spout2, bolt1)
thread3 = myThread(3, "Thread-3", spout3, bolt2)
threads = [thread1, thread2, thread3]

# Start new Threads
thread1.start()
thread3.start()

time.sleep(5)
thread2.start()
