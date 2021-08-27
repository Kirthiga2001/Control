import serial
import tkinter as tk
import time

w=tk.Tk()
w.configure(background="black")
w.geometry("330x80")
w.title("Kittu Controller")

board=serial.Serial('COM3',9600)

def Control():
    def on():
        board.write(bytes("1", 'utf-8'))
        print("LED IS ON")
    def off():
        board.write(bytes("0", 'utf-8'))
        print("LED IS OFF")
    def quit():
        #board.write(10)
        board.close()
        w.destroy

    x=tk.Button(w, text="ON", command=on,bg="white",fg="black",font=("Helvetica", "16"))
    y=tk.Button(w, text="OFF", command=off, bg="white",fg="black", font=("Helvetica", "16"))
    z=tk.Button(w, text="EXIT", command=quit, bg="white",fg="red", font=("Helvetica", "16"))
    x.grid(row=1,column=0,padx=5,pady=10)
    y.grid(row=1,column=1,padx=5,pady=10)
    z.grid(row=1,column=2,padx=5,pady=10)

    w.mainloop()

time.sleep(0.5)
Control()
