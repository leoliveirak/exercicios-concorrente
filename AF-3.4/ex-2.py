from time import sleep
from random import randint
from threading import Thread, Semaphore

def produtor():
  global buffer
  for i in range(10):
    sleep(randint(0,2))           # fica um tempo produzindo...
    item = 'item ' + str(i)

    sem_vazio.acquire()
    buffer.append(item)
    print('Produzido %s (ha %i itens no buffer)' % (item,len(buffer)))
    sem_cheio.release()

def consumidor():
  global buffer
  for i in range(10):

    sem_cheio.acquire()
    item = buffer.pop(0)
    print('Consumido %s (ha %i itens no buffer)' % (item,len(buffer)))
    sem_vazio.release()
    
    sleep(randint(0,2))         # fica um tempo consumindo...

buffer = []
tam_buffer = 3

sem_cheio = Semaphore(0)
sem_vazio = Semaphore(tam_buffer)

prod = Thread(target=produtor) 
cons = Thread(target=consumidor) 
prod.start()
cons.start()
prod.join()
cons.join() 