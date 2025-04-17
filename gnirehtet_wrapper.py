import subprocess
import os

gnirehtet_process = None  # Global variable to hold the process

def start_gnirehtet():
    global gnirehtet_process
    exe_path = os.path.join(os.getcwd(), 'gnirehtet.exe')
    gnirehtet_process = subprocess.Popen([exe_path, 'run'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def stop_gnirehtet():
    global gnirehtet_process
    if gnirehtet_process is not None:
        gnirehtet_process.terminate()
        try:
            gnirehtet_process.wait(timeout=5)
        except Exception:
            gnirehtet_process.kill()
        gnirehtet_process = None