// Multiplicação de matrizes (sequencial)

#include <iostream>
#include <string>
#include <chrono>
#include "common.h"

using namespace std;
using namespace std::chrono;

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
    if(argc != 2) {
        cout << "Número de argumentos inválido" << endl;
        cout << "Formato: " << endl;
        cout << argv[0] << " x" << endl;
        return 0;
    }

    int m = atoi(argv[1]);
    string filenamePrefix = "matrizes/";
    string filenameSuffix = to_string(m) + "x" + to_string(m) + ".txt";
    string filenameA = filenamePrefix + "A" + filenameSuffix;
    string filenameB = filenamePrefix + "B" + filenameSuffix;

    string resultPrefix = "resultados/";
    string filenameC = resultPrefix + "C" + filenameSuffix;

    int* matrixA = new int[m * m];
    int* matrixB = new int[m * m];
    readMatrixFromFile(filenameA, m, matrixA);
    readMatrixFromFile(filenameB, m, matrixB);

    int* matrixC = new int[m * m];
    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    multiply(m, matrixA, matrixB, matrixC);
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    auto durationNs = duration_cast<nanoseconds>(t2 - t1).count();
    cout << durationNs / 1e6 << "ms" << endl;

    saveMatrixToFile(filenameC, m, matrixC);

    return 0;
}
