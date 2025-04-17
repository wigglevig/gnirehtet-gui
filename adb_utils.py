import subprocess
def get_connected_devices():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    # print(f"ADB devices output: {result.stdout}")  # Debugging line
    lines = result.stdout.strip().split('\n')[1:]  # skip the first line
    devices = [line.split()[0] for line in lines if 'device' in line]
    
    return devices
