# gRPC

## 概览

In gRPC, a client application can directly call a method on a server application on a different machine as if it were a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just a client in some languages) that provides the same methods as the server.

在 gRPC 中，客户机应用程序可以直接调用不同机器上的服务器应用程序上的方法，就好像它是一个本地对象一样，这使您更容易创建分布式应用程序和服务。与许多 RPC 系统一样，gRPC 基于定义服务的思想，指定可以通过参数和返回类型远程调用的方法。在服务器端，服务器实现这个接口并运行一个 gRPC 服务器来处理客户机调用。在客户端，客户端有一个存根(在某些语言中称为客户端) ，它提供与服务器相同的方法。

![grpc](https://grpc.io/img/landing-2.svg)

## 安装

这里的python版本为 `3.6.12` ，通过pipenv进行安装：

``` sh
pipenv install grpcio == 1.37.0
pipenv install grpcio-tools == 1.37.0
```

运行示例代码：

``` sh
cd gRpc/examples/helloworld
# 运行服务端
python greeter_server.py
# 运行客户端
python greeter_client.py
```

生成代码：

``` sh
cd gRpc/examples/helloworld
python -m grpc_tools.protoc -I ./ --python_out . --grpc_python_out . ./helloworld.proto
```
