基于http2.0,实现client与server全双工

客户端是websocket协议，服务端也要设置成websocket协议
connect阶段client发送连接请求，根据该请求，server给予正确的应答即可
如果server端不是基于websocket，则会报错，如下是报了HandshakeError
aiohttp.client_exceptions.WSServerHandshakeError: 200, message='Invalid response status'

由于lock那边没有server支持，所以该部分代码并没有通过测试，停在了connect阶段