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

## zeromq 的几种模式

- Request-Reply 模式（请求响应模型）
- Publish-Subscribe 模式（发布订阅模型）
- Parallel Pipeline 模式（管道模型）

### Request-Reply 模式（请求响应模型）

客户端在请求后，服务端必须回响应

![img](https://i.loli.net/2021/06/04/QKUfEjOMwLsFnqh.png)

服务端：

```python
import zmq
import sys
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    try:
        print("wait for client ...")
        message = socket.recv()
        print("message from client:", message.decode('utf-8'))
        socket.send(message)
    except Exception as e:
        print('异常:',e)
        sys.exit()
```

客户端：

```python
import zmq
import sys
context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
while True:
    input1 = input("请输入内容：").strip()
    if input1 == 'b':
        sys.exit()
    socket.send(input1.encode('utf-8'))

    message = socket.recv()
    print("Received reply: ", message.decode('utf-8'))
```



> 参考资料
>
> [Python zmq的三种简单模式 - Mr_Yun - 博客园 (cnblogs.com)](https://www.cnblogs.com/yunwangjun-python-520/p/10777375.html)
