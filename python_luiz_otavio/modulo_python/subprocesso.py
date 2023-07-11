import subprocess
import sys

cmd = ['ping', '127.0.0.1', '-c', '4']

system = sys.platform

if system == 'linux':
    cmd = ["ls -lah /"]

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding="utf-8",
    shell=True,
)

# print(proc.args)
# print(proc.stderr)
# print(proc.stdout.decode('utf-8'))
print(sys.platform)
print(proc.stdout)
# print(proc.returncode)
