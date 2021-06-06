import tkinter as tk
import tkvideo
import cv2
from tkinter.constants import CENTER

main_window = tk.Tk()

width= main_window.winfo_screenwidth()               
height= main_window.winfo_screenheight()               
main_window.geometry("%dx%d" % (width, height))
main_window['background'] = "#252526"
main_window.title("Exam-Proctor")

student1 = ""
student2 = ""
student3 = ""
student4 = "Hello"

label4_frame = tk.Frame(main_window,width=400,height=40,bg="#5b64bd")
label4_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
lbl4 = tk.Label(label4_frame,bg="#5b64bd",fg="#ffffff",text=student4,font=("Helvetica",20))
lbl4.config(anchor=CENTER)
lbl4.pack()
label4_frame.place(relx=0.7,rely=0.8)

label3_frame = tk.Frame(main_window,width=400,height=40,bg="#5b64bd")
label3_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
lbl3 = tk.Label(label3_frame,bg="#5b64bd",fg="#ffffff",text=student3,font=("Helvetica",20))
lbl3.config(anchor=CENTER)
lbl3.pack()
label3_frame.place(relx=0.7,rely=0.7)

label2_frame = tk.Frame(main_window,width=400,height=40,bg="#5b64bd")
label2_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
lbl2 = tk.Label(label2_frame,bg="#5b64bd",fg="#ffffff",text=student2,font=("Helvetica",20))
lbl2.config(anchor=CENTER)
lbl2.pack()
label2_frame.place(relx=0.7,rely=0.6)

label1_frame = tk.Frame(main_window,width=400,height=40,bg="#5b64bd")
label1_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
lbl1 = tk.Label(label1_frame,bg="#5b64bd",fg="#ffffff",text=student1,font=("Helvetica",20))
lbl1.config(anchor=CENTER)
lbl1.pack()
label1_frame.place(relx=0.7,rely=0.5)

video4_frame = tk.Frame(main_window,width=400,height=300,bg="#5b64bd")
video4_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
vid4 = tk.Label(video4_frame,bg="#5b64bd",fg="#ffffff",text=student3,font=("Helvetica",20))
vid4.config(anchor=CENTER)
vid4.pack()
video4_frame.place(relx=0.35,rely=0.5)

video2_frame = tk.Frame(main_window,width=400,height=300,bg="#5b64bd")
video2_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
vid2 = tk.Label(video2_frame,bg="#5b64bd",fg="#ffffff",text=student3,font=("Helvetica",20))
vid2.config(anchor=CENTER)
vid2.pack()
video2_frame.place(relx=0.35,rely=0.12)

video3_frame = tk.Frame(main_window,width=400,height=300,bg="#5b64bd")
video3_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
vid3 = tk.Label(video3_frame,bg="#5b64bd",fg="#ffffff",text=student3,font=("Helvetica",20))
vid3.config(anchor=CENTER)
vid3.pack()
video3_frame.place(relx=0.05,rely=0.5)

video1_frame = tk.Frame(main_window,width=400,height=300,bg="#5b64bd")
video1_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
vid1 = tk.Label(video1_frame,bg="#5b64bd",fg="#ffffff",text=student3,font=("Helvetica",20))
vid1.config(anchor=CENTER)
vid1.pack()
video1_frame.place(relx=0.05,rely=0.12)

tk.Label(main_window, 
		 text="Exam-Proctor",
		 fg = "#ffffff",
		 bg = "#5b64bd",
		 font = "Helvetica 40 bold italic").pack()


main_window.mainloop()

