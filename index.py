# -*- coding: utf-8 -*-
# duas fazes:
#   1 - fase de eliminação
#       a - montar a matriz aumentada [A|b]

#   2 - fase de substituição
# --------------------------------------------------------------------

# 1 - fase de eliminação
def main(matrizCoeficientes, matrizTermosIndependentes, line, column):
    
    #a - montar a matriz aumentada [A|b]
    matrizOverall(matrizCoeficientes, matrizTermosIndependentes, line, column) #Overall = global

    staggeringGaussian(matrizCoeficientes, line)

    
    
#gera a matriz em forma [A|b]
def matrizOverall(matrizCoeficientes, matrizTermosIndependentes, line, column):
    #precisamos saber, quantas linhas a matriz tem
    i = 0
    while (i < line):
        matrizCoeficientes[i].append("")
        matrizCoeficientes[i][column] = matrizTermosIndependentes[i][0]
        i += 1

#staggering for method Gaussiano
def staggeringGaussian(matrix, line):
    [pivot, k, linePivot, column, multiplicator] = [0,0,0,0,0]
    while (k < (line )):
        #b - determinar o pivô: a(kk)
        pivot = matrix[k][k]
        if(pivot == 0):
            print("pivot connot be zero")
            return
        #print("pivot ", pivot)
        printMatriz(matrix)
        linePivot = k + 1  #
        while (linePivot < (line)): #
            column = 0

            #determina o multiplicador
            multiplicator = matrix[linePivot][k]/float(pivot)

            while(column <= line):
                #update value 
                matrix[linePivot][column] = (round(matrix[linePivot][column],2) - round((multiplicator * matrix[k][column]),2))
                
                column += 1

            linePivot += 1
  
        k += 1



#       c - determinar os multiplicadores de linha m(ik) = a(ik)/a(kk)
#       d - atualizar as linhas Li <- Li - m(ik)*L(pivô)    








#printa matriz
def printMatriz(matrix):
    print("\n")
    for item in matrix:
        print(item)









main([[3,2,4],
      [1,1,2],
      [4,3,-2]], [[1],
                  [2],
                  [3]], 3, 3)




#python muda diretamente no endereço da variável