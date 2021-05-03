# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging

import grpc

import route_guide_pb2
import route_guide_pb2_grpc


def guide_get_one_feature(stub, point):
    """获取一个坐标的信息

    :param stub: [description]
    :type stub: [type]
    :param point: [description]
    :type point: [type]
    """
    # 同步
    # feature_future = stub.GetFeature(point)
    # 异步
    feature_future = stub.GetFeature.future(point)
    feature = feature_future.result()
    if not feature.location:
        print("Server returned incomplete feature")
        return

    if feature.name:
        print("Feature called %s at %s" % (feature.name, feature.location))
    else:
        print("Found no feature at %s" % feature.location)


def guide_get_feature(stub):
    """根据坐标返回相应的信息

    :param stub: [description]
    :type stub: [type]
    """
    guide_get_one_feature(
        stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906))
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print("-------------- GetFeature --------------")
        guide_get_feature(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
