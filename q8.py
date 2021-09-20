import threading
import time

def print_thread(ptr):
        lock = threading.Lock()
        lock.acquire()
        print (ptr)
        time.sleep(1)
        lock.release()

class cointingThread(threading.Thread):
        def __init__(self,num_start):
                threading.Thread.__init__(self)
                self.daemon=True
                self.start_num=num_start

        def run(self):
                while self.start_num>0:
                        print_thread(str(self.getName())+":"+str(self.start_num))
                        self.start_num=self.start_num-1
                        

print ('\--------')
th1=cointingThread(10)
th2=cointingThread(10)
th1.start()
time.sleep(1)
th2.start()


