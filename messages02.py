import multiprocessing

def worker(q):
    message = q.get()
    print('Got message %s ' % message)

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    message = {'source': 'c', 'name': 'testing', 'timeout': .03}

    queue.put(message)

    queue.close()
    queue.join_thread()
    p.join()
