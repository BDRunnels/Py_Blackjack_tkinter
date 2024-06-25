import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

main_windows = tkinter.Tk()

main_windows.title("Hello World")
main_windows.geometry("640x480+8+400")  # 640x480+(x-offset)+(y-offset)

# PACK GEOMETRY MANAGER
label = tkinter.Label(main_windows, text="Hello World")
label.pack(side="top")

left_frame = tkinter.Frame(main_windows)
left_frame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

right_frame = tkinter.Frame(main_windows)
right_frame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

main_windows.mainloop()
