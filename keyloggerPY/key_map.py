key_map = {
	'Key.space': ' ',
	'Key.shift_r': '',
	'Key.shift': '',
	'Key.enter': '\n',
	'Key.backspace': ' [BACKSPACE] ',
	'Key.ctrl_l': '',
	'Key.ctrl_r': '',
	'Key.alt_l': '',
	'Key.alt_r': '',
	'Key.caps_lock': ''
}

def get_mapped_key(key):
	letter = str(key).replace("'", "")
	return key_map.get(letter, letter)
