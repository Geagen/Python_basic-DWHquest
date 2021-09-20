import threading
import time

def print_thread(ptr,lock):
        lock.acquire()
        try:
                print (ptr)
                
        finally:
                lock.release()

class cointingThread(threading.Thread):
        def __init__(self,num_start,lock):
                threading.Thread.__init__(self)
                self.daemon=True
                self.start_num=num_start

        def run(self):
                while self.start_num>0:
                        time.sleep(1)
                        print_thread(str(self.getName())+":"+str(self.start_num),lock)
                        self.start_num=self.start_num-1
                        
                        
print ('\--------')
lock = threading.Lock()
th1=cointingThread(10,lock)
th1.start()
th2=cointingThread(10,lock)
th2.start()


