import tkinter as tk
from tkinter import messagebox
import smtplib
def send_email():
  email_sender = "prathiba2654@gmail.com"
  pswd_sender = "1@donttrust"
  email_receiver = receiver_entry.get()
  subject=subject_entry.get()
  msg = msg_text.get("1.0",tk.END)
  try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
       server.starttls()
       server.login(email_sender,pswd_sender)
       email_msg = f"Subject: {subject}\n\n{msg}"
       server.sendmail(email_sender,email_receiver,email_msg)
    messagebox.showinfo("Success","Email sent successfully!")
  except Exception as e:
    messagebox.showinfo("Success","Email sent successfully!")
def entry_focus_in(event):
  event.widget.config(bg="beige")
def entry_focus_out(event):
  event.widget.config(bg="white")

def exit_email():
  app.destroy()

app = tk.Tk()
app.title("Mail Application")
app.geometry("700x450")
app.config(bg="#000000")

frame = tk.Frame(app,bg="white",highlightbackground="red",highlightthickness=5,padx=40,pady=30)
frame.pack(fill=tk.BOTH,expand=True,padx=30,pady=20)

mail_icon = tk.PhotoImage(file="C:\\Users\\prathiswe\\Videos\\images.png")
r_mail_icon = mail_icon.subsample(6)

#creating widgets for entry 
label_receiver = tk.Label(frame,text=" Receiver Email:",bg="white",image=r_mail_icon,compound="left",fg="black",font=("Palatino Linotype bold italic",12,"underline"))
label_receiver.grid(row=0,column=0,sticky="e")
receiver_entry = tk.Entry(frame,width=53,highlightbackground="black",highlightthickness=0.5)
receiver_entry.grid(row=0,column=1,padx=5,pady=5,sticky="w")
receiver_entry.bind("<FocusIn>",entry_focus_in)
receiver_entry.bind("<FocusOut>",entry_focus_out)

label_subj = tk.Label(frame,text="Subject:",bg="white",compound="left",font=("Palatino Linotype bold italic",12,"underline"))
label_subj.grid(row=1,column=0,sticky="e")
subject_entry = tk.Entry(frame,width = 53,highlightbackground="black",highlightthickness=0.5)
subject_entry.grid(row=1,column=1,padx=5,pady=5,sticky="w")
subject_entry.bind("<FocusIn>",entry_focus_in)
subject_entry.bind("<FocusOut>",entry_focus_out)

label_msg = tk.Label(frame,text="Message:",bg="white",compound="left",font=("Palatino Linotype bold italic",12,"underline"))
label_msg.grid(row=2,column=0,sticky="e")
msg_text = tk.Text(frame,height=10,width=40,highlightbackground="black",highlightthickness=0.5)
msg_text.grid(row=2,column=1,padx=5,pady=5,sticky="w")
msg_text.bind("<FocusIn>",entry_focus_in)
msg_text.bind("<FocusOut>",entry_focus_out)

#creating the send button
send_btn = tk.Button(frame,text="Send",command=send_email,bg="#6D4C41",fg="white",font=("Palatino Linotype 10 bold italic",10),padx=10,pady=5)
send_btn.grid(row=3,column=1,columnspan=1,padx=9,pady=9)
exit_btn = tk.Button(frame,text="Exit from application",command=exit_email,bg="tomato",font=("Palatino Linotype bold italic",10),padx=10,pady=5)
exit_btn.grid(row=4,column=1,columnspan=1,padx=9,pady=9)

#main loop
app.mainloop()