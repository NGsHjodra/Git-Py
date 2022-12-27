import subprocess
import os

subprocess.run(['git'] + ['status'])

os.chdir('../C-CPP-Harbour.Space')


subprocess.run(['git'] + ['status'])

directorys = [f for f in os.listdir('.') if os.path.isdir(f)]
for dir in directorys:
    if (dir[0] >= '0' and dir[0] <= '9'):
        for root, dirs, files in os.walk(dir):
            for filename in files:
                if filename == "main.cpp":
                    print(os.path.join(dir, filename))
                    subprocess.run(['git'] + ['add'] + [os.path.join(dir, filename)])

subprocess.run(['git'] + ['status'])

subprocess.run(['git'] + ['commit'] + ['-am'] + ['"add all main.cpp"'])

subprocess.run(['git'] + ['push'])