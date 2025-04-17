import tkinter as tk
from tkinter import messagebox
from adb_utils import get_connected_devices
from gnirehtet_wrapper import start_gnirehtet, stop_gnirehtet
import threading
class GnirehtetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gnirehtet Controller")
        
        self.device_list = tk.StringVar()
        self.status_label = tk.Label(root, text="Devices: ")
        self.status_label.pack()
        
        self.refresh_devices()
        
        self.start_btn = tk.Button(root, text="Start Gnirehtet", command=self.start_gnirehtet)
        self.start_btn.pack(pady=5)
        self.stop_btn = tk.Button(root, text="Stop Gnirehtet", command=self.stop_gnirehtet)
        self.stop_btn.pack(pady=5)

    def refresh_devices(self):
        devices = get_connected_devices()
        self.device_list.set(", ".join(devices) if devices else "No device")
        self.status_label.config(text=f"Connected: {self.device_list.get()}")

    def _run_gnirehtet(self):
        start_gnirehtet()

    
    def start_gnirehtet(self):
        self.refresh_devices()
        if self.device_list.get() == "No device":
            messagebox.showerror("Error", "No ADB device connected.")
        else:
            threading.Thread(target=self._run_gnirehtet).start()
            messagebox.showinfo("Success", "Gnirehtet started!")
    
    
    def stop_gnirehtet(self):
        stop_gnirehtet()
        messagebox.showinfo("Stopped", "Gnirehtet stopped.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GnirehtetGUI(root)
    root.mainloop()
