with open('file.txr', 'r') as problem:
	nucleotides = ''
	ident = ''
	gc = 0
	while True:
		line = problem.readline()
		if line and line[0] == '>':
			if len(nucleotides) > 0:
				gc = nucleotides.count('G') + nucleotides.count('C')
				porcentaje = (gc * 100) / len(nucleotides)
				print(ident)
				print(porcentaje)
			ident_finded = True
			nucleotides = ''
		else:
			ident_finded = False
		if ident_finded:
			ident = line[1:-1]
		else:
			if line:
				nucleotides += line.rstrip("\n")
		if not line:
			if len(nucleotides) > 0:
				gc = nucleotides.count('G') + nucleotides.count('C')
				porcentaje = (gc * 100) / len(nucleotides)
				print(ident)
				print(porcentaje)
			break