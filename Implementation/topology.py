from spout import Spout
from bolt import Bolt
from cordinator import Cordinator
from thread import myThread
import threading
import time

spout1 = Spout(1, 'spout1', 0.2)
spout2 = Spout(2, 'spout2', 0.1)
spout3 = Spout(3, 'spout3', 0.5)
bolt1 = Bolt(1, 'bolt1', 32, 38)
bolt2 = Bolt(2, 'bolt2', 30, 35)
bolts = [bolt1, bolt2]

# Create new threads
thread1 = myThread(1, "Thread-1", spout1, bolt1, 0)
thread2 = myThread(2, "Thread-2", spout2, bolt1, 0)
thread3 = myThread(3, "Thread-3", spout3, bolt2, 0)
threads = [thread1, thread2, thread3]
cordinator = Cordinator(threads, 25)
x = threading.Thread(target=cordinator.calculate_load, args=(threads,))

# Start new Threads
thread1.start()
thread3.start()
x.start()
time.sleep(5)
thread2.start()
