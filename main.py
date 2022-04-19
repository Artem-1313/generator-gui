import tkinter as tk

def test():
	print(selected.get())



# options for window
window = tk.Tk()
window.title("МЕЛТелеком генератор")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width=screen_width-400
window_height=screen_height-100
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
print(screen_width, screen_height)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)


## Frames

ent_frame=tk.Frame(window, relief=tk.SUNKEN,borderwidth=5)
labels = [ "ІР адреса мережі: ","l2tp логін", "ІР адреса l2tp"]
radio_lbl=tk.Label(master=ent_frame, text="Виберіть сервер МЕЛТелеком")
radio_lbl.grid(stick="W")
selected=tk.IntVar()
selected.set("3")
servers={
	"MELTelecom 188": 1,
	"MELTelecom 190": 2,
	"MELTelecom Cloud": 3,
}
for key, value in servers.items():
    tk.Radiobutton(ent_frame, text=key, value=value, variable=selected).grid(stick="W")

for text in labels:
	label=tk.Label(master=ent_frame, text=text)
	entry = tk.Entry(master=ent_frame, width=30)
	label.grid(stick="W")
	entry.grid(padx=10)
btn_submit = tk.Button(master=ent_frame, text="Генерувати!", command=test)
btn_submit.grid(stick="we", pady=5)

ent_frame.grid(row=0,column=0,stick="NW")

client_frame=tk.Frame(window,relief=tk.SUNKEN,borderwidth=5)
client_label=tk.Label(master=client_frame, text="Клієнтський скрипт")
client_label.grid(row=0, column=0)
client_text_box=tk.Text(master=client_frame, height=20)
client_text_box.grid(row=1, column=0)
btn_copy = tk.Button(master=client_frame, text="Скопіювати!")
btn_copy.grid(row=2,stick="E")
btn_to_file = tk.Button(master=client_frame, text="Зберегти!")
btn_to_file.grid(row=2,stick="w")
client_frame.grid(row=0, column=1, stick="N", pady=5)


server_frame=tk.Frame(window,  relief=tk.SUNKEN,borderwidth=5)
server_label=tk.Label(master=server_frame, text="Серверний скрипт")
server_label.grid()
server_text_box=tk.Text(master=server_frame, height=10)
server_text_box.grid()


server_frame.grid(row=1,column=1)



window.mainloop()