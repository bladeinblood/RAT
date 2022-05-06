import pyautogui
import socket
import webbrowser
import os

print('Hello dear developer, it is your RAT')
logon = input('')

if logon == 'blade in blood':
  print('Well, it is you, heh kek')
  
  command = input('')
  
  if command == 'screenshot':
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)


if command == 'open':
    print('Сколько сайтов? Можно только 2')
    
    url_chislo = input('')

    if url_chislo == '1':
        url1 = input('url: ')

        webbrowser.open(url1)

    if url_chislo == '2':
        url1 = input('url: ')
        url2 = input('url: ')
        
        webbrowser.open(url1)
        webbrowser.open(url2)
        
    with open('sites.txt', 'w') as file:
        file.write(url1 + ' opened\n')
        file.write(url2 + ' opened\n')

command = input('')

def scan_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if client.connect_ex((ip, port)):
        pass
    else:
        print(f"Порт {port} открыт")
    
inputip = input()
ip = socket.gethostbyname(inputip)
for i in range(100):
    scan_port(ip, i)



if command == 'scan_port':
    scan_port()
  
  
else:  
  print('Bye')
