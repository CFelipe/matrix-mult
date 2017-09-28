// Matrix multiplication (concurrent)

#include <iostream>
#include <string>
#include "common.h"

using namespace std;

void multThread(int rangeA, int rangeB, int m, int matrixA[], int matrixB[], int matrixC[]) {
}

void multiply(int m, int matrixA[], int matrixB[], int matrixC[]) {
    int i, j, k, sum;
    for(i = 0; i < m; ++i) {
        for(j = 0; j < m; ++j) {
            sum = 0;
            for(k = 0; k < m; ++k) {
                sum += matrixA[(i * m) + k] * matrixB[(k * m) + j];
            }
            matrixC[(i * m) + j] = sum;
        }
    }
}

int main(int argc, char *argv[]) {
    if(argc != 3) {
        cout << "Número de argumentos inválido" << endl;
        cout << "Formato: " << endl;
        cout << argv[0] << " x x" << endl;
        return 0;
    }

    int m = atoi(argv[1]);          // Substituir por strtol pra detectar erros
    int threadQty = atoi(argv[2]);  // Idem
    string filenamePrefix = "matrizes/";
    string filenameSuffix = to_string(m) + "x" + to_string(m) + ".txt";
    string filenameA = filenamePrefix + "A" + filenameSuffix;
    string filenameB = filenamePrefix + "B" + filenameSuffix;
    cout << filenameA << endl;
    cout << filenameB << endl;

    int* matrixA = new int[m * m];
    int* matrixB = new int[m * m];
    readMatrixFromFile(filenameA, m, matrixA);
    readMatrixFromFile(filenameB, m, matrixB);

    int* matrixC = new int[m * m];

    int threadElements = m / threadQty;
    int remainder = m % threadQty;
    int rangeA, rangeB;

    int i;
    for(i = 0; i < threadQty; ++i) {
        cout << "Thread " << (i + 1) << ": ";
        rangeA = i * threadElements;
        rangeB = ((i + 1) * threadElements) - 1;
        if(i == threadQty - 1) { rangeB += remainder; }
        cout << rangeA << " | " << rangeB;
        cout << endl;
    }
    //multiplyConcurrent(m, matrixA, matrixB, matrixC);
    //printMatrix(m, matrixC);

    return 0;
}
