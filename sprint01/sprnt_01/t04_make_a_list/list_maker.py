def list_maker(line, delim):
	if(delim == '') :
		return line.split(" ")
	else :
		return line.split(delim)

