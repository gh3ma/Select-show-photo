import tkinter as tk

"""window_1 = tk.Tk()
welcome_massage = tk.Label(text="Name" ,
                           fg="black" ,
                           bg="#77CEFA",
                           width=25,
                           height=3,
                           )
welcome_massage.pack()

button = tk.Button(text="Upload photo",
                   bg="black",
                   fg="white",
                   width=20 ,
                   height= 3
                    )
button.pack()

Type_here = tk.Entry(fg="yellow" ,
                     bg="green"
                     )

Type_here.pack()

frame_Fun = tk.Frame()
frame_Fun.pack()
window_1.mainloop()

name = entry.get()
"""
############################
"""
Label = tk.Label(text="Name")
entry = tk.Entry()

Label.pack()
entry.pack()

entry.insert(0,"Ghaith")
entry.insert(0, "Madani ")
Label.mainloop()

"""
############################


window = tk.Tk()

text_box = tk.Text()
text_box.pack()

text_box.mainloop()