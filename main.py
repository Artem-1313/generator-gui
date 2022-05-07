import tkinter as tk
from tkinter import messagebox
import ipaddress, string, random, os
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename

entries=[]

r=[]
global selected1
selected1=False

def my_popup(e):
	menu_client.tk_popup(e.x_root, e.y_root)

def my_popup_server(e):
	menu_server.tk_popup(e.x_root, e.y_root)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)


def save_file_client():
	"""Save the current file as a new file."""
	filepath = asksaveasfilename(
		defaultextension=".txt",
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
	)
	if not filepath:
		return
	with open(filepath, mode="w", encoding="utf-8") as output_file:
		text = client_text_box.get("1.0", tk.END)
		output_file.write(text)

def save_file_server():
	"""Save the current file as a new file."""
	filepath = asksaveasfilename(
		defaultextension=".txt",
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
	)
	if not filepath:
		return
	with open(filepath, mode="w", encoding="utf-8") as output_file:
		text = server_text_box.get("1.0", tk.END)
		output_file.write(text)

def server_188():
	x=test()
	path_origin = resource_path("origin/cfg.txt")
	path_origin_server= resource_path("origin/cfg-server.txt")
	def split_cfg_file(path):
		
		with open(path, 'r') as file:
		  filedata = file.read()

		checkWords = ("{{LAN}}", "{{LAN-RANGE}}", "{{LAN-GW}}", "{{LAN-ADDRESS}}", "{{USER}}", "{{PSW}}", "{{L2TP-IP}}", "{{PEER-NAME}}")
		repWords = (x[0], x[1], x[2], str(x[3]), x[4], x[5], x[7], x[9])
		# Replace the target string
		for check, rep in zip(checkWords, repWords):
			filedata = filedata.replace(check, rep)
		return filedata

	# Write the file out again
	client_text_box.delete('1.0', tk.END)
	server_text_box.delete('1.0', tk.END)	
	client_text_box.insert(tk.END, split_cfg_file(path_origin))
	server_text_box.insert(tk.END, split_cfg_file(path_origin_server))
	return "188 works"

def server_190():
	x=test()
	path_origin = resource_path("origin/cfg-190.txt")
	path_origin_server= resource_path("origin/cfg-190-server.txt")
	def split_cfg_file(path):
		
		with open(path, 'r') as file:
		  filedata = file.read()

		checkWords = ("{{LAN}}", "{{LAN-RANGE}}", "{{LAN-GW}}", "{{LAN-ADDRESS}}", "{{USER}}", "{{PSW}}", "{{L2TP-IP}}", "{{PEER-NAME}}")
		repWords = (x[0], x[1], x[2], str(x[3]), x[4], x[5], x[7], x[9])
		# Replace the target string
		for check, rep in zip(checkWords, repWords):
			filedata = filedata.replace(check, rep)
		return filedata

	# Write the file out again
	client_text_box.delete('1.0', tk.END)
	server_text_box.delete('1.0', tk.END)	
	client_text_box.insert(tk.END, split_cfg_file(path_origin))
	server_text_box.insert(tk.END, split_cfg_file(path_origin_server))
	return "190 works"

def server_cloud():
	x=test()
	path_origin = resource_path("origin/cfg-Cloud.txt")
	path_origin_server= resource_path("origin/cfg-Cloud-server.txt")
	def split_cfg_file(path):
		
		with open(path, 'r') as file:
		  filedata = file.read()

		checkWords = ("{{LAN}}", "{{LAN-RANGE}}", "{{LAN-GW}}", "{{LAN-ADDRESS}}", "{{USER}}", "{{PSW}}", "{{L2TP-IP}}", "{{PEER-NAME}}")
		repWords = (x[0], x[1], x[2], str(x[3]), x[4], x[5], x[7], x[9])
		# Replace the target string
		for check, rep in zip(checkWords, repWords):
			filedata = filedata.replace(check, rep)
		return filedata

	# Write the file out again
	client_text_box.delete('1.0', tk.END)
	server_text_box.delete('1.0', tk.END)	
	client_text_box.insert(tk.END, split_cfg_file(path_origin))
	server_text_box.insert(tk.END, split_cfg_file(path_origin_server))


	return f"Cloud works"	

def select_server(argument):
	switcher = {
		1: server_188,
		2: server_190,
		3: server_cloud,

	}
	# Get the function from switcher dictionary


	func = switcher.get(argument, lambda: " Невірний вибір!")
	print(func())

def generate_ppp_psw():

		result_str = ''.join((random.choice('!~^-+_:#*') for _ in range(12)))
		psw = ''.join(random.choice(result_str + string.ascii_uppercase + string.digits + string.ascii_lowercase + result_str) for _ in range(55))
		return psw

def test():
	
	r.clear()
	for index, i in enumerate(entries):
		if index == 0 or index==2:
			try:
				 ipaddress.ip_network(i.get().strip())
			except ValueError:
				 messagebox.showerror('Error', 'Невірна адреса мережі!')
				 return
		if len(i.get())==0:
			r.clear()
			messagebox.showerror('Error', 'ppp логін не введено!')
			return
		r.append(i.get().strip())
	ip_addr = r[0]
	user = r[1]
	psw = generate_ppp_psw()
	l2tp_ip = r[2]
	l2tp_ip_split=l2tp_ip.split('.')
	peer_name=(f"peer{l2tp_ip_split[2]}-{l2tp_ip_split[3]}")
	peer_name_190=l2tp_ip_split[3]
	n = ipaddress.IPv4Network(ip_addr)

	gw = str(n[1])
	gw_addr = str(gw) + "/" + ip_addr[-2:]

	second = str(n[2])
	last = str(n[-2])
	range_net = f"{second}-{last}"
	filename = user + ".txt"
	return (gw_addr, range_net, gw, ip_addr, user, psw, filename, l2tp_ip, peer_name, peer_name_190)
	
def test1():
	select_server(selected.get())
		
def clipboard_client():
	window.clipboard_clear()
	window.clipboard_append(client_text_box.get("1.0", tk.END))

def clipboard_server():
	window.clipboard_clear()
	window.clipboard_append(server_text_box.get("1.0", tk.END))	
	

	

# options for і
window = tk.Tk()
window.title("МЕЛТелеком генератор")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width=1250
window_height=650
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

for index, text in enumerate(labels):
	label=tk.Label(master=ent_frame, text=text)
	entry = tk.Entry(master=ent_frame, width=30,name=str(index))
	entries.append(entry)
	label.grid(stick="W")
	entry.grid(padx=10)



btn_submit = tk.Button(master=ent_frame, text="Генерувати!", command=test1)
btn_submit.grid(stick="we", pady=5)

ent_frame.grid(row=0,column=0,stick="NW")

client_frame=tk.Frame(window,relief=tk.SUNKEN,borderwidth=5)
client_label=tk.Label(master=client_frame, text="Клієнтський скрипт")
client_label.grid(row=0, column=0)
client_text_box=tk.Text(master=client_frame, height=20, width=116, wrap="none")
print(window_height)
textVsb = tk.Scrollbar(client_frame, orient="vertical", command=client_text_box.yview)
textHsb = tk.Scrollbar(client_frame, orient="horizontal", command=client_text_box.xview)
client_text_box.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)
client_text_box.grid(row=1, column=0, sticky="nsew")
textVsb.grid(row=1, column=1, sticky="ns")
textHsb.grid(row=2, column=0, sticky="ew")

btn_copy = tk.Button(master=client_frame, text="Скопіювати!", command=clipboard_client)
btn_copy.grid(row=3,stick="E")
btn_to_file = tk.Button(master=client_frame, text="Зберегти!", command=save_file_client)
btn_to_file.grid(row=3,stick="w")


client_frame.grid(row=0, column=1, stick="N", pady=1)


server_frame=tk.Frame(window,  relief=tk.SUNKEN,borderwidth=5)
server_label=tk.Label(master=server_frame, text="Серверний скрипт")
server_label.grid()
server_text_box=tk.Text(master=server_frame, height=9, width=116, wrap="none")
textVsb = tk.Scrollbar(server_frame, orient="vertical", command=server_text_box.yview)
textHsb = tk.Scrollbar(server_frame, orient="horizontal", command=server_text_box.xview)
server_text_box.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)
server_text_box.grid(row=1, column=0, sticky="nsew")
textVsb.grid(row=1, column=1, sticky="ns")
textHsb.grid(row=2, column=0, sticky="ew")
btn_copy_ = tk.Button(master=server_frame, text="Скопіювати!", command=clipboard_server)
btn_copy_.grid(row=3,stick="E")
btn_to_file_ = tk.Button(master=server_frame, text="Зберегти!", command=save_file_server)
btn_to_file_.grid(row=3,stick="w")
server_text_box.grid()


server_frame.grid(row=1,column=1)

def cut_client(e):
	global selected1
	# Check to see if keyboard shortcut used
	if e:
		selected1 = window.clipboard_get()
	else:
		if client_text_box.selection_get():
			# Grab selected text from text box
			selected1 = client_text_box.selection_get()
			# Delete Selected Text from text box
			client_text_box.delete("sel.first", "sel.last")
			# Clear the clipboard then append
			window.clipboard_clear()
			window.clipboard_append(selected1)

def copy_client(e):
	global selected1
	# check to see if we used keyboard shortcuts
	
	if e:
		selected1 = window.clipboard_get()
	if client_text_box.selection_get():
		# Grab selected text from text box
		selected1 = client_text_box.selection_get()
		# Clear the clipboard then append
		window.clipboard_clear()
		window.clipboard_append(selected1)

def paste_client(e):
	global selected1
	#Check to see if keyboard shortcut used
	if e:
		selected1 = window.clipboard_get()
	else:
		if selected1:
			position = client_text_box.index("insert")
			client_text_box.insert(position, selected1)

####
def cut_server(e):
	global selected1
	# Check to see if keyboard shortcut used
	if e:
		selected1 = window.clipboard_get()
	else:
		if server_text_box.selection_get():
			# Grab selected text from text box
			selected1 = server_text_box.selection_get()
			# Delete Selected Text from text box
			server_text_box.delete("sel.first", "sel.last")
			# Clear the clipboard then append
			window.clipboard_clear()
			window.clipboard_append(selected1)

def copy_server(e):
	global selected1
	# check to see if we used keyboard shortcuts
	if e:
		selected1 = window.clipboard_get()

	if server_text_box.selection_get():
		# Grab selected text from text box
		selected1 = server_text_box.selection_get()
		# Clear the clipboard then append
		window.clipboard_clear()
		window.clipboard_append(selected1)

def paste_server(e):
	global selected1
	#Check to see if keyboard shortcut used
	if e:
		selected1 = window.clipboard_get()
	else:
		if selected1:
			position = server_text_box.index("insert")
			server_text_box.insert(position, selected1)
####
def select_all_client(e):
	# Add sel tag to select all text
	client_text_box.tag_add('sel', '1.0', 'end')

def select_all_server(e):
	# Add sel tag to select all text
	server_text_box.tag_add('sel', '1.0', 'end')

menu_client = tk.Menu(client_text_box, tearoff=False)
menu_client.add_command(label="Копіювати!",command=lambda:copy_client(False))
menu_client.add_command(label="Вирізати", command=lambda: cut_client(False),accelerator="(Ctrl+x)")
menu_client.add_command(label="Вставити", command=lambda:paste_client(False))
menu_client.add_command(label="Виділити все", command=lambda:select_all_client(False), accelerator="(Ctrl+A)")

menu_client.add_separator()


client_text_box.bind("<Button-3>", my_popup)
window.bind("<Control-C>", copy_client)
window.bind("<Control-c>", copy_client)
window.bind("<Control-X>", cut_client)
window.bind("<Control-x>", cut_client)
window.bind("<Control-v>", paste_client)
window.bind("<Control-V>", paste_client)
window.bind("<Control-a>", select_all_client)
window.bind("<Control-A>", select_all_client)








menu_server = tk.Menu(server_text_box, tearoff=False)
menu_server.add_command(label="Копіювати!",command=lambda:copy_server(False))
menu_server.add_command(label="Вирізати", command=lambda: cut_server(False))
menu_server.add_command(label="Вставити", command=lambda:paste_server(False))
menu_server.add_command(label="Виділити все", command=lambda:select_all_server(False), accelerator="(Ctrl+A)")

menu_server.add_separator()



server_text_box.bind("<Button-3>", my_popup_server)
server_text_box.bind("<Control-c>", copy_server)
server_text_box.bind("<Control-C>", copy_server)
server_text_box.bind("<Control-x>", cut_server)
server_text_box.bind("<Control-X>", cut_server)
server_text_box.bind("<Control-v>", paste_server)
server_text_box.bind("<Control-V>", paste_server)


window.mainloop()


