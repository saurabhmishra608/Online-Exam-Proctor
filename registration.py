
import tkinter as tk
from typing import Text
import tkvideo
import cv2
import tkinter. messagebox
from tkinter.constants import CENTER
from tkinter import filedialog
import os

reg_window = tk.Tk()
global main_frame
main_frame = tk.Frame(reg_window,width=600,height=500,bg="#5b64bd")
main_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
	
main_frame.place(relx = 0.5, rely = 0.5,anchor=CENTER)

def submit(filename,main_frame):
    print(filename)
    tkinter. messagebox. showinfo("Message","Don't close the registration window. It will close automatically after successful registration")
    os.system(f"python Face_Recognition/extract_embeddings.py --dataset {filename}\ --embeddings output/embeddings.pickle --detector face_detection_model\ --embedding-model openface.nn4.small2.v1.t7")
    os.system('python Face_Recognition/train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')
    tkinter. messagebox. showinfo("Message","Registration Successful")
    reg_window.destroy()
    

filename = "hello"

def UploadAction(event=None,):
    global filename
    
    
    filename = filedialog.askdirectory()
    print(type(filename))


    
width= reg_window.winfo_screenwidth()               
height= reg_window.winfo_screenheight()               
reg_window.geometry("%dx%d" % (width, height))
reg_window['background'] = "#252526"
reg_window.title("Registeration")
tk.Label(reg_window, 
		 text="Exam-Proctor",
		 fg = "#ffffff",
		 bg = "#5b64bd",
		 font = "Helvetica 40 bold italic").pack()


name = tk.Label(main_frame,text = "Name",bg = "#5b64bd",fg = "#ffffff",font = "Helvetica 20 bold italic")
name.place(relx = 0.05,rely = 0.1)
name_input = tk.Text(main_frame,width = 30,height = 1,bg ="white",fg = "#5b64bd",font = "Helvetica 20")
name_input.place(relx = 0.22,rely = 0.1)

roll = tk.Label(main_frame,text = "Roll No",bg = "#5b64bd",fg = "#ffffff",font = "Helvetica 20 bold italic")
roll.place(relx = 0.05,rely = 0.2)
roll_input = tk.Text(main_frame,width = 30,height = 1,bg ="white",fg = "#5b64bd",font = "Helvetica 20")
roll_input.place(relx = 0.22,rely = 0.2)

course = tk.Label(main_frame,text = "Course",bg = "#5b64bd",fg = "#ffffff",font = "Helvetica 20 bold italic")
course.place(relx = 0.05,rely = 0.3)
course_input = tk.Text(main_frame,width = 30,height = 1,bg ="white",fg = "#5b64bd",font = "Helvetica 20")
course_input.place(relx = 0.22,rely = 0.3)

upload = tk.Label(main_frame,text = "Upload the folder containing minimum 15 photos of yours",bg = "#5b64bd",fg = "#ffffff",font = "Helvetica 15 bold italic")
upload.place(relx = 0.05,rely = 0.4)

upload_btn = tk.Button(main_frame,text = "Upload",font = "10",command=UploadAction)
upload_btn.place(relx = 0.05,rely = 0.48)
submit_btn = tk.Button(main_frame,text = "SUBMIT",font = "20",command = lambda:submit(filename,main_frame))
submit_btn.place(relx = 0.5,rely = 0.7,anchor=CENTER)

reg_window.mainloop()



        
    

