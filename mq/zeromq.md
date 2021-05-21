# zeromq 的使用

## 入门

zeromq 的简单使用

安装：`pip install zmq`

一个简单的服务端：

```python
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    message = socket.recv()
    print(f'Received request: {message}')

    time.sleep(1)
    socket.send(b'hello world')
```

一个简单的客户端：

```python
import zmq

context = zmq.Context()

print('Connecting to hello world server...')
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print(f'Sending request {request} ...')
    socket.send(b'Hello World from client')

    # get the reply
    message = socket.recv()
    print(f'Received reply {request} [ {message} ]')
```
