- http://lartc.org/lartc.html#LARTC.QDISC
- http://www.voidcn.com/article/p-dcbuqhml-bkt.html
- https://wiki.linuxfoundation.org/networking/ifb
- http://blog.csdn.net/eydwyz/article/details/53085690
# example
## tc in use
```
. /etc/profile
# https://wiki.linuxfoundation.org/networking/ifb
# http://blog.csdn.net/eydwyz/article/details/53085690
# 15.8.2. The actual script (CBQ)
# start ifb1
modprobe ifb || exit 1
ip link set dev ifb1 up
# outgress/dequeue
tc qdisc del dev em1 root
tc qdisc add dev em1 root handle 1: tbf rate 99mbit burst 128000 latency 50ms
# ingress
tc qdisc del dev em1 ingress
tc qdisc add dev em1 handle ffff: ingress
# ingress function too slowly
#tc qdisc add dev em1 parent ffff: protocol ip prio 50 u32 match ip src \
#   0.0.0.0/0 police rate 50mbit burst 10k drop flowid :1
# redirect ingress to egress
tc filter add dev em1 parent ffff: protocol ip prio 10 u32 match u32 0 0 flowid 1:1 action mirred egress redirect dev ifb1
# for fib
tc qdisc del dev ifb1 root
tc qdisc add dev ifb1 root handle 1: tbf rate 99mbit burst 128000 latency 50ms
tc -s qd sh dev em1
tc -s qd sh dev ifb1
```
## iptables package ctr
```
# not always true
# http://ptallrights.blog.51cto.com/11151122/1841911
#3conn ~100
#-A INPUT -p tcp -m tcp --sport 80 -m limit --limit 3400/s --limit-burst 70 -j ACCEPT
# all ~100
#-A INPUT -p tcp -m tcp --sport 80 -m limit --limit 1300/s --limit-burst 31 -j ACCEPT
#-A INPUT -p tcp -m tcp --sport 80 -j DROP
# http://ptallrights.blog.51cto.com/11151122/1841911
# ~100Mb
#-A OUTPUT -p tcp -m tcp -m limit --limit 3300/s --limit-burst 80 -j ACCEPT
#-A OUTPUT -p tcp -m tcp  -j DROP
# add --limit-burst make the reverst affect???
#20.10
``` 

# show
    tc -s qd sh dev eth1
# del
    tc qd del dev eth1 root
# rate
Just to prevent confusion, tc uses the following rules for bandwith specification:

mbps = 1024 kbps = 1024 * 1024 bps => byte/s
mbit = 1024 kbit => kilo bit/s.
mb = 1024 kb = 1024 * 1024 b => byte
mbit = 1024 kbit => kilo bit.
Internally, the number is stored in bps and b.
But when tc prints the rate, it uses following :

1Mbit = 1024 Kbit = 1024 * 1024 bps => byte/s

# Simple, classless Queueing Disciplines
only reschedule, delay or drop it

## pfifo_fast
- First In, First Out
- low band firstly
- TOS to band
- To set the queue length to 10, execute: ifconfig eth0 txqueuelen 10

## Token Bucket Filter
- shape with tokens, the data in Bucket(buffer), clear when tokens avild; buffer full, drop
- your first choice if you simply want to slow an interface down
- logic
  - data_rate == tokens_rate: passes the queue without delay
  - data_rate < tokens_rate: short data bursts occur
  - data_rate == tokens_rate: throttle data for a while(limit or latency), drop after that
- tokens correspond to bytes, not packets
- tc qd add dev eth1 root handle 1: tbf rate 99mbit burst 128000 latency 50ms 
- params
  - limit or latency: waiting (in limit $bytes or latency $timeout) for tokens to become available, or drop
  - burst/buffer/maxburst: If your buffer is too small, packets may be dropped because more tokens arrive per timer tick than fit in your bucket.(Intel ref: 10mbit/s <--> 10kbyte)
  - mpu: The Minimum Packet Unit determines the minimal token usage for a packet.64 bytes for ethernet
  - rate: limits rate
  - ???


### Stochastic Fairness Queueing (SFQ)
- SFQ is only useful in case your actual outgoing interface is really full! If it isn't then there will be no queue on your linux machine and hence no effect
- it has an algorithm which divides traffic over a limited number of queues using a hashing algorithm
- SFQ changes its hashing algorithm quite often so that any two colliding sessions will only do so for a small number of seconds
- tc qdisc add dev ppp0 root sfq perturb 10
- params:
  - perturb: Reconfigure hashing once this many seconds. If unset, hash will never be reconfigured. Not recommended. 10 seconds is probably a good value.
  - quantum: Amount of bytes a stream is allowed to dequeue once(d~: MTU)
  - limit: limit Amount of package a time, drop if exceeded

### wait to continue
