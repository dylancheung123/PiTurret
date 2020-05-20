import reader
import turret
import threading, random

def main():
	thread = threading.Thread(target=reader.run)
	thread.start()
	turret.run()
	print("End of main function")

if __name__ == "__main__":
	main()
	print("End of run.py")