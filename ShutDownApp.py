from tkinter import *
import os


def restart():
    os.system("shutdown /r")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")



st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Black")


r_button=Button(st, text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="arrow",command=restart)
r_button.place(x=150,y=60,height=50,width=200)


rt_button=Button(st, text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="arrow",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)



rl_button=Button(st, text="Log-out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="arrow",command=logout)
rl_button.place(x=150,y=270,height=50,width=200)


rs_button=Button(st, text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="arrow",command=shutdown)
rs_button.place(x=150,y=370,height=50,width=200)





st.mainloop()
