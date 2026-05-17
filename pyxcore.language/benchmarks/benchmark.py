
import time
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
t=time.time(); fib(20); print("benchmark:", time.time()-t)
