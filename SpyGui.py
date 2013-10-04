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
import Tkinter 
import tkMessageBox
from Tkinter import * 
import os
import sys

root = Tk()
root.minsize(400,100) 
root.geometry("300x100")
root.title("iMessage Spy") 

def spy():
   cmd = 'python imessagegrabber.py'
   os.system(cmd)
   os.system('clear')
   cmd2 = 'open messages.txt'
   os.system(cmd2)
   os.system('exit')
   sys.exit()

L = Label(root, text="Later the spy, you find all messages in the document message.txt. \n", font=("Helvetica", 12))

z = Label(root, text="\n ", font=("Helvetica", 1)) 

B = Tkinter.Button(root, text ="Spy", command=spy, width=30) 

z.pack()
L.pack()
B.pack() 
root.mainloop()
