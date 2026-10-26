
def Create_quiz(filename):
    import customtkinter as ctk

    Window = ctk.CTk()
    Window.title(filename)
    Window.geometry("337x227")
    Window.resizable(False,False)

    global Current_question_index
    Current_question_index = 0
    global Final_points
    Final_points = 0

    with open(filename, "r") as File:
        Lines = File.readlines()
        Lines = [Line.strip() for Line in Lines]
        Questions = [Lines[i:i+5] for i in range(0,len(Lines),5)]

    def update_question(question_index):
        Question = Questions[question_index]
        for i in range(1,5):
            if Question[i].endswith(" 0"):
                Question[i] = Question[i].removesuffix("0")
            elif Question[i].endswith(" 1"):
                global True_answer
                True_answer = i
                Question[i] = Question[i].removesuffix("1")

        Question_entry.configure(state="normal")
        Question_entry.delete(0, ctk.END)
        Question_entry.insert(0, Question[0])
        Question_entry.configure(state="disabled")

        Answer_A_entry.configure(state="normal")
        Answer_A_entry.delete(0, ctk.END)
        Answer_A_entry.insert(0, Question[1])
        Answer_A_entry.configure(state="disabled")

        Answer_B_entry.configure(state="normal")
        Answer_B_entry.delete(0, ctk.END)
        Answer_B_entry.insert(0, Question[2])
        Answer_B_entry.configure(state="disabled")

        Answer_C_entry.configure(state="normal")
        Answer_C_entry.delete(0, ctk.END)
        Answer_C_entry.insert(0, Question[3])
        Answer_C_entry.configure(state="disabled")
        
        Answer_D_entry.configure(state="normal")
        Answer_D_entry.delete(0, ctk.END)
        Answer_D_entry.insert(0, Question[4])
        Answer_D_entry.configure(state="disabled")

    def next_question(answer):
        global True_answer

        if True_answer == answer:
            global Final_points
            Final_points += 1

        global Current_question_index
        Current_question_index += 1

        if Current_question_index < len(Questions):
            update_question(Current_question_index)
        else:
            for Widget in Window.winfo_children():
                Widget.destroy()

            Final_score_label = ctk.CTkLabel(Window,text= f"Final Score is {Final_points}")
            Final_score_label.grid(row=0,column=0,padx=5,pady=5)

    Frame1 = ctk.CTkFrame(Window)
    Frame1.place(relx=0.5,rely=0.5,anchor="center")

    Frame2 = ctk.CTkFrame(Frame1)
    Frame2.grid(row=0,column=0,padx=5,pady=5)

    Frame3 = ctk.CTkFrame(Frame2)
    Frame3.grid(row=0,column=0,padx=5,pady=5)

    Question_entry = ctk.CTkEntry(Frame3,width=300,height=30)
    Question_entry.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

    Answer_A_button = ctk.CTkButton(Frame3,text="A",width=30,height=30,command=lambda:next_question(1))
    Answer_A_button.grid(row=1,column=0,padx=5,pady=5)
    Answer_A_entry = ctk.CTkEntry(Frame3,width=250,height=30)
    Answer_A_entry.grid(row=1,column=1,padx=5,pady=5)

    Answer_B_button = ctk.CTkButton(Frame3,text="B",width=30,height=30,command=lambda:next_question(2))
    Answer_B_button.grid(row=2,column=0,padx=5,pady=5)
    Answer_B_entry = ctk.CTkEntry(Frame3,width=250,height=30)
    Answer_B_entry.grid(row=2,column=1,padx=5,pady=5)

    Answer_C_button = ctk.CTkButton(Frame3,text="C",width=30,height=30,command=lambda:next_question(3))
    Answer_C_button.grid(row=3,column=0,padx=5,pady=5)
    Answer_C_entry = ctk.CTkEntry(Frame3,width=250,height=30)
    Answer_C_entry.grid(row=3,column=1,padx=5,pady=5)

    Answer_D_button = ctk.CTkButton(Frame3,text="D",width=30,height=30,command=lambda:next_question(4))
    Answer_D_button.grid(row=4,column=0,padx=5,pady=5)
    Answer_D_entry = ctk.CTkEntry(Frame3,width=250,height=30)
    Answer_D_entry.grid(row=4,column=1,padx=5,pady=5)

    update_question(Current_question_index)

    Window.mainloop()