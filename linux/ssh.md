```
(python36) ➜  ~ ssh -p 27351 root@xxx.xxx.xxx.xxx
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:VVNvvEK0gVfz2ed2mtjBHfXmzBHegkN8cQ/Wi0TznZk.
Please contact your system administrator.
Add correct host key in /Users/chengcong/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/chengcong/.ssh/known_hosts:1
RSA host key for [xxx.xxx.xxx.xxx]:27351 has changed and you have requested strict checking.


# reset keys
(python36) ➜  ~ ssh-keygen -R '[xxx.xxx.xxx.xxx]:27351'
# Host [xxx.xxx.xxx.xxx]:27351 found: line 1
/Users/chengcong/.ssh/known_hosts updated.
Original contents retained as /Users/xxx/.ssh/known_hosts.old

# retry
(python36) ➜  ~ ssh -p 27351 root@xxx.xxx.xxx.xxx
The authenticity of host '[xxx.xxx.xxx.xxx]:27351 ([xxx.xxx.xxx.xxx]:27351)' can't be established.
RSA key fingerprint is SHA256:VVNvvEK0gVfz2ed2mtjBHfXmzBHegkN8cQ/Wi0TznZk.
Are you sure you want to continue connecting (yes/no)?
```
