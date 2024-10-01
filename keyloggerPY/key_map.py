key_map = {
	'Key.space': ' ',
	'Key.shift': '',
	'Key.shift_r': '',
	'Key.enter': '\n',
	'Key.backspace': ' [BACKSPACE] ',
	'Key.ctrl_l': '',
	'Key.ctrl_r': '',
	'Key.alt_l': '',
	'Key.alt_r': '',
	'Key.caps_lock': ''
	'Key.tab': ' [TAB] ',
	'Key.cmd': '',
	'Key.esc': ' [ESC] ',
	'Key.delete': ' [DEL] ',
	'Key.up': ' [UP] ',
	'Key.down': ' [DOWN] ',
	'Key.left': ' [LEFT] ',
	'Key.right': ' [RIGHT] ',
}

def get_mapped_key(key):
	letter = str(key).replace("'", "")
	return key_map.get(letter, letter)
