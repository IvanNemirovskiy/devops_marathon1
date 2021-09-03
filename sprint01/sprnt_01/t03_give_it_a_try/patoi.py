def patoi(data):
	try:
		cast = int(data)
		return cast		
	except ValueError:
		return False
