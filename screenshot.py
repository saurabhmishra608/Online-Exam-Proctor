import random
import numpy as np
import cv2
import pyautogui
import time
i = 0

while True:
    t= 20
   
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
  
    s = np.random.choice([True, False], p=[0.3, 0.7])    
    
    if s:
        
        i = i+1
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite(f"Screenshots/image{i}.png", image)




