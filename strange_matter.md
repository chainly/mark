1. use huawei_router to nat OUTER_IP:9999 to INNER_IP:ANY_PORT failed (tcp send/send_ack/ack good
  , but client can send data(GET / ...) and server blocked at socket.recv(),
  then rest/final good!!!, no firewall!, see: [server_packages_capture](./aaa)).Still unkown!!!

2. `msg` is overwrite when `Exception` occurred, and delete after getting out of `except` block
```
# python3
msg = 'sdfsdf'
try:
    1/0
except Exception as msg:
    pass
print(msg)
NameError: name 'msg' is not defined
```
