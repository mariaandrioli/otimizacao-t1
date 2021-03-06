#!/usr/bin/env python3

FILENAME = "output.lp"

def read_input():
	num_sedes, num_conexoes = input().split()
	num_sedes = int(num_sedes)
	num_conexoes = int(num_conexoes)

	sede_origem, sede_destino, demanda = input().split()
	sede_origem = int(sede_origem)
	sede_destino = int(sede_destino)
	demanda = int(demanda)

	custos = []
	for conexao in range(num_conexoes):
		aux = input().split()
		custos.append(int(aux[0]))
		custos.append(int(aux[1]))
		custos.append(float(aux[2]))

	return num_sedes, num_conexoes, sede_origem, sede_destino, demanda, custos

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def criaDictCustos(custos, demanda):
	custos_conexoes = {}

	j = 0
	for i in range(0,len(custos),3):
		custos_conexoes[(custos[i], custos[i+1])] = custos[i+2]*demanda
		custos_conexoes[(custos[i+1], custos[i])] = custos[i+2]*demanda
		j = j + 1
		
	return custos_conexoes

def origemDestino(sede, custos_conexoes, first_position, second_position):
	in_aux = []
	out_aux = []
	for i in custos_conexoes:
		if i[first_position] == sede: # incoming
			in_aux.append(str(i[0]) + str(i[1]))
		if i[second_position] == sede: # outgoing
			out_aux.append(str(i[0]) + str(i[1]))

	f = open(FILENAME, "a")
	
	if (len(in_aux) > 0):
		for i in range(len(in_aux)-1):
				f.write('x' + str(in_aux[i]) + " + ")
		f.write('x' + str(in_aux[len(in_aux)-1]) + " + ")

	if (len(out_aux) > 0):
		for i in range(len(out_aux)-1):
				f.write('-x' + str(out_aux[i]) + " + ")
		f.write('-x' + str(out_aux[len(out_aux)-1]) + " = 1;\n")

	f.close()

def equacaoMeio(sede, custos_conexoes):
	in_aux = []
	out_aux = []
	for i in custos_conexoes:
		if i[0] == sede: # incoming
			in_aux.append(str(i[0]) + str(i[1]))
		if i[1] == sede: # outgoing
			out_aux.append(str(i[0]) + str(i[1]))

	# print(sede)
	# print(in_aux)
	# print(out_aux)

	f = open(FILENAME, "a")
	if (len(in_aux) > 0):
		for i in range(len(in_aux)-1):
				f.write('x' + str(in_aux[i]) + " + ")
		f.write('x' + str(in_aux[len(in_aux)-1]) + " + ")

	if (len(out_aux) > 0):
		for i in range(len(out_aux)-1):
				f.write('-x' + str(out_aux[i]) + " + ")
		f.write('-x' + str(out_aux[len(out_aux)-1]) + " = 0;\n")

	f.close()

def criaSaida(sedes, custos_conexoes, num_conexoes, sede_origem, sede_destino):
	f = open(FILENAME, "w")
	# print("custos entre vertices: ", custos_conexoes)

	vars = []
	for i in custos_conexoes:
		vars.append(str(custos_conexoes[i]) + ' x' + str(i[0]) + str(i[1]))

	f.write("min: ")
	for i in range(num_conexoes-1):
			f.write(str(vars[i]) + " + ")
	f.write(str(vars[num_conexoes-1]) + ";\n")
	f.close()

	origemDestino(sede_origem, custos_conexoes, 0, 1)
	origemDestino(sede_destino, custos_conexoes, 1, 0)


	for i in sedes:
		if i != sede_origem and i != sede_destino:
			equacaoMeio(i, custos_conexoes)


	# f = open(FILENAME, "r")
	# print(f.read())

	return 0

def vertices(num_sedes):
	aux = []
	for i in range(1, num_sedes+1, 1):
		aux.append(i)

	return aux

def main():
	num_sedes, num_conexoes, sede_origem, sede_destino, demanda, custos = read_input()
	# print("origem: ", sede_origem,"\ndestino: ", sede_destino, "\ndemanda: ", demanda)

	num_conexoes = num_conexoes * 2

	sedes = vertices(num_sedes)
	custos_conexoes = criaDictCustos(custos, demanda)
	criaSaida(sedes, custos_conexoes, num_conexoes, sede_origem, sede_destino)

	return 0

if __name__ == "__main__":
	main()