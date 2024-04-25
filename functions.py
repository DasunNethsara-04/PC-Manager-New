import os, webbrowser
# import disk

def cleanup() -> None:
	"""
    This function opens the Windows System Cleanup tool (cleanmgr.exe).

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    To open the System Cleanup tool, simply call the cleanup() function:

    ```python
    cleanup()
    ```

    This will start the System Cleanup tool, allowing the user to clean up unnecessary files and optimize their system.
    """
	os.startfile('C:\\Windows\\System32\\cleanmgr.exe')

def ctrl() -> None:
	"""
    This function opens the Computer Management console.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    This function uses the os module's startfile function to open the 'compmgmt.msc' file located in the 'C:\\WINDOWS\\System32' directory.

    Example:
    >>> ctrl()
    """
	path = 'C:\\WINDOWS\\System32\\compmgmt.msc'
	os.startfile(os.path.join(path))

def defrag() -> None:
	"""
    This function opens the Windows Disk Defragmenter tool.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    >>> defrag()
    """
	os.startfile('C:\\Windows\\System32\\dfrgui.exe')

def sys_info() -> None:
	"""
    This function opens the System Information window using the 'msinfo32.exe' executable.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    >>> sys_info()
    """
	path = 'C:\\WINDOWS\\System32\\msinfo32.exe'
	os.startfile(os.path.join(path))

def add_rem() -> None:
	"""
    This function opens the 'Add or Remove Programs' window in Windows.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    >>> add_rem()
    """
	path = 'C:\\WINDOWS\\System32\\appwiz.cpl'
	os.startfile(os.path.join(path))

def win() -> None:
	"""
    This function opens the Windows Information dialog.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    >>> win()
    """
	path = 'C:\\WINDOWS\\system32\\winver.exe'
	os.startfile(os.path.join(path))

def restore() -> None:
	"""
    This function opens the System Restore dialog box.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    Example:
    >>> restore()
    """
	os.startfile('C:\\Windows\\System32\\rstrui.exe')

def web() -> None:
	webbrowser.open('https://www.techsaralk.epizy.com/')

def github() -> None:
	webbrowser.open('https://github.com/DasunNethsara-04')

def telegram() -> None:
	webbrowser.open('https://t.me/techsara_lk')

def youtube() -> None:
	webbrowser.open('https://www.youtube.com/channel/UCpWe6k8GxYuLmlzlvX7VBRg')

def shutdown() -> None:
	"""
    This function is used to initiate a system shutdown.

    Parameters:
    None

    Returns:
    None

    Raises:
    This function does not raise any exceptions.

    Example:
    To initiate a system shutdown, simply call the `shutdown()` function.

    ```python
    shutdown()
    ```

    This will execute the `shutdown.exe` command with the `-s` (shutdown) and `-t 00` (immediate) options.
    """
	os.system('shutdown.exe -s -t 00')

def restart() -> None:
	"""
    This function initiates a restart of the system. It uses the 'shutdown.exe' command-line tool to perform the restart operation. The '-r' parameter specifies that a restart should be performed, and the '-t 00' parameter sets the time delay before the restart to zero seconds.

    Parameters:
    None

    Returns:
    None

    Raises:
    This function does not raise any exceptions.

    Example:
    >>> restart()
    """
	os.system('shutdown.exe -r -t 00')

def hibernate() -> None:
	"""
    This function initiates the system hibernation process. It does this by calling the 'rundll32.exe powrprof.dll, SetSuspendState' function with the appropriate parameters.

    Parameters:
    No parameters are required for this function.

    Return value:
    This function does not return any value. It initiates the hibernation process and then exits.

    Raises:
    This function does not raise any exceptions. However, if the 'rundll32.exe powrprof.dll, SetSuspendState' function fails to execute for any reason, the system hibernation process will not be initiated.

    Example:
    To initiate the system hibernation process, simply call the 'hibernate' function:

    ```python
    hibernate()
    ```
    """
	os.system('rundll32.exe powrprof.dll, SetSuspendState')

def lock() -> None:
	"""
    This function is used to lock the system. It initiates the system locking process by invoking the appropriate Windows API function.

    Parameters:
    None

    Returns:
    None

    Raises:
    This function does not raise any exceptions.

    Usage:
    To lock the system, simply call the `lock()` function.

    Example:
    ```python
    from pc_info import lock

    def main():
        # Perform some tasks
        # ...

        # Lock the system
        lock()

    if __name__ == "__main__":
        main()
    ```
    """
	os.system('rundll32.exe user32.dll, LockWorkStation')

def log_off() -> None:
	"""
    This function initiates the system shutdown process. It uses the 'shutdown.exe' command-line tool to execute the 'l' (log off) option.

    Parameters:
    No parameters are required for this function.

    Returns:
    This function does not return any value.

    Raises:
    This function does not raise any exceptions.

    Usage:
    To initiate the system shutdown process, simply call the 'log_off' function.

    Example:
    ```python
    from pc_info import log_off

    # Call the log_off function to initiate the system shutdown process.
    log_off()
    ```
    """
	os.system('shutdown.exe -l')

# dis = ''
# def disk_part():
# 	global lst, dis
# 	for i in psutil.disk_partitions():
# 		if i[2] == "":
# 			continue
# 		drive, percent = i[0], float(psutil.disk_usage(i[0]).percent)
# 		free = round(100 - percent, 2)
# 		dis = Label(frame, text=f'{drive}\t\t{percent}%\t\t{free}%', font='arial 18', fg='green', bg=bgcolor)
# 		dis.pack(pady=10)
