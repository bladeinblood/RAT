import pyautogui

print('Hello dear developer, it is your RAT')
logon = input('')

if logon == 'blade in blood':
  print('Well, it is you, heh kek')
  
  command = input('')
  
  if command == 'screenshot':
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)
    
  
  
else:  
  print('Bye')
