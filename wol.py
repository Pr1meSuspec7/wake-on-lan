from wakeonlan import send_magic_packet
# dest mac-address, source-interface
#
# networklab
# send_magic_packet('70.f3.95.01.4a.4f', interface='192.168.178.31')
#
# pve
send_magic_packet('64.00.6a.73.44.d9', interface='192.168.178.31')