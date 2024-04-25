# imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import platform
import psutil
import datetime
import ctypes
import wmi
import pystray
from functions import *

pc = wmi.WMI()

# color codes
fgcolor: str = '#204db2'
fgcolor2: str = '#000000'
bgcolor: str = '#e8f0f4'
dark_bg: str = '#1d1d1d'

# important variables
total = 0
pc_name: str = platform.node()
cpu_data = pc.Win32_Processor()[0].name
ram_data: float = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
sys: str = platform.system()
rls: str = platform.release()
user: str = psutil.users()[0][0]
edition: str = platform.win32_edition()
cpu_cores: int = psutil.cpu_count(logical=False)
cpu_threads: int = psutil.cpu_count(logical=True)
arch: str = platform.architecture()[0]
clock: float = psutil.cpu_freq().current
machine: str = platform.uname().machine
# hdd_usable_size = disk.ret()[0]
# #hdd_actual_size = disk.ret()[1]
# hdd_used_size = disk.ret()[2]
# hdd_free_size = disk.ret()[3]
swap = psutil.swap_memory()
soket = pc.Win32_Processor()[0].SocketDesignation
virt = pc.Win32_Processor()[0].VirtualizationFirmwareEnabled
if virt == 'True':
	virt = 'Enabled'
else:
	virt = 'Disabled'

man = pc.Win32_Processor()[0].Manufacturer
os_name = pc.Win32_OperatingSystem()[0].Caption
os_build = pc.Win32_OperatingSystem()[0].BuildNumber
os_man = pc.Win32_OperatingSystem()[0].Manufacturer
os_lang = pc.Win32_OperatingSystem()[0].MUILanguages[0]
os_version = pc.Win32_OperatingSystem()[0].Version
os_sys_dir = pc.Win32_OperatingSystem()[0].SystemDirectory
os_win_dir = pc.Win32_OperatingSystem()[0].WindowsDirectory

# splash screen
import splash

# functions
def on_minimize(window) -> None:
	"""Minimize the main window and display the system tray icon.

    Args:
        window (tk.Tk): The main window.

    """
	window.withdraw()  # Hide the main window
	icon = pystray.Icon("PC Manager")
	icon.icon = Image.open("icon.ico")  # Replace "icon.png" with your icon file
	icon.title = "PC Manager"
	
	def on_double_click(icon, item) -> None:
		window.deiconify()  # Restore the main window
		icon.stop()
	
	def quit_app(icon, item) -> None:
		icon.stop()
		window.destroy()  # Close the application
	
	menu = (
			pystray.MenuItem("Restore", on_double_click),
			pystray.MenuItem("Open Disk Cleanup Tool", cleanup),
			pystray.MenuItem("Open Disk Defragmentation Tool", defrag),
			pystray.MenuItem("Show System Information", sys_info),
			pystray.MenuItem("Open Computer Management", ctrl),
			pystray.MenuItem("Windows Information", win),
			pystray.MenuItem("Quit", quit_app),
			)
	icon.menu = pystray.Menu(*menu)
	icon.run()


def theme_changer() -> None:
	global state
	if state:
		s.configure('TFrame', background=dark_bg)
		theme_btn.config(image=light_img, bg=dark_bg)
		lbl1.config(bg=dark_bg)
		lbl2.config(bg=dark_bg, fg='white')
		lbl3.config(bg=dark_bg, fg='white')
		lbl4.config(bg=dark_bg, fg='white')
		lbl5.config(bg=dark_bg, fg='white')
		lbl6.config(bg=dark_bg, fg='white')
		lbl7.config(bg=dark_bg, fg='white')
		lbl8.config(bg=dark_bg, fg='white')
		lbl9.config(bg=dark_bg, fg='white')
		lbl10.config(bg=dark_bg, fg='white')
		lbl11.config(bg=dark_bg, fg='white')
		lbl12.config(bg=dark_bg, fg='white')
		lbl13.config(bg=dark_bg, fg='white')
		lbl14.config(bg=dark_bg, fg='white')
		lbl15.config(bg=dark_bg, fg='white')
		btry.config(bg=dark_bg)
		usr.config(bg=dark_bg, fg='white')

		lbl16.config(bg=dark_bg)
		cpu.config(bg=dark_bg, fg='white')
		lbl17.config(bg=dark_bg, fg='white')
		lbl18.config(bg=dark_bg, fg='white')
		lbl19.config(bg=dark_bg, fg='white')
		lbl20.config(bg=dark_bg, fg='white')
		lbl21.config(bg=dark_bg, fg='white')
		lbl22.config(bg=dark_bg, fg='white')
		lbl23.config(bg=dark_bg, fg='white')
		lbl24.config(bg=dark_bg, fg='white')
		lbl25.config(bg=dark_bg, fg='white')
		lbl26.config(bg=dark_bg, fg='white')
		lbl27.config(bg=dark_bg, fg='white')
		lbl28.config(bg=dark_bg, fg='white')
		lbl29.config(bg=dark_bg, fg='white')
		lbl30.config(bg=dark_bg, fg='white')
		lbl31.config(bg=dark_bg, fg='white')
		lbl32.config(bg=dark_bg, fg='white')
		lbl33.config(bg=dark_bg, fg='white')
		lbl34.config(bg=dark_bg, fg='white')
		lbl35.config(bg=dark_bg, fg='white')
		lbl36.config(bg=dark_bg, fg='white')
		lbl37.config(bg=dark_bg, fg='white')
		lbl38.config(bg=dark_bg, fg='white')
		lbl39.config(bg=dark_bg, fg='white')
		lbl40.config(bg=dark_bg, fg='white')

		lbl41.config(bg=dark_bg)
		lbl42.config(bg=dark_bg, fg='blue')
		lbl43.config(bg=dark_bg, fg='white')
		lbl44.config(bg=dark_bg, fg='white')
		lbl45.config(bg=dark_bg, fg='white')
		lbl46.config(bg=dark_bg, fg='white')
		lbl47.config(bg=dark_bg, fg='blue')
		lbl48.config(bg=dark_bg, fg='white')
		lbl49.config(bg=dark_bg, fg='white')
		lbl50.config(bg=dark_bg, fg='white')
		lbl51.config(bg=dark_bg, fg='white')
		lbl52.config(bg=dark_bg, fg='white')
		ram.config(bg=dark_bg, fg='white')
		tot_ram.config(bg=dark_bg, fg='white')
		usd_ram.config(bg=dark_bg, fg='white')
		free_ram.config(bg=dark_bg, fg='white')
		swap_per.config(bg=dark_bg, fg='white')
		tot_swap.config(bg=dark_bg, fg='white')
		usd_swap.config(bg=dark_bg, fg='white')
		free_swap.config(bg=dark_bg, fg='white')

		#frame.config(bg=dark_bg)
		# lbl53.config(bg=dark_bg)
		# lbl54.config(bg=dark_bg, fg='blue')
		# lbl55.config(bg=dark_bg, fg='white')
		# lbl56.config(bg=dark_bg, fg='white')
		# lbl57.config(bg=dark_bg, fg='white')
		# lbl58.config(bg=dark_bg, fg='white')
		# lbl59.config(bg=dark_bg, fg='white')
		# lbl60.config(bg=dark_bg, fg='white')
		# lbl61.config(bg=dark_bg, fg='blue')
		# lbl62.config(bg=dark_bg, fg='white')
		# lbl63.config(bg=dark_bg, fg='white')
		# lbl64.config(bg=dark_bg, fg='white')
		# lbl65.config(bg=dark_bg, fg='white')
		# dis.config(bg=dark_bg, fg='green')

		lbl66.config(bg=dark_bg)
		lbl67.config(bg=dark_bg, fg='white')
		lbl68.config(bg=dark_bg, fg='white')
		lbl69.config(bg=dark_bg, fg='white')
		lbl70.config(bg=dark_bg, fg='white')
		lbl71.config(bg=dark_bg, fg='white')
		lbl72.config(bg=dark_bg, fg='white')
		lbl73.config(bg=dark_bg, fg='white')
		lbl74.config(bg=dark_bg, fg='white')
		lbl75.config(bg=dark_bg, fg='white')
		lbl76.config(bg=dark_bg, fg='white')
		lbl77.config(bg=dark_bg, fg='white')
		lbl78.config(bg=dark_bg, fg='white')
		lbl79.config(bg=dark_bg, fg='white')
		lbl80.config(bg=dark_bg, fg='white')
		lbl81.config(bg=dark_bg, fg='white')
		lbl82.config(bg=dark_bg, fg='white')
		lbl83.config(bg=dark_bg)
		lbl84.config(bg=dark_bg, fg='white')
		lbl85.config(bg=dark_bg, fg='white')
		lbl86.config(bg=dark_bg, fg='white')
		lbl87.config(bg=dark_bg, fg='white')
		lbl88.config(bg=dark_bg, fg='white')
		lbl89.config(bg=dark_bg, fg='white')
		lbl90.config(bg=dark_bg, fg='white')
		lbl91.config(bg=dark_bg, fg='white')
		lbl92.config(bg=dark_bg, fg='white')
		lbl93.config(bg=dark_bg, fg='white')
		lbl94.config(bg=dark_bg, fg='white')
		lbl95.config(bg=dark_bg, fg='white')
		lbl96.config(bg=dark_bg, fg='white')
		lbl97.config(bg=dark_bg, fg='white')
		lbl98.config(bg=dark_bg, fg='white')
		lbl99.config(bg=dark_bg, fg='white')
		lbl100.config(bg=dark_bg, fg='white')
		#lbl101.config(bg=dark_bg, fg='white')
		lbl102.config(bg=dark_bg)
		lbl103.config(bg=dark_bg, fg='white')
		lbl104.config(bg=dark_bg, fg='white')
		lbl105.config(bg=dark_bg, fg='white')
		lbl106.config(bg=dark_bg, fg='white')
		lbl107.config(bg=dark_bg, fg='white')
		lbl108.config(bg=dark_bg, fg='white')
		lbl109.config(bg=dark_bg, fg='white')
		lbl110.config(bg=dark_bg)
		lbl111.config(bg=dark_bg, fg='white')
		lbl112.config(bg=dark_bg, fg='white')
		lbl113.config(bg=dark_bg, fg='white')
		lbl114.config(bg=dark_bg, fg='white')
		lbl115.config(bg=dark_bg, fg='white')
		lbl116.config(bg=dark_bg, fg='white')
		lbl117.config(bg=dark_bg, fg='white')
		btn1.config(fg='blue', bg=dark_bg)
		btn2.config(fg='blue', bg=dark_bg)
		btn3.config(fg='blue', bg=dark_bg)
		btn4.config(fg='blue', bg=dark_bg)
		messagebox.showinfo('Done', 'Dark Mode Activated!')
		state = False
	else:
		s.configure('TFrame', background=bgcolor)
		lbl1.config(bg=bgcolor)
		theme_btn.config(image=dark_img, bg=bgcolor)
		lbl2.config(bg=bgcolor, fg=fgcolor2)
		lbl3.config(bg=bgcolor, fg=fgcolor2)
		lbl4.config(bg=bgcolor, fg=fgcolor2)
		lbl5.config(bg=bgcolor, fg=fgcolor2)
		lbl6.config(bg=bgcolor, fg=fgcolor2)
		lbl7.config(bg=bgcolor, fg=fgcolor2)
		lbl8.config(bg=bgcolor, fg=fgcolor2)
		lbl9.config(bg=bgcolor, fg=fgcolor2)
		lbl10.config(bg=bgcolor, fg=fgcolor2)
		lbl11.config(bg=bgcolor, fg=fgcolor2)
		lbl12.config(bg=bgcolor, fg=fgcolor2)
		lbl13.config(bg=bgcolor, fg=fgcolor2)
		lbl14.config(bg=bgcolor, fg=fgcolor2)
		lbl15.config(bg=bgcolor, fg=fgcolor2)
		cpu.config(bg=bgcolor, fg=fgcolor2)
		btry.config(bg=bgcolor)
		usr.config(bg=bgcolor, fg=fgcolor2)

		lbl16.config(bg=bgcolor)
		lbl17.config(bg=bgcolor, fg=fgcolor2)
		lbl18.config(bg=bgcolor, fg=fgcolor2)
		lbl19.config(bg=bgcolor, fg=fgcolor2)
		lbl20.config(bg=bgcolor, fg=fgcolor2)
		lbl21.config(bg=bgcolor, fg=fgcolor2)
		lbl22.config(bg=bgcolor, fg=fgcolor2)
		lbl23.config(bg=bgcolor, fg=fgcolor2)
		lbl24.config(bg=bgcolor, fg=fgcolor2)
		lbl25.config(bg=bgcolor, fg=fgcolor2)
		lbl26.config(bg=bgcolor, fg=fgcolor2)
		lbl27.config(bg=bgcolor, fg=fgcolor2)
		lbl28.config(bg=bgcolor, fg=fgcolor2)
		lbl29.config(bg=bgcolor, fg=fgcolor2)
		lbl30.config(bg=bgcolor, fg=fgcolor2)
		lbl31.config(bg=bgcolor, fg=fgcolor2)
		lbl32.config(bg=bgcolor, fg=fgcolor2)
		lbl33.config(bg=bgcolor, fg=fgcolor2)
		lbl34.config(bg=bgcolor, fg=fgcolor2)
		lbl35.config(bg=bgcolor, fg=fgcolor2)
		lbl36.config(bg=bgcolor, fg=fgcolor2)
		lbl37.config(bg=bgcolor, fg=fgcolor2)
		lbl38.config(bg=bgcolor, fg=fgcolor2)
		lbl39.config(bg=bgcolor, fg=fgcolor2)
		lbl40.config(bg=bgcolor, fg=fgcolor2)

		lbl41.config(bg=bgcolor)
		lbl42.config(bg=bgcolor, fg='blue')
		lbl43.config(bg=bgcolor, fg=fgcolor2)
		lbl44.config(bg=bgcolor, fg=fgcolor2)
		lbl45.config(bg=bgcolor, fg=fgcolor2)
		lbl46.config(bg=bgcolor, fg=fgcolor2)
		lbl47.config(bg=bgcolor, fg='blue')
		lbl48.config(bg=bgcolor, fg=fgcolor2)
		lbl49.config(bg=bgcolor, fg=fgcolor2)
		lbl50.config(bg=bgcolor, fg=fgcolor2)
		lbl51.config(bg=bgcolor, fg=fgcolor2)
		lbl52.config(bg=bgcolor, fg=fgcolor2)
		ram.config(bg=bgcolor, fg=fgcolor2)
		tot_ram.config(bg=bgcolor, fg=fgcolor2)
		usd_ram.config(bg=bgcolor, fg=fgcolor2)
		free_ram.config(bg=bgcolor, fg=fgcolor2)
		swap_per.config(bg=bgcolor, fg=fgcolor2)
		tot_swap.config(bg=bgcolor, fg=fgcolor2)
		usd_swap.config(bg=bgcolor, fg=fgcolor2)
		free_swap.config(bg=bgcolor, fg=fgcolor2)

		#frame.config(bg=bgcolor)
		# lbl53.config(bg=bgcolor)
		# lbl54.config(bg=bgcolor, fg='blue')
		# lbl55.config(bg=bgcolor, fg=fgcolor2)
		# lbl56.config(bg=bgcolor, fg=fgcolor2)
		# lbl57.config(bg=bgcolor, fg=fgcolor2)
		# lbl58.config(bg=bgcolor, fg=fgcolor2)
		# lbl59.config(bg=bgcolor, fg=fgcolor2)
		# lbl60.config(bg=bgcolor, fg=fgcolor2)
		# lbl61.config(bg=bgcolor, fg='blue')
		# lbl62.config(bg=bgcolor, fg=fgcolor2)
		# lbl63.config(bg=bgcolor, fg=fgcolor2)
		# lbl64.config(bg=bgcolor, fg=fgcolor2)
		# lbl65.config(bg=bgcolor, fg=fgcolor2)
		# dis.config(bg=bgcolor, fg='green')

		lbl66.config(bg=bgcolor)
		lbl67.config(bg=bgcolor, fg=fgcolor2)
		lbl68.config(bg=bgcolor, fg=fgcolor2)
		lbl69.config(bg=bgcolor, fg=fgcolor2)
		lbl70.config(bg=bgcolor, fg=fgcolor2)
		lbl71.config(bg=bgcolor, fg=fgcolor2)
		lbl72.config(bg=bgcolor, fg=fgcolor2)
		lbl73.config(bg=bgcolor, fg=fgcolor2)
		lbl74.config(bg=bgcolor, fg=fgcolor2)
		lbl75.config(bg=bgcolor, fg=fgcolor2)
		lbl76.config(bg=bgcolor, fg=fgcolor2)
		lbl77.config(bg=bgcolor, fg=fgcolor2)
		lbl78.config(bg=bgcolor, fg=fgcolor2)
		lbl79.config(bg=bgcolor, fg=fgcolor2)
		lbl80.config(bg=bgcolor, fg=fgcolor2)
		lbl81.config(bg=bgcolor, fg=fgcolor2)
		lbl82.config(bg=bgcolor, fg=fgcolor2)
		lbl83.config(bg=bgcolor)
		lbl84.config(bg=bgcolor, fg=fgcolor2)
		lbl85.config(bg=bgcolor, fg=fgcolor2)
		lbl86.config(bg=bgcolor, fg=fgcolor2)
		lbl87.config(bg=bgcolor, fg=fgcolor2)
		lbl88.config(bg=bgcolor, fg=fgcolor2)
		lbl89.config(bg=bgcolor, fg=fgcolor2)
		lbl90.config(bg=bgcolor, fg=fgcolor2)
		lbl91.config(bg=bgcolor, fg=fgcolor2)
		lbl92.config(bg=bgcolor, fg=fgcolor2)
		lbl93.config(bg=bgcolor, fg=fgcolor2)
		lbl94.config(bg=bgcolor, fg=fgcolor2)
		lbl95.config(bg=bgcolor, fg=fgcolor2)
		lbl96.config(bg=bgcolor, fg=fgcolor2)
		lbl97.config(bg=bgcolor, fg=fgcolor2)
		lbl98.config(bg=bgcolor, fg=fgcolor2)
		lbl99.config(bg=bgcolor, fg=fgcolor2)
		lbl100.config(bg=bgcolor, fg=fgcolor2)
		#lbl101.config(bg=bgcolor, fg=fgcolor2)
		lbl102.config(bg=bgcolor)
		lbl103.config(bg=bgcolor, fg=fgcolor2)
		lbl104.config(bg=bgcolor, fg=fgcolor2)
		lbl105.config(bg=bgcolor, fg=fgcolor2)
		lbl106.config(bg=bgcolor, fg=fgcolor2)
		lbl107.config(bg=bgcolor, fg=fgcolor2)
		lbl108.config(bg=bgcolor, fg=fgcolor2)
		lbl109.config(bg=bgcolor, fg=fgcolor2)
		lbl109.config(bg=bgcolor, fg=fgcolor2)
		lbl110.config(bg=bgcolor)
		lbl111.config(bg=bgcolor, fg=fgcolor2)
		lbl112.config(bg=bgcolor, fg=fgcolor2)
		lbl113.config(bg=bgcolor, fg=fgcolor2)
		lbl114.config(bg=bgcolor, fg=fgcolor2)
		lbl115.config(bg=bgcolor, fg=fgcolor2)
		lbl116.config(bg='black', fg='white')
		lbl117.config(bg=bgcolor, fg=fgcolor2)
		btn1.config(fg='blue', bg=bgcolor)
		btn2.config(fg='blue', bg=bgcolor)
		btn3.config(fg='blue', bg=bgcolor)
		btn4.config(fg='blue', bg=bgcolor)
		messagebox.showinfo('Done', 'Light Mode Activated!')
		state = True

# main interface
def main() -> None:
	root = Tk()
	root.title("PC Manager 3")

	width_of_window = 1200
	height_of_window = 700
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x_cordinate = (screen_width / 2) - (width_of_window / 2)
	y_cordinate = (screen_height / 2) - (height_of_window / 2)

	root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate))

	root.iconbitmap('icon.ico')
	root.resizable(0, 0)

	# greeting
	messagebox.showinfo('Welcome', f'Hello, {user}')

	def battery() -> None:
		if not hasattr(psutil, "sensors_battery"):
			#return sys.exit("platform not supported")
			btry.config(text='Platform not supported')
		batt = psutil.sensors_battery()
		if batt is None:
			btry.config(text='No battery is installed', fg='#ff0000')
			#return sys.exit("no battery is installed")
		else:
			btry.config(text=("Charge:     %s%%" % round(batt.percent, 2)), fg='#00ff00')
			btry.after(1000, battery)
			#print("charge:     %s%%" % round(batt.percent, 2))
   
	def upTime() -> None:
		lib = ctypes.windll.kernel32
		t = lib.GetTickCount64()
		t = int(str(t)[:-3])

		mins, sec = divmod(t, 60)
		hours, mins = divmod(mins, 60)
		days, hours = divmod(hours, 24)
		if days == 0:
			usr.config(text=f'{hours} hours, {mins} minutes, {sec} seconds')
		else:
			usr.config(text=f'{days} days, {hours} hours, {mins} minutes, {sec} seconds')
		usr.after(1000, upTime)

	def size(byte) -> str | None:
		for x in ['B', 'KB', 'MB', 'GB', 'TB']:
			if byte < 1024:
				return f'{byte:.2f}{x}'
			byte = byte / 1024

	def swapPer() -> None:
		swap_per.config(text=f'{swap.percent}%')
		swap_per.after(1000, swapPer)

	def total_swap() -> None:
		tot_swap.config(text=f'{size(swap.total)}')
		tot_swap.after(1000, total_swap)

	def used_swap() -> None:
		usd_swap.config(text=f'{size(swap.used)}')
		usd_swap.after(1000, used_swap)

	def free__swap() -> None:
		free_swap.config(text=f'{size(swap.free)}')
		free_swap.after(1000, free__swap)

	def cpu_check() -> None:
		cpu_data = psutil.cpu_percent()
		cpu.config(text=str(cpu_data)+"%")
		cpu.after(1000, cpu_check)

	def ramcheck() -> None:
		per_ram = psutil.virtual_memory().percent
		ram.config(text=str(per_ram)+'%')
		ram.after(1000, ramcheck)

	def totRam() -> None:
		total_ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
		tot_ram.config(text=str(total_ram)+'GB (usable)')
		tot_ram.after(1000, totRam)

	def useRam() -> None:
		used_ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
		usd_ram.config(text=str(used_ram)+'GB')
		usd_ram.after(1000, useRam)

	def freeRam() -> None:
		freeram = round((psutil.virtual_memory().free) / (1024 ** 3), 2)
		free_ram.config(text=str(freeram)+'GB')
		free_ram.after(1000, freeRam)

	# images
	cpu_img = Image.open('images/cpu.png')
	cpu_img = cpu_img.resize((150, 150))
	cpu_img = ImageTk.PhotoImage(cpu_img)

	gpu_img = Image.open('images/graphics-card.png')
	gpu_img = gpu_img.resize((200, 200))
	gpu_img = ImageTk.PhotoImage(gpu_img)

	os_img1 = Image.open('images/windows.png')
	os_img1 = os_img1.resize((120, 120))
	os_img1 = ImageTk.PhotoImage(os_img1)

	os_img2 = Image.open('images/linux.png')
	os_img2 = os_img2.resize((120, 120))
	os_img2 = ImageTk.PhotoImage(os_img2)

	ram_img = Image.open('images/ram-memory.png')
	ram_img = ram_img.resize((150, 150))
	ram_img = ImageTk.PhotoImage(ram_img)

	hdd_img = Image.open('images/hard-disk.png')
	hdd_img = hdd_img.resize((150, 150))
	hdd_img = ImageTk.PhotoImage(hdd_img)



	# ttk styling
	s = ttk.Style()
	s.configure('TNotebook.Tab', font=('Calibri', 10))
	s.configure('TButton', font=('Ubuntu', 16), foreground='#204db2')
	s.configure('TFrame', background=bgcolor)
	'''s.theme_create("yummy", parent='alt', settings={
		"TNotebook.Tab": {
			"configure": {"background": '204db2', '#cf3237'}
		}})
	s.theme_use("yummy")'''
	# structure
	tabs = ttk.Notebook(root)
	tabs.pack(fill=BOTH, pady=5, expand=True)

	tab1 = ttk.Frame(tabs, width=1200, height=750)
	tab2 = ttk.Frame(tabs, width=1200, height=750)
	tab3 = ttk.Frame(tabs, width=1200, height=750)
	# tab4 = ttk.Frame(tabs, width=1200, height=750)
	tab5 = ttk.Frame(tabs, width=1200, height=750)
	tab6 = ttk.Frame(tabs, width=1200, height=750)
	tab7 = ttk.Frame(tabs, width=1200, height=750)
	tab8 = ttk.Frame(tabs, width=1200, height=750)

	tabs.add(tab1, text='Dashboard')
	tabs.add(tab2, text='Processor')
	tabs.add(tab3, text='Memory')
	# tabs.add(tab4, text='Storage')
	tabs.add(tab5, text='O. S.')
	tabs.add(tab6, text='Graphics')
	tabs.add(tab7, text='Utilities')
	tabs.add(tab8, text='About Us')

	# images for theme changer
	light_img = Image.open('images/light.png').resize((40, 40))
	light_img = ImageTk.PhotoImage(light_img)

	dark_img = Image.open('images/dark.png').resize((40, 40))
	dark_img = ImageTk.PhotoImage(dark_img)

	######## TAB 1 - Dashboard ########
	lbl1 = Label(tab1, text='DASHBOARD', font='Poppins 40 bold', fg=fgcolor, bg=bgcolor)
	lbl1.pack()
	lbl2 = Label(tab1, text='Current Time/Date:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl2.place(x=15, y=180)
	lbl3 = Label(tab1, text='Computer Name:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl3.place(x=15, y=240)
	lbl4 = Label(tab1, text='User:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl4.place(x=15, y=300)
	lbl5 = Label(tab1, text='Up Time:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl5.place(x=15, y=360)
	usr = Label(tab1, font='arial 18', fg=fgcolor2, bg=bgcolor)
	usr.place(x=280, y=360)
	lbl6 = Label(tab1, text='Processor:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl6.place(x=15, y=420)
	lbl7 = Label(tab1, text='System Memory:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl7.place(x=15, y=480)
	lbl8 = Label(tab1, text='Operating System:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl8.place(x=15, y=540)
	lbl9 = Label(tab1, text='Battery:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl9.place(x=15, y=600)
	btry = Label(tab1, font='arial 18', fg=fgcolor2, bg=bgcolor)
	btry.place(x=280, y=600)

	lbl10 = Label(tab1, text=f"{datetime.datetime.now().strftime('%I:%M:%S %p')}, {datetime.date.today().strftime('%d.%m.%Y')}", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl10.place(x=280, y=180)
	lbl11 = Label(tab1, text=f'{pc_name}', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl11.place(x=280, y=240)
	lbl12 = Label(tab1, text=f'{user}', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl12.place(x=280, y=300)
	lbl13 = Label(tab1, text=f'{cpu_data}', font='arial 15', fg=fgcolor2, bg=bgcolor)
	lbl13.place(x=280, y=420)
	lbl14 = Label(tab1, text=f'{ram_data}GB (Usable)', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl14.place(x=280, y=480)
	lbl15 = Label(tab1, text=f'{os_name}', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl15.place(x=280, y=540)


	# Button to change the theme
	state = True
	theme_btn = Button(tab1, image=dark_img, bd=0, fg='white', bg=bgcolor, command=theme_changer)
	theme_btn.place(x=1100, y=30)

	## Buttons in Parent Tab (Dashboard)
	ttk.Button(tab1, text='Shut down', width=15, command=shutdown, cursor="hand2").place(x=980, y=250)
	ttk.Button(tab1, text='Restart', width=15, command=restart, cursor="hand2").place(x=980, y=300)
	ttk.Button(tab1, text='Log Off', width=15, command=log_off, cursor="hand2").place(x=980, y=350)
	ttk.Button(tab1, text='Hibernate', width=15, command=hibernate, cursor="hand2").place(x=980, y=400)
	ttk.Button(tab1, text='Lock', width=15, command=lock, cursor="hand2").place(x=980, y=450)

	########					########

	######## TAB 2 - Processor ########
	lbl16 = Label(tab2, text='PROCESSOR', font='Poppins 40 bold', fg=fgcolor, bg=bgcolor)
	lbl16.pack()
	lbl17 = Label(tab2, text='Utilization:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl17.place(x=15, y=140)
	cpu = Label(tab2, font='arial 18', fg=fgcolor2, bg=bgcolor)
	cpu.place(x=308, y=140)
	lbl18 = Label(tab2, text='Processor:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl18.place(x=15, y=180)
	lbl19 = Label(tab2, text='Manufacturer:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl19.place(x=15, y=220)
	lbl20 = Label(tab2, text='Cores:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl20.place(x=15, y=260)
	lbl21 = Label(tab2, text='Threads:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl21.place(x=15, y=300)
	lbl22 = Label(tab2, text='Architecture:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl22.place(x=15, y=340)
	lbl23 = Label(tab2, text='Clock Speed:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl23.place(x=15, y=380)
	lbl24 = Label(tab2, text='Machine:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl24.place(x=15, y=420)
	lbl25 = Label(tab2, text='CPU Socket:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl25.place(x=15, y=460)
	lbl26 = Label(tab2, text='Processor ID:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl26.place(x=15, y=500)
	lbl27 = Label(tab2, text='Description:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl27.place(x=15, y=540)
	lbl28 = Label(tab2, text='Virtualization:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl28.place(x=15, y=580)

	lbl29 = Label(tab2, text=cpu_data, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl29.place(x=308, y=180)
	lbl30 = Label(tab2, text=man, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl30.place(x=308, y=220)
	lbl31 = Label(tab2, text=cpu_cores, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl31.place(x=308, y=260)
	lbl32 = Label(tab2, text=cpu_threads, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl32.place(x=308, y=300)
	lbl33 = Label(tab2, text=arch, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl33.place(x=308, y=340)
	lbl34 = Label(tab2, text=f'{clock/1000}GHz ({clock}MHz)', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl34.place(x=308, y=380)
	lbl35 = Label(tab2, text=machine, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl35.place(x=308, y=420)
	lbl36 = Label(tab2, text=soket, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl36.place(x=308, y=460)
	lbl37 = Label(tab2, text=pc.Win32_Processor()[0].ProcessorId, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl37.place(x=308, y=500)
	lbl38 = Label(tab2, text=pc.Win32_Processor()[0].Description, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl38.place(x=308, y=540)
	lbl39 = Label(tab2, text=virt, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl39.place(x=308, y=580)

	lbl40 = Label(tab2, image=cpu_img, bd=0, bg=bgcolor)
	lbl40.pack(side=RIGHT, padx=40)

	########					########

	######## TAB 3 - Memory ########
	lbl41 = Label(tab3, text='MEMORY', font='Poppins 40 bold', fg=fgcolor, bg=bgcolor)
	lbl41.pack()
	lbl42 = Label(tab3, text='Physical Memory Information', font='Poppins 25', fg='blue', bg=bgcolor)
	lbl42.place(x=15, y=140)
	lbl43 = Label(tab3, text='Utilization:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl43.place(x=15, y=220)
	ram = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	ram.place(x=250, y=220)

	lbl44 = Label(tab3, text='Total RAM:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl44.place(x=15, y=280)
	tot_ram = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	tot_ram.place(x=250, y=280)

	lbl45 = Label(tab3, text='Used RAM:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl45.place(x=15, y=340)
	usd_ram = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	usd_ram.place(x=250, y=340)

	lbl46 = Label(tab3, text='Free RAM:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl46.place(x=15, y=390)
	free_ram = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	free_ram.place(x=250, y=390)



	lbl47 = Label(tab3, text='SWAP Memory Information', font='Poppins 25', fg='blue', bg=bgcolor)
	lbl47.place(x=720, y=140)
	lbl48 = Label(tab3, text='Utilization:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl48.place(x=720, y=220)
	swap_per = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	swap_per.place(x=950, y=220)

	lbl49 = Label(tab3, text='Total SWAP:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl49.place(x=720, y=280)
	tot_swap = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	tot_swap.place(x=950, y=280)

	lbl50 = Label(tab3, text='Used SWAP:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl50.place(x=720, y=340)
	usd_swap = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	usd_swap.place(x=950, y=340)

	lbl51 = Label(tab3, text='Free SWAP:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl51.place(x=720, y=390)
	free_swap = Label(tab3, font='arial 18', fg=fgcolor2, bg=bgcolor)
	free_swap.place(x=950, y=390)
	lbl52 = Label(tab3, image=ram_img, bd=0, bg=bgcolor)
	lbl52.pack(side=BOTTOM, pady=30)
	########					########

	# ######## TAB 4 - Storage ########
	# frame = ttk.Frame(tab4, width=550, height=700)
	# frame.place(x=580, y=240)

	# lbl53 = Label(tab4, text='STORAGE', font='Poppins 40 bold', fg=fgcolor, bg=bgcolor)
	# lbl53.pack()
	# lbl54 = Label(tab4, text='Disk Information', font='Poppins 25', fg='blue', bg=bgcolor)
	# lbl54.place(x=15, y=140)
	# #Label(tab4, text='Capacity:', font='arial 18', fg=fgcolor2, bg=bgcolor).place(x=15, y=200)
	# lbl55 = Label(tab4, text='Usable:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl55.place(x=15, y=200)
	# lbl56 = Label(tab4, text='Used:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl56.place(x=15, y=260)
	# lbl57 = Label(tab4, text='Free:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl57.place(x=15, y=320)

	#Label(tab4, text=f'{hdd_actual_size}GB', font='arial 18', fg=fgcolor2, bg=bgcolor).place(x=180, y=200)
	# lbl58 = Label(tab4, text=f'{hdd_usable_size}GB', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl58.place(x=180, y=200)
	# lbl59 = Label(tab4, text=f'{hdd_used_size}GB', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl59.place(x=180, y=260)
	# lbl60 = Label(tab4, text=f'{hdd_free_size}GB', font='arial 18', fg=fgcolor2, bg=bgcolor)
	# lbl60.place(x=180, y=320)

	# lbl61 = Label(tab4, text='Disk Partitions', font='Poppins 25', fg='blue',  bg=bgcolor)
	# lbl61.place(x=580, y=140)
	# lbl62 = Label(tab4, text='Disk', font='Poppins 19', fg=fgcolor2, bg=bgcolor)
	# lbl62.place(x=580, y=200)
	# lbl63 = Label(tab4, text='Used', font='Poppins 19', fg=fgcolor2, bg=bgcolor)
	# lbl63.place(x=790, y=200)
	# lbl64 = Label(tab4, text='Free', font='Poppins 19', fg=fgcolor2, bg=bgcolor)
	# lbl64.place(x=990, y=200)
	# lbl65 = Label(tab4, image=hdd_img, bd=0, bg=bgcolor)
	# lbl65.pack(side=BOTTOM, pady=30)
	########					########

	######## TAB 5 - OS ########
	lbl66 = Label(tab5, text='OPERATING SYSTEM', font='Poppins 40 bold', fg=fgcolor,bg=bgcolor)
	lbl66.pack()
	lbl67 = Label(tab5, text='OS Name:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl67.place(x=15, y=180)
	lbl68 = Label(tab5, text='Version:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl68.place(x=15, y=240)
	lbl69 = Label(tab5, text='OS Build:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl69.place(x=15, y=300)
	lbl70 = Label(tab5, text='Manufacturer:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl70.place(x=15, y=360)
	lbl71 = Label(tab5, text='Language:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl71.place(x=15, y=420)
	lbl72 = Label(tab5, text='System Directory:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl72.place(x=15, y=540)
	lbl73 = Label(tab5, text='Windows Directory:', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl73.place(x=15, y=480)

	lbl74 = Label(tab5, text=os_name, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl74.place(x=300, y=180)
	lbl75 = Label(tab5, text=os_version, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl75.place(x=300, y=240)
	lbl76 = Label(tab5, text=os_build, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl76.place(x=300, y=300)
	lbl77 = Label(tab5, text=os_man, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl77.place(x=300, y=360)
	lbl78 = Label(tab5, text=os_lang, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl78.place(x=300, y=420)
	lbl79 = Label(tab5, text=os_sys_dir, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl79.place(x=300, y=540)
	lbl80 = Label(tab5, text=os_win_dir, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl80.place(x=300, y=480)

	lbl81 = Label(tab5, image=os_img2, bd=0, bg=bgcolor)
	lbl81.pack(side=RIGHT, padx=40)
	lbl82 = Label(tab5, image=os_img1, bd=0, bg=bgcolor)
	lbl82.pack(side=RIGHT, padx=40)

	######## TAB 6 - Graphics ########
	lbl83 = Label(tab6, text='GRAPHICS', font='Poppins 40 bold', fg=fgcolor,bg=bgcolor)
	lbl83.pack()

	lbl84 = Label(tab6, text="Video Processor:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl84.place(x=15, y=180)
	lbl85 = Label(tab6, text="Manufacturer:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl85.place(x=15, y=240)
	lbl86 = Label(tab6, text="Type:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl86.place(x=15, y=300)
	lbl87 = Label(tab6, text="Resolution:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl87.place(x=15, y=360)
	lbl88 = Label(tab6, text="Refresh Rate:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl88.place(x=15, y=420)
	lbl89 = Label(tab6, text="Video Mode:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl89.place(x=15, y=480)
	lbl90 = Label(tab6, text="Bits Per Pixel:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl90.place(x=15, y=540)
	lbl91 = Label(tab6, text="Driver Verion:", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl91.place(x=15, y=600)

	res = f'{pc.Win32_VideoController()[0].CurrentHorizontalResolution} x {pc.Win32_VideoController()[0].CurrentVerticalResolution}'
	lbl92 = Label(tab6, text=pc.Win32_VideoController()[0].VideoProcessor, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl92.place(x=300, y=180)
	lbl93 = Label(tab6, text=pc.Win32_VideoController()[0].AdapterCompatibility, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl93.place(x=300, y=240)
	lbl94 = Label(tab6, text=pc.Win32_VideoController()[0].AdapterDACType, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl94.place(x=300, y=300)
	lbl95 = Label(tab6, text=res, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl95.place(x=300, y=360)
	lbl96 = Label(tab6, text=str(pc.Win32_VideoController()[0].CurrentRefreshRate)+"Hz", font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl96.place(x=300, y=420)
	lbl97 = Label(tab6, text=pc.Win32_VideoController()[0].VideoModeDescription, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl97.place(x=300, y=480)
	lbl98 = Label(tab6, text=pc.Win32_VideoController()[0].CurrentBitsPerPixel, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl98.place(x=300, y=540)
	lbl99 = Label(tab6, text=pc.Win32_VideoController()[0].DriverVersion, font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl99.place(x=300, y=600)

	lbl100 = Label(tab6, image=gpu_img, bd=0, bg=bgcolor)
	lbl100.pack(side=RIGHT, padx=50)
	########					########

	######## TAB 7 - Utilities ########
	lbl102 = Label(tab7, text='UTILITIES', font='Poppins 40 bold', fg=fgcolor,bg=bgcolor)
	lbl102.pack()
	ttk.Button(tab7, text='Disk Cleanup', command=cleanup, width=25, cursor="hand2").place(x=35, y=180)
	lbl103 = Label(tab7, text='Cleanup Junk Fils with just few clicks', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl103.place(x=380, y=180)
	ttk.Button(tab7, text='Computer Managment', command=ctrl, width=25, cursor="hand2").place(x=35, y=240)
	lbl104 = Label(tab7, text='Manage your computer', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl104.place(x=380, y=240)
	ttk.Button(tab7, text='Disk Defragment', command=defrag, width=25, cursor="hand2").place(x=35, y=300)
	lbl105 = Label(tab7, text='Defrag the Hard Disk to keep your PC Faster', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl105.place(x=380, y=300)
	ttk.Button(tab7, text='System Information', command=sys_info, width=25, cursor="hand2").place(x=35, y=360)
	lbl106 = Label(tab7, text='Get advanced details about your computer', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl106.place(x=380, y=360)
	ttk.Button(tab7, text='Add/ Remove Apps', command=add_rem, width=25, cursor="hand2").place(x=35, y=420)
	lbl107 = Label(tab7, text='Remove unwanted applications from your computer', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl107.place(x=380, y=420)
	ttk.Button(tab7, text='About Windows', command=win, width=25, cursor="hand2").place(x=35, y=480)
	lbl108 = Label(tab7, text='Get details about the main operating system', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl108.place(x=380, y=480)
	ttk.Button(tab7, text='System Restore', command=restore, width=25, cursor="hand2").place(x=35, y=540)
	lbl109 = Label(tab7, text='Keep your computer safe with system restore feature', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl109.place(x=380, y=540)
	########					########

	######## TAB 8 - About Us ########
	img1 = Image.open('images/img.png')
	img1 = img1.resize((250, 250))
	img1 = ImageTk.PhotoImage(img1)

	lbl110 = Label(tab8, text='ABOUT US', font='Poppins 40 bold', fg=fgcolor, bg=bgcolor)
	lbl110.pack()
	lbl111 = Label(tab8, text='Thank you for choosing our software for your Computer!', font='arial 20', fg=fgcolor2, bg=bgcolor)
	lbl111.place(x=15, y=180)
	lbl112 = Label(tab8, text='Dasun Nethsara', font='arial 18', fg=fgcolor2, bg=bgcolor)
	lbl112.place(x=15, y=250)
	lbl113 = Label(tab8, image=img1, bd=0)
	lbl113.place(x=860, y=230)
	lbl114 = Label(tab8, text='Certified in Python Programming', font='Consolas 13', fg=fgcolor2, bg=bgcolor)
	lbl114.place(x=15, y=280)
	lbl115 = Label(tab8, text='Certified in Web Development (HTML, CSS, PHP)', font='Consolas 13', fg=fgcolor2, bg=bgcolor)
	lbl115.place(x=15, y=305)
	lbl116 = Label(tab8, text=f'© Dasun Nethsara {datetime.date.today().year}', font='Consolas 15', bg='black', fg='white')
	lbl116.pack(side=BOTTOM, fill=X)

	lbl117 = Label(tab8, text='Contact me on', font='Poppins 20', fg=fgcolor2, bg=bgcolor)
	lbl117.place(x=15, y=340)
	btn1 = Button(tab8, text='Tech SARA LK (Web)', bd=0, font='Ubuntu 15 underline', fg='blue', command=web, cursor="hand2", bg=bgcolor)
	btn1.place(x=35, y=400)
	btn2 = Button(tab8, text='GitHub', bd=0, font='Ubuntu 15 underline', fg='blue', command=github, cursor="hand2",bg=bgcolor)
	btn2.place(x=35, y=450)
	btn3 = Button(tab8, text='Telegram', bd=0, font='Ubuntu 15 underline', fg='blue', command=telegram, cursor="hand2",bg=bgcolor)
	btn3.place(x=35, y=500)
	btn4 = Button(tab8, text='YouTube', bd=0, font='Ubuntu 15 underline', fg='blue', command=youtube, cursor="hand2",bg=bgcolor)
	btn4.place(x=35, y=550)

	upTime()
	battery()
	cpu_check()
	ramcheck()
	totRam()
	useRam()
	freeRam()
	swapPer()
	total_swap()
	used_swap()
	free__swap()

	root.protocol("WM_DELETE_WINDOW", lambda: on_minimize(root))
	# run and looping the main user interface
	root.mainloop()
	########					########

if __name__ == "__main__":
	main()
	