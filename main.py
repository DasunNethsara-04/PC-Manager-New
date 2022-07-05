# imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import platform
import psutil
import os
import datetime
import disk
import webbrowser

# important variables
total = 0
pc_name = platform.node()
cpu_data = platform.processor()
ram_data = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
sys = platform.system()
rls = platform.release()
edition = platform.win32_edition()
time = datetime.datetime.now().strftime("%I:%M:%S %p")
date = datetime.date.today()
cpu_cores = psutil.cpu_count(logical=True)
cpu_threads = psutil.cpu_count(logical=False)
arch = platform.architecture()[0]
clock = psutil.cpu_freq().current
machine = platform.uname().machine
hdd_usable_size = disk.ret()[0]
hdd_actual_size = disk.ret()[1]
hdd_used_size = disk.ret()[2]
hdd_free_size = disk.ret()[3]

# functions
def secs2hours(secs):
	mm, ss = divmod(secs, 60)
	hh, mm = divmod(mm, 60)
	return "%d:%02d:%02d" % (hh, mm, ss)

def battery():
	if not hasattr(psutil, "sensors_battery"):
		#return sys.exit("platform not supported")
		btry.config(text='Platform not supported')
	batt = psutil.sensors_battery()
	if batt is None:
		btry.config(text='N/A')
		btry.after(1000, battery)
		#return sys.exit("no battery is installed")
	else:
		btry.config(text=("Charge:     %s%%" % round(batt.percent, 2)))
		btry.after(1000, battery)
		#print("charge:     %s%%" % round(batt.percent, 2))

def cpu_check():
	cpu_data = psutil.cpu_percent()
	cpu.config(text=str(cpu_data)+"%")
	cpu.after(1000, cpu_check)

def ramcheck():
	per_ram = psutil.virtual_memory().percent
	ram.config(text=str(per_ram)+'%')
	ram.after(1000, ramcheck)

def totRam():
	total_ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
	tot_ram.config(text=str(total_ram)+'GB (usable)')
	tot_ram.after(1000, totRam)

def useRam():
	used_ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
	usd_ram.config(text=str(used_ram)+'GB')
	usd_ram.after(1000, useRam)

def freeRam():
	freeram = round((psutil.virtual_memory().free) / (1024 ** 3), 2)
	free_ram.config(text=str(freeram)+'GB')
	free_ram.after(1000, freeRam)

def cleanup():
	os.startfile('C:\\Windows\\System32\\cleanmgr.exe')

def ctrl():
	os.startfile('C:\\Windows\\System32\\control.exe')

def defrag():
	os.startfile('C:\\Windows\\System32\\dfrgui.exe')

def sys_info():
	path = 'C:\\WINDOWS\\System32\\msinfo32.exe'
	os.startfile(os.path.join(path))

def add_rem():
	path = 'C:\\WINDOWS\\System32\\appwiz.cpl'
	os.startfile(os.path.join(path))

def win():
	path = 'C:\\WINDOWS\\system32\\winver.exe'
	os.startfile(os.path.join(path))

def restore():
	os.startfile('C:\\Windows\\System32\\rstrui.exe')

def web():
	webbrowser.open('https://sites.google.com/view/techsaralk')

def github():
	webbrowser.open('https://github.com/DasunNethsara-04')

def telegram():
	webbrowser.open('https://t.me/techsara_lk')

def youtube():
	webbrowser.open('https://www.youtube.com/channel/UCpWe6k8GxYuLmlzlvX7VBRg')

# main interface
root = Tk()
root.title("PC Manager")
root.geometry('1200x750+200+200')
root.iconbitmap('icon.ico')
root.resizable(0, 0)

s = ttk.Style()
s.configure('TNotebook.Tab', font=('Calibri', 16))
s.configure('TButton', font=('Ubuntu', 16))

# structure
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, pady=5, expand=True)

tab1 = ttk.Frame(tabs, width=1200, height=750)
tab2 = ttk.Frame(tabs, width=1200, height=750)
tab3 = ttk.Frame(tabs, width=1200, height=750)
tab4 = ttk.Frame(tabs, width=1200, height=750)
tab5 = ttk.Frame(tabs, width=1200, height=750)
tab6 = ttk.Frame(tabs, width=1200, height=750)

tabs.add(tab1, text='Dashboard')
tabs.add(tab2, text='Processor')
tabs.add(tab3, text='Memory')
tabs.add(tab4, text='Storage')
tabs.add(tab5, text='Utilities')
tabs.add(tab6, text='About Us')



######## TAB 1 - Dashboard ########
Label(tab1, text='SYSTEM DASHBOARD', font='Poppins 45 underline', fg='red').pack()
Label(tab1, text=f'Current Time/Date:\t\t{time}, {date}', font='arial 18').place(x=15, y=180)
Label(tab1, text=f'Computer Name:\t\t{pc_name}', font='arial 18').place(x=15, y=240)
Label(tab1, text=f'Processor:\t\t{cpu_data}', font='arial 18').place(x=15, y=300)
Label(tab1, text=f'System Memory:\t\t{ram_data}GB (Usable)', font='arial 18').place(x=15, y=360)
Label(tab1, text=f'Operating System:\t\t{sys} {rls} {edition}', font='arial 18').place(x=15, y=420)
Label(tab1, text='Battery:', font='arial 18').place(x=15, y=480)
btry = Label(tab1, font='arial 18')
btry.place(x=328, y=480)


ttk.Button(tab1, text='EXIT', command=root.destroy).pack(side=BOTTOM)

########					########

######## TAB 2 - Processor ########
Label(tab2, text='PROCESSOR', font='Poppins 45 underline', fg='red').pack()
Label(tab2, text='Utilization:', font='arial 18').place(x=15, y=180)
cpu = Label(tab2, font='arial 18')
cpu.place(x=328, y=180)
Label(tab2, text=f'Processor:\t\t{cpu_data}', font='arial 18').place(x=15, y=240)
Label(tab2, text=f'Cores:\t\t\t{cpu_cores}', font='arial 18').place(x=15, y=300)
Label(tab2, text=f'Threads:\t\t\t{cpu_threads}', font='arial 18').place(x=15, y=360)
Label(tab2, text=f'Architecture:\t\t{arch}', font='arial 18').place(x=15, y=420)
Label(tab2, text=f'Clock Speed:\t\t{clock/1000}GHz ({clock}MHz)', font='arial 18').place(x=15, y=480)
Label(tab2, text=f'Machine:\t\t\t{machine}', font='arial 18').place(x=15, y=540)
ttk.Button(tab2, text='EXIT', command=root.destroy).pack(side=BOTTOM)
########					########

######## TAB 3 - Memory ########
Label(tab3, text='MEMORY', font='Poppins 45 underline', fg='red').pack()
Label(tab3, text='Utilization:', font='arial 18').place(x=15, y=180)
ram = Label(tab3, font='arial 18')
ram.place(x=328, y=180)

Label(tab3, text='Total RAM:', font='arial 18').place(x=15, y=240)
tot_ram = Label(tab3, font='arial 18')
tot_ram.place(x=328, y=240)

Label(tab3, text='Used RAM:', font='arial 18').place(x=15, y=300)
usd_ram = Label(tab3, font='arial 18')
usd_ram.place(x=328, y=300)

Label(tab3, text='Free RAM:', font='arial 18').place(x=15, y=360)
free_ram = Label(tab3, font='arial 18')
free_ram.place(x=328, y=360)

ttk.Button(tab3, text='EXIT', command=root.destroy).pack(side=BOTTOM)
########					########

######## TAB 4 - Storage ########
Label(tab4, text='STORAGE', font='Poppins 45 underline', fg='red').pack()
Label(tab4, text=f'Capacity:\t\t{hdd_actual_size}GB', font='arial 18').place(x=15, y=180)
Label(tab4, text=f'Usable:\t\t{hdd_usable_size}GB', font='arial 18').place(x=15, y=240)
Label(tab4, text=f'Used:\t\t{hdd_used_size}GB', font='arial 18').place(x=15, y=300)
Label(tab4, text=f'Free:\t\t{hdd_free_size}GB', font='arial 18').place(x=15, y=360)

ttk.Button(tab4, text='EXIT', command=root.destroy).pack(side=BOTTOM)
########					########

######## TAB 5 - Utilities ########
Label(tab5, text='UTILITIES', font='Poppins 45 underline', fg='red').pack()
ttk.Button(tab5, text='Disk Cleanup', command=cleanup, width=25).place(x=35, y=180)
Label(tab5, text='Cleanup Junk Fils with just few clicks', font='arial 18').place(x=370, y=180)
ttk.Button(tab5, text='Control Panel', command=ctrl, width=25).place(x=35, y=240)
Label(tab5, text='To open Control Panel', font='arial 18').place(x=370, y=240)
ttk.Button(tab5, text='Disk Defragment', command=defrag, width=25).place(x=35, y=300)
Label(tab5, text='Defrag the Hard Disk to keep your PC Faster', font='arial 18').place(x=370, y=300)
ttk.Button(tab5, text='System Information', command=sys_info, width=25).place(x=35, y=360)
Label(tab5, text='Get advanced details about your computer', font='arial 18').place(x=370, y=360)
ttk.Button(tab5, text='Add/ Remove Apps', command=add_rem, width=25).place(x=35, y=420)
Label(tab5, text='Remove unwanted applications from your computer', font='arial 18').place(x=370, y=420)
ttk.Button(tab5, text='About Windows', command=win, width=25).place(x=35, y=480)
Label(tab5, text='Get details about the main operating system', font='arial 18').place(x=370, y=480)
ttk.Button(tab5, text='System Restore', command=restore, width=25).place(x=35, y=540)
Label(tab5, text='Keep your computer safe with system restore feature', font='arial 18').place(x=370, y=540)

ttk.Button(tab5, text='EXIT', command=root.destroy).pack(side=BOTTOM)
########					########

######## TAB 6 - About Us ########

img1 = Image.open('images/img.png')
img1 = img1.resize((250, 250))
img1 = ImageTk.PhotoImage(img1)

Label(tab6, text='ABOUT US', font='Poppins 45 underline', fg='red').pack()
Label(tab6, text='Thank you for choosing our software for your Computer!', font='arial 20').place(x=15, y=180)
Label(tab6, text='Dasun Nethsara', font='arial 18').place(x=15, y=250)
Label(tab6, image=img1, bd=0).place(x=820, y=230)
Label(tab6, text='Certified in Python Programming', font='arial 13').place(x=15, y=280)
Label(tab6, text='Certified in Web Development (HTML, CSS, PHP)', font='arial 13').place(x=15, y=305)
Label(tab6, text=f'© Tech SARA LK {datetime.date.today().year}', font='arial 15', bg='black', fg='white').pack(side=BOTTOM, fill=X)

Label(tab6, text='Contact me on', font='Poppins 20').place(x=15, y=340)
Button(tab6, text='Tech SARA LK (Web)', bd=0, font='Ubuntu 15 underline', fg='blue', command=web).place(x=35, y=400)
Button(tab6, text='GitHub', bd=0, font='Ubuntu 15 underline', fg='blue', command=github).place(x=35, y=450)
Button(tab6, text='Telegram', bd=0, font='Ubuntu 15 underline', fg='blue', command=telegram).place(x=35, y=500)
Button(tab6, text='YouTube', bd=0, font='Ubuntu 15 underline', fg='blue', command=youtube).place(x=35, y=550)


battery()
cpu_check()
ramcheck()
totRam()
useRam()
freeRam()

root.mainloop()