import tkinter as tk
import tkvideo
import cv2
#import registration
#from registration import *
from tkinter.constants import CENTER
import os
from threading import *



main_window = tk.Tk()

width= main_window.winfo_screenwidth()               
height= main_window.winfo_screenheight()               
main_window.geometry("%dx%d" % (width, height))
main_window['background'] = "#252526"
main_window.title("Exam-Proctor")


def monitor():
	
	t1 = Thread(os.system("python  Face_Recognition/recognise_video.py --detector face_detection_model --embedding-model openface.nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle"))
	t2 = Thread(os.system('screenshot.py'))
	t1.start()
	t2.start()


	

video1_frame = tk.Frame(main_window,width=800,height=600,bg="#5b64bd")
video1_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
video1_frame.place(relx=0.1,rely=0.15)



reg_frame = tk.Frame(main_window,width=200,height=80,bg="#252526")
reg_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
reg = tk.Button(reg_frame,bg="#5b64bd",fg="#ffffff",text="Register",command=lambda:os.system('registration.py'),font=("Helvetica",20)) #command=os.system('registration.py')
reg.config(anchor=CENTER)
reg.pack()
reg_frame.place(relx=0.765,rely=0.4)

monitor_frame = tk.Frame(main_window,width=200,height=80,bg="#252526")
monitor_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
mon = tk.Button(monitor_frame,bg="#5b64bd",fg="#ffffff",text="Exam Time",command=lambda:monitor(),font=("Helvetica",20))
mon.config(anchor=CENTER)
mon.pack()
monitor_frame.place(relx=0.765,rely=0.3)

close_frame = tk.Frame(main_window,width=200,height=80,bg="#252526")
close_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
close = tk.Button(close_frame,bg="#5b64bd",fg="#ffffff",text="Close",command=lambda:main_window.destroy(),font=("Helvetica",20))
close.config(anchor=CENTER)
close.pack()
close_frame.place(relx=0.765,rely=0.5)

tk.Label(main_window, 
		 text="Exam-Proctor",
		 fg = "#ffffff",
		 bg = "#5b64bd",
		 font = "Helvetica 40 bold italic").pack()


main_window.mainloop()

