import subprocess
import time
import sys
import os

LMS_BIN = r"C:\Users\malda\.lmstudio\bin\lms.exe"

print("1. Starting LM Studio local server...")
res1 = subprocess.run([LMS_BIN, "server", "start"], capture_output=True, text=True)
print("Server start output:", res1.stdout, res1.stderr)

print("2. Loading Qwen2.5-VL-7B with context 4096...")
res2 = subprocess.run([LMS_BIN, "load", "qwen/qwen2.5-vl-7b", "-c", "4096", "--gpu", "off", "-y"], capture_output=True, text=True)
print("Load output:", res2.stdout, res2.stderr)

print("3. Daemon ready! Keeping service alive...")
sys.stdout.flush()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping...")
