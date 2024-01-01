from wakeonlan import send_magic_packet
# dest mac-address, source-interface
send_magic_packet('70.f3.95.01.4a.4f', interface='192.168.178.31')