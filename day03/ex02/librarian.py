from asyncore import write
import subprocess
import sys
import os


if __name__ == "__main__":
	if (os.getenv("VIRTUAL_ENV") is None):
		raise Exception("Not venv")
	subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "pytest"])
	x = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
	with open("requirments.txt", "w") as f:
		f.write(x.decode("utf-8"))


