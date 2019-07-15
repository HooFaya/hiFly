import threading
import time
class my_thread(threading.Thread):
    def __init__(self,thread_ID,name,counter):
        threading.Thread.__init__(self)
        #super(my_thread,self).__init__()
        self.threadID=thread_ID
        self.name=name
        self.counter=counter
    def run(self):
        print("开始线程："+self.name)
        print_time(self.name,self.counter,5)
        print("结束线程" +self.name)


def print_time(threadName,delay,counter):
    while(counter):
        time.sleep(delay)
        print("{}:{}".format(threadName,time.ctime(time.time())))
        counter-=1


thread1=my_thread(1,"thread-1",1)
thread2=my_thread(2,"thread-2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
