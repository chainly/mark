# send sock
import multiprocessing
from multiprocessing import reduction
import socket
import time

def worker(q, i):
    logging.info(q,i)
    f, args = q.get()
    s = f(*args)
    s.sendall(b'GET /\r\n\r\n')
    result = s.recv(100)
    print(result)    
    s.close()

def main():
    manager = multiprocessing.Manager()
    p = multiprocessing.Pool(processes=2)
    q = manager.Queue()
    lock = manager.Lock()
    for i in range(1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.baidu.com', 80))
        q.put(reduction._reduce_socket(s))
        print(q,i,s)
        
        p.apply_async(worker, args=(q, i), error_callback=lambda r: print(r))
    p.close()
    p.join()
    
if __name__ == '__main__':
    import logging
    l = multiprocessing.get_logger()
    l.setLevel(logging.DEBUG)
    main()
