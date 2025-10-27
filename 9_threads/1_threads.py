# Threads:

# Exemplo da receita de bolo:
# 1 pessoa fazendo e 2 pessoas fazendo.

import threading

def task1():
    x = 0
    while x < 10:
        print("- Task 01")
        x+=1

def task2():
    y = 0
    while y < 10:
        print("+ Task 02")
        y+=1

# threading.Thread(target=task1).start()
# task2()

# THREAD 01:

    # Concept about thread.

# THREAD 02:


"""
import _thread
import time

def print_message(name, delay, limit):
    count = 0
    while count < limit:
        time.sleep(delay)
        count += 1
        print(name, "----------", time.time())

try:
    _thread.start_new_thread(print_message, ("thread 01", 2, 3))
    _thread.start_new_thread(print_message, ("thread 02", 1, 3))
    input() # necessario para roda corretamente.
except:
    print("Error threading.")
"""

# THREAD 03:

"""
import threading
import time

def print_message(name, delay, limit):
    count = 0
    while count < limit:
        time.sleep(delay)
        count += 1
        print(name, "----------", time.time())

try:
    if __name__ == "__main__":
        t1 = threading.Thread(target=print_message, args={"thread01", 2, 3})
        t2 = threading.Thread(target=print_message, args={"thread02", 2, 3})
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Done!")
except:
    print("Error threading.")
"""

# THREAD 04:

# usando classe

"""
import threading
import time

def print_message(name, delay, limit):
    cont = 0
    while cont < limit:
        cont += 1
        time.sleep(delay)
        print(f"{name} --------- {time.time()}")

class MyThreadClass(threading.Thread):
    def __init__(self, name, delay, limit):
        threading.Thread.__init__(self) # chamando o construtor da classe acima
        self.name = name
        self.delay = delay
        self.limit = limit

    def run(self):
        print(f"{self.name} started.")
        print_message(self.name, self.delay, self.limit)
        print(f"{self.name} ended.")

if __name__ == "__main__":
    t1 = MyThreadClass("thread01", 2, 3)
    t2 = MyThreadClass("thread02", 1 ,3)
    t1.start()
    t2.start()

    # propriedades da thread e do objeto de thread:

    # OBJECT
    print(f"NAME T1: {t1.getName()}")
    print(f"NAME T2: {t2.getName()}")

    # GERAL
    print(f"COUNT: {threading.active_count()}")
    print(f"CURRENT THREAD: {threading.current_thread()}")
    print(f"ENUMERATE: {threading.enumerate()}")

    t1.join()
    t2.join()
    print("Done!")
"""

# THREAD 05:

# Syncronization

import threading

x = 0

def unlock_task():
    global x
    for i in range(1000000):
        x += 1

def lock_task(lock):
    global x
    for i in range(1000000):
        lock.acquire()
        x += 1
        lock.release()

def main_task():
    opc = 1 
    t1 = None 
    t2 = None
    if opc == 2:
        # Assyncronized
        t1 = threading.Thread(target=unlock_task)
        t2 = threading.Thread(target=unlock_task)
    else:
        # Syncronized
        lock = threading.Lock()
        t1 = threading.Thread(target=lock_task, args=(lock, ))
        t2 = threading.Thread(target=lock_task, args=(lock, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print(f"RESULT: {x}")
    print("Done!")


# ----------------------
    
import threading
import time

def print_message(name, delay, limit):
    i = 0
    while i < limit:
        print(f"{name}: {time.time()}")
        time.sleep(delay)
        i += 1
    print(f"{name} is done!")

t1 = threading.Thread(target=print_message, args=("Thread 01", 1, 5))
t2 = threading.Thread(target=print_message, args=("Thread 02", 4, 5))
t3 = threading.Thread(target=print_message, args=("Thread 03", 3, 5))

t3.start()
t1.start()
t2.start()

t3.join()
t1.join()
t2.join()

# ----------------------------------------------------


import time
import _thread

def Sleeping():
    print("Aguardando...")
    sleep(3)
    print("Passaram-se 3 segundos.")

def funcao(thread_name, thread_delay):
    count = 0
    while count < 10:
        time.sleep(thread_delay)
        count += 1
    print("\nThread: %s -- Terminada: %s" % (thread_name, time.ctime(time.time()))) 

def IniciarThread():
    _thread.start_new_thread(funcao, ("Thread-01", 3,))
    _thread.start_new_thread(funcao, ("Thread-02", 1,))
    _thread.start_new_thread(funcao, ("Thread-03", 5,))
    _thread.start_new_thread(funcao, ("Thread-04", 2,))
    _thread.start_new_thread(funcao, ("Thread-05", 0,))
    _thread.start_new_thread(funcao, ("Thread-06", 4,))

#Sleeping()
IniciarThread()


import time
import threading

# ----------------------------------------------------

def CountDown(*args):
    i = 10
    for i in range (10, 0, -1):
        print("THREAD #01: %d" %(i))
        time.sleep(1)
    print("\n\nTHREAD #01 completo!!!")

def CountUp(*args):
    i = 0
    for i in range (0, 10, 1):
        print("\n\nTHREAD #02: %d" %(i))
        time.sleep(1)
    print("THREAD #02 completo!!!")
   
t1 = threading.Thread(target=CountDown())
t2 = threading.Thread(target=CountUp())   
# CountDown()
# CountUp() 
t1.start()
t2.start()


# ----------------------------------------------------

from collections.abc import Callable
from typing import Any, Iterable, Mapping


def example_01():
    import _thread
    import time

    def greeting(name, *args):
        print(f"Hello, {name}!")

    name = "Anderson"
    _thread.start_new_thread(greeting, (name, None))
    time.sleep(0.1) # senao, nao aperece o resultado da ação da thread.

# example_01()

def example_02():

    import threading
    import time

    def run(name, delay, limit):
        for i in range(0, limit):
            print(f"{name}[{i+1}] - {time.time()} ")
            time.sleep(delay)
        print(f"{name} finished!")

    t1 = threading.Thread(target=run, args=("thread_01", 2, 10))
    t2 = threading.Thread(target=run, args=("thread_02", 3, 10))
    t3 = threading.Thread(target=run, args=("thread_03", 1, 10))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    
# example_02()


def example_03():

    import threading
    import time

    def execution(name, delay, limit):
        for i in range(0, limit):
            print(f"{name}[{i+1}]: {time.time()}")
            time.sleep(delay)
     

    class MyThread(threading.Thread):

        def __init__(self, name, delay, limit):
            threading.Thread.__init__(self)
            self.name = name
            self.delay = delay
            self.limit = limit

        def run(self):
            print(f"{self.name} started!")
            execution(self.name, self.delay, self.limit)
            print(f"{self.name} terminated!")
    
    t1 = MyThread("thread-01", 2, 10)
    t2 = MyThread("thread-02", 3, 10)
    t3 = MyThread("thread-03", 1, 10)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    time.sleep(4)
    print("main_thread is done!")
    
# example_03()


def example_04():

    import threading
    import time

    def execution(name, delay, limit):
        for i in range(0,limit):
            print(f"{name}[{i + 1}] -- {time.time()}")
            time.sleep(delay)
    
    class MyThread(threading.Thread):
    
        def __init__(self, name, delay, limit):
            threading.Thread.__init__(self)
            self.name = name
            self.delay = delay
            self.limit = limit

        def run(self):
            print(f"{self.name} started!")
            execution(self.name, self.delay, self.limit)
            print(f"{self.name} terminated!")


    t1 = MyThread("thread_01", 1, 10)
    t2 = MyThread("thread_02", 0.25, 10)
    t3 = MyThread("thread_03", 0.5, 10)

    opc = 0
    if opc == 1:
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()    
    else:
        t1.start()
        t2.start()
        t3.start()
        time.sleep(2)
        print("main_thread terminated!")

# example_04()

# scheduling

def example_05():

    import time
    import threading
    
    def print_time():
        print(f"current_time: {time.ctime(time.time())}")

    t = threading.Timer(3, print_time, args=())
    t.start()
    t.join()
    print(f"finished in {time.ctime(time.time())}")
  
# example_05()

def example_06():
   
   import time
   import sched

   def print_thread(name):
       print(f"{name}: {time.ctime(time.time())}")
   
   scheduler = sched.scheduler(time.time, time.sleep)
   print(f"started in : {time.ctime(time.time())}")
   scheduler.enter(3, 5, print_thread, ("EVENT_01", ))
   scheduler.enter(2, 1, print_thread, ("EVENT_02", ))
   scheduler.run()
   print(f"finished in: {time.ctime(time.time())}")
 
# example_06()

def example_07():
   
   import time
   import sched

   def print_thread(name):
       print(f"{name}: {time.ctime(time.time())}")
   
   scheduler = sched.scheduler(time.time, time.sleep)
   print(f"started in : {time.ctime(time.time())}")
   scheduler.enter(3, 5, print_thread, ("EVENT_01", ))
   scheduler.enter(2, 1, print_thread, ("EVENT_02", ))
   scheduler.run()
   print(f"finished in: {time.ctime(time.time())}")
 
# example_07()

def example_08():
   
    import time
    import sched

    scheduler = sched.scheduler(time.time, time.sleep)

    def print_time(current_event):
        print(f"{current_event}: {time.ctime(time.time())}")

    for i in range(5):
        scheduler.enter(i + 1, 1, print_time, (f"EVENT_{i + 1}",))

    print(f"START : {time.ctime(time.time())}")
    scheduler.run()
    print(f"FINISH: {time.ctime(time.time())}")

# example_08()

def example_09():

   import time
   from multiprocessing.dummy import Pool 

   def print_thread(name):
       print(f"{name}: {time.ctime(time.time())}")
       time.sleep(1)

   threads = []
   for i in range(0,7):
       threads.append(f"threads_0{i+1}")
   
   pool = Pool(1)
   pool.map(print_thread, threads)
   pool.close()

   pool = Pool(3)
   pool.map(print_thread, threads)
   pool.close()

   pool = Pool(6)
   pool.map(print_thread, threads)
   pool.close()

# example_09()

def example_10():
    
    import time
    from multiprocessing.dummy import Pool

    def print_thread(name):
        print(f"{name}: {time.ctime(time.time())}")
        time.sleep(0.5)

    threads=[]
    for i in range(0,7):
        threads.append(f"thread_0{i+1}")

    pack = [1,3,6]
    for i in pack:
        print(f"\n\n{i} por vez:")
        pool = Pool(i)
        pool.map(print_thread, threads)
        pool.close()
 
# example_10()

    
def example_11():
    
    import time
    from concurrent.futures import ThreadPoolExecutor

    def print_thread(name):
        print(f"{name}: {time.ctime(time.time())}")
        time.sleep(0.5)

    threads=[]
    for i in range(0,7):
        threads.append(f"thread_0{i+1}")

    pack = [1,3,6]
    for i in pack:
        print(f"\n\n{i} por vez:")
        tpool = ThreadPoolExecutor(i)
        tpool.map(print_thread, threads)
 
# example_11()

def example_12():

    def print_current_thread():
        import threading
        print(threading.current_thread())  
    
    print_current_thread()
 
example_12()

def example_12():

    import threading

    def func(delay):
        if threading.current_thread() is threading.main_thread():
            print("main_thread!")
        else:
            print("background_thread!")

    t = threading.Thread(target=func, args=(2,))
    t.start()
    func(1)
 
# example_12()


def example_13():

    import threading
    import time

    def execution(name, delay, limit, priority):
        time.sleep(1.0 * priority)
        for i in range(0,limit):
            print(f"{name}[{i+1}]")
            time.sleep(delay)

    class MyThread(threading.Thread):

        def __init__(self, name, delay, limit, priority):
            super().__init__()
            self.name = name
            self.delay = delay
            self.limit = limit
            self.priority = priority

        def run(self):
            print(f"{self.name} started .")
            execution(self.name, self.delay, self.limit, self.priority)
            print(f"{self.name} finished.")


    t1 = MyThread("thread_01", 1, 10, 3)
    t2 = MyThread("thread_02", 1, 10, 1)
    t3 = MyThread("thread_03", 1, 10, 2)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

# example_13()
    
def example_14():

    import threading
    import time

    def execution(name, delay, limit, priority):
        time.sleep(1.0 * priority)
        for i in range(0,limit):
            print(f"{name}[{i+1}]")
            time.sleep(delay)

    class MyThread(threading.Thread):

        def __init__(self, name, delay, limit, priority):
            super().__init__()
            self.name = name
            self.delay = delay
            self.limit = limit
            self.priority = priority

        def run(self):
            print(f"{self.name} started .")
            execution(self.name, self.delay, self.limit, self.priority)
            print(f"{self.name} finished.")


    t1 = MyThread("thread_01", 1, 10, 3)
    t2 = MyThread("thread_02", 1, 10, 1)
    t3 = MyThread("thread_03", 1, 10, 2)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

# example_14()


def example_15():

    import threading
    import time

    my_lock = threading.Lock()

    def task(name, opc):
        my_lock.acquire()
        print(f"{name} started .")
        time.sleep(2)
        print(f"{name} finished.")
        my_lock.release()

    t1 = threading.Thread(target=task, args=("thread_01", 1))
    t2 = threading.Thread(target=task, args=("thread_02", 2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

# example_15()

def example_16():
    
    import threading
    import time

    my_lock = threading.Lock()

    def task(name, opc):
        with my_lock: 
            print(opc)
            print(f"{name} started .")
            time.sleep(2)
            print(f"{name} finished.")

    t1 = threading.Thread(target=task, args=("thread_01", 1))
    t2 = threading.Thread(target=task, args=("thread_02", 2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

# example_16()

def example_17():

    import threading
    import time

    semaphore = threading.Semaphore(2)

    def execution(name, delay, limit):
        with semaphore:
            for i in range(0,limit):
                print(f"{name}[{i + 1}] -- {time.time()}")
                time.sleep(delay)
        
    class MyThread(threading.Thread):
    
        def __init__(self, name, delay, limit):
            threading.Thread.__init__(self)
            self.name = name
            self.delay = delay
            self.limit = limit

        def run(self):
            print(f"{self.name} started!")
            execution(self.name, self.delay, self.limit)
            print(f"{self.name} terminated!")


    t1 = MyThread("thread_01", 1, 10)
    t2 = MyThread("thread_02", 0.25, 10)
    t3 = MyThread("thread_03", 0.5, 10)

    opc = 0
    if opc == 1:
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()    
    else:
        t1.start()
        t2.start()
        t3.start()
        time.sleep(2)
        print("main_thread terminated!")

example_17()

# syncronization 

import threading

x = 0

def unlock_task():
    global x
    for i in range(10000000):
        x+=1

def lock_task(lock):
    global x
    for i in range(10000000):
        lock.acquire()
        x+=1
        lock.release()
    
def main_task():
    opc = 1
    t1 = None
    t2 = None
    if opc == 2:
        t1 = threading.Thread(target=unlock_task)
        t2 = threading.Thread(target=unlock_task)
    else:
        lock = threading.Lock()
        t1 = threading.Thread(target=lock_task, args=(lock,))
        t2 = threading.Thread(target=lock_task, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print(f"RESULT: {x}")
    print("done!")





