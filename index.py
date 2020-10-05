# -*- coding: utf-8 -*-
# duas fazes:
#   1 - fase de eliminação
#       a - montar a matriz aumentada [A|b]
#       b - determinar o pivô: a(kk)
#       c - determinar os multiplicadores de linha m(ik) = a(ik)/a(kk)
#       d - atualizar as linhas Li <- Li - m(ik)*L(pivô)
#   2 - fase de substituição
# --------------------------------------------------------------------

# 1 - fase de eliminação
def main(matrizCoeficientes, matrizTermosIndependentes, line, column):
    # matriz dos coeficientes
    print("matriz dos coeficientes")
    printMatriz(matrizCoeficientes)

    #matriz dos termos independentes
    print("\nmatriz dos termos independentes")
    printMatriz(matrizTermosIndependentes)
    
    #a - montar a matriz aumentada [A|b]
    matrizOverall(matrizCoeficientes, matrizTermosIndependentes, line, column) #Overall = global
    print("\nmatriz aumentada")
    printMatriz(matrizCoeficientes)

    #retorna pivo da matriz apliada
    #fazer um laço aqui
    #[k1,k2] = returnPivo(matrix)
    
#gera a matriz em forma [A|b]
def matrizOverall(matrizCoeficientes, matrizTermosIndependentes, line, column):
    #precisamos saber, quantas linhas a matriz tem
    i = 0
    while (i < line):
        matrizCoeficientes[i].append("")
        matrizCoeficientes[i][column] = matrizTermosIndependentes[i][0]
        i += 1

#printa matriz
def printMatriz(matrix):
    for item in matrix:
        print(item)







main([[3,2,4],
      [1,1,2],
      [4,3,-2]], [[1],
                  [2],
                  [3]], 3, 3)




#python muda diretamente no endereço da variável