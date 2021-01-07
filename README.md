# BackdooR321 0.1

![캡처](https://user-images.githubusercontent.com/51448912/103857190-5a7aad00-50f9-11eb-84da-d7777ce6e472.PNG)

이 프로그램은 윈도우용 컴퓨터 원격 제어 프로그램으로, Python과 Pyinstaller를 사용해 작성되었습니다.
소켓과 윈도우 프로그래밍을 활용해 제작되었으며, 소켓들을 딕셔너리에 저장해 다양한 컴퓨터를 한번에 제어할수 있게 설계되어있습니다.

This program is a computer remote controller program for window by using Python and Pyinstaller.
It's developed by utilizing Socket, Windows Programming and It's designed to store many sockets in a dictionary so it can controll various computers.

# Installation

기본적으로 설치되어야 있어야 하는 프로그램들을 다음과 같습니다.

* Python 3.x 

* Ngrok (같은 디렉토리에 넣어주세요.)


+ ```git clone https://github.com/R32191/BackdooR321-0.1.git```
+ ```cd BackdooR321-0.1.git```
+ ```python -m pip install -r requirements.txt```
+ ```start setup.py```

Reqirements : 

* Python 3.x 

* Ngrok (In the same directory)


+ ```git clone https://github.com/R32191/BackdooR321-0.1.git```
+ ```cd BackdooR321-0.1.git```
+ ```python -m pip install -r requirements.txt```
+ ```start setup.py```

# Features

* Simple Command List:
    1. cd [Folder Name] - Change directory
    2. ls - Print file list
    3. mkdir - Make Directory
    4. @[cmd_command] - Execute some cmd command
    5. $[cmd_command] - Print output after executing input command
    6. screenshot - Store screenshot file
    7. txt -r [file_name] - Read text file
    8. txt -w [file_name] - Write data in the text file
    9. download [file_name] - Downloading files
    10. upload [file_name] - Uploading files
    11. msg - Generate Error Message
    12. cls or clear - clear the screen
    13. help - Print Command List
    14. beep [hz] [time len] - Generate beep sound
    15. exit - exit

* Webcam Hacking Command List:
    1. webcam -c - Capture Webcam Videos with windows
    2. webcam -c -h - Capture Webcam Videos with no windows
    3. webcam -p - Capture Webcam Picture with windows
    4. webcam -p -h - Capture Webcam Picture with no windows
    
* Setting Command List:
    1. set - setting screen
    2. set color [option] - set color

# Warning
* 본 프로그램은 오직 교육, 학습 목적으로만 사용해야하며 악용할시 발생하는 법적 책임은 책임지지 않습니다.
* This program is for educational and learning purposes only, and we are not responsible for any legal liability in case of abuse.
