import time
from prometheus_client import Counter, start_http_server
my_counter = Counter('my_counter_total', 'A useful help string.')

def my_function():
    my_counter.inc()

start_http_server(8000)
while True:
    my_function()
    time.sleep(5)