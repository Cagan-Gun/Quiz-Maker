import customtkinter as ctk
from customtkinter import filedialog
from Quiz import Create_quiz
import os

DATAFOLDER = "Quizzes"

if not os.path.exists(DATAFOLDER):
    os.makedirs(DATAFOLDER)

Window = ctk.CTk()
Window.title("Quiz Maker") 
Window.geometry("347x420")
Window.resizable(False, False)

def Add_question_to_file():
    Question = Add_question_entry.get()

    Answer_A = Add_answer_A_entry.get()
    if Add_answer_A_button.cget("fg_color") == "green":
        Answer_A = Answer_A + " 1"
    else:
        Answer_A = Answer_A + " 0"

    Answer_B = Add_answer_B_entry.get()
    if Add_answer_B_button.cget("fg_color") == "green":
        Answer_B = Answer_B + " 1"
    else:
        Answer_B = Answer_B + " 0"

    Answer_C = Add_answer_C_entry.get()
    if Add_answer_C_button.cget("fg_color") == "green":
        Answer_C = Answer_C + " 1"
    else:
        Answer_C = Answer_C + " 0"

    Answer_D = Add_answer_D_entry.get()
    if Add_answer_D_button.cget("fg_color") == "green":
        Answer_D = Answer_D + " 1"
    else:
        Answer_D = Answer_D + " 0"

    File_name_answer = File_name_entry.get()

    Add_question_entry.delete(0, ctk.END)
    Add_answer_A_entry.delete(0, ctk.END)
    Add_answer_B_entry.delete(0, ctk.END)
    Add_answer_C_entry.delete(0, ctk.END)
    Add_answer_D_entry.delete(0, ctk.END)
    Add_answer_A_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_B_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_C_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_D_button.configure(fg_color="red",hover_color="dark red")
    Add_question_button.configure(fg_color="red",state="disabled")
    global Selected_answer
    Selected_answer = False

    File_path = os.path.join(DATAFOLDER,File_name_answer)
    with open(File_path,"a+",encoding="utf-8") as File:
        File.write(Question + "\n")
        File.write(Answer_A + "\n")
        File.write(Answer_B + "\n")
        File.write(Answer_C + "\n")
        File.write(Answer_D + "\n")

def Select_file():
    Selected_path = filedialog.askopenfilename()
    if not Selected_path:
        return
    File_title_entry.configure(state="normal")
    File_title_entry.delete(0, ctk.END)
    File_title_entry.insert(0, Selected_path)
    File_title_entry.configure(state="disabled")
    Create_quiz(Selected_path)

def Select_file_button_on(state=None):
    if not Selected_answer: pass
    elif not File_name_entry.get(): pass
    elif not Add_question_entry.get(): pass
    elif not Add_answer_A_entry.get(): pass
    elif not Add_answer_B_entry.get(): pass
    elif not Add_answer_C_entry.get(): pass
    elif not Add_answer_D_entry.get(): pass
    else: 
        Add_question_button.configure(fg_color="green",hover_color="dark green",state="normal")
        return
    Add_question_button.configure(fg_color="red",state="disabled")

def Change_answer(widget):
    Add_answer_A_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_B_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_C_button.configure(fg_color="red",hover_color="dark red")
    Add_answer_D_button.configure(fg_color="red",hover_color="dark red")
    global Selected_answer
    Selected_answer = True
    widget.configure(fg_color="green",hover_color="dark green")
    Select_file_button_on()

Selected_answer = False

Frame = ctk.CTkFrame(Window)
Frame.place(relx=0.5,rely=0.5,anchor="center")

Question_maker_label = ctk.CTkLabel(Frame,text="______Quiz Maker______",font=("Arial Black",24,"bold"))
Question_maker_label.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

Question_maker_frame = ctk.CTkFrame(Frame)
Question_maker_frame.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

Adding_question_frame = ctk.CTkFrame(Question_maker_frame)
Adding_question_frame.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

Add_question_entry = ctk.CTkEntry(Adding_question_frame,placeholder_text="Enter your Question ...",placeholder_text_color="gray",width=300,height=30)
Add_question_entry.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
Add_question_entry.bind("<KeyRelease>",Select_file_button_on)

Add_answer_A_button = ctk.CTkButton(Adding_question_frame,text="A",fg_color="red",hover_color="dark red",command=lambda:Change_answer(Add_answer_A_button),width=30)
Add_answer_A_button.grid(row=1,column=0,padx=5,pady=5)

Add_answer_A_entry = ctk.CTkEntry(Adding_question_frame,width=250,height=30)
Add_answer_A_entry.grid(row=1,column=1,padx=5,pady=5)
Add_answer_A_entry.bind("<KeyRelease>",Select_file_button_on)

Add_answer_B_button = ctk.CTkButton(Adding_question_frame,text="B",fg_color="red",hover_color="dark red",command=lambda:Change_answer(Add_answer_B_button),width=30)
Add_answer_B_button.grid(row=2,column=0,padx=5,pady=5)

Add_answer_B_entry = ctk.CTkEntry(Adding_question_frame,width=250,height=30)
Add_answer_B_entry.grid(row=2,column=1,padx=5,pady=5)
Add_answer_B_entry.bind("<KeyRelease>",Select_file_button_on)

Add_answer_C_button = ctk.CTkButton(Adding_question_frame,text="C",fg_color="red",hover_color="dark red",command=lambda:Change_answer(Add_answer_C_button),width=30)
Add_answer_C_button.grid(row=3,column=0,padx=5,pady=5)

Add_answer_C_entry = ctk.CTkEntry(Adding_question_frame,width=250,height=30)
Add_answer_C_entry.grid(row=3,column=1,padx=5,pady=5)
Add_answer_C_entry.bind("<KeyRelease>",Select_file_button_on)

Add_answer_D_button = ctk.CTkButton(Adding_question_frame,text="D",fg_color="red",hover_color="dark red",command=lambda:Change_answer(Add_answer_D_button),width=30)
Add_answer_D_button.grid(row=4,column=0,padx=5,pady=5)

Add_answer_D_entry = ctk.CTkEntry(Adding_question_frame,width=250,height=30)
Add_answer_D_entry.grid(row=4,column=1,padx=5,pady=5)
Add_answer_D_entry.bind("<KeyRelease>",Select_file_button_on)

Adding_question_frame = ctk.CTkFrame(Question_maker_frame)
Adding_question_frame.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

File_name_entry = ctk.CTkEntry(Adding_question_frame,placeholder_text="Enter the title of the Quiz ...",placeholder_text_color="gray",width=200,height=30)
File_name_entry.grid(row=0,column=0,padx=5,pady=5)
File_name_entry.bind("<KeyRelease>",Select_file_button_on)

Add_question_button = ctk.CTkButton(Adding_question_frame,text="Add Question",fg_color="red",command=Add_question_to_file,state="disabled",width=100,height=30)
Add_question_button.grid(row=0,column=1,padx=5,pady=5)

Start_label = ctk.CTkLabel(Frame,text="______Start Quiz______",font=("Arial Black",24,"bold"))
Start_label.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

Start_frame_frame = ctk.CTkFrame(Frame)
Start_frame_frame.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

Start_frame = ctk.CTkFrame(Start_frame_frame)
Start_frame.grid(row=0,column=0,padx=5,pady=5)

File_title_entry = ctk.CTkEntry(Start_frame,placeholder_text="Enter your Quiz path ...",placeholder_text_color="gray",width=200,height=30)
File_title_entry.grid(row=0,column=0,padx=5,pady=5)
    
Select_file_button = ctk.CTkButton(Start_frame,text="Select a file",fg_color="green",hover_color="dark green",command=Select_file,width=100,height=30)
Select_file_button.grid(row=0,column=1,padx=5,pady=5)

Window.mainloop()