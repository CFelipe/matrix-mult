// Multiplicação de matrizes (concorrente)

#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <vector>
#include "common.h"

using namespace std;
using namespace std::chrono;

void multThread(int rangeA, int rangeB, int m, int matrixA[], int matrixB[], int matrixC[]) {
    int matI, matJ, element, sum, k;

    for(element = rangeA; element <= rangeB; ++element) {
        sum = 0;
        matI = element / m;
        matJ = element % m;
        for(k = 0; k < m; ++k) {
            sum += matrixA[(matI * m) + k] * matrixB[(k * m) + matJ];
        }
        matrixC[(matI * m) + matJ] = sum;
    }
}

void multiplyConcurrent(int threadQty, int m, int matrixA[], int matrixB[], int matrixC[]) {
    int threadElements = (m * m) / threadQty;
    int remainder = (m * m) % threadQty;
    int rangeA, rangeB;
    vector<thread> threads;
    threads.reserve(threadQty);

    int i;
    for(i = 0; i < threadQty; ++i) {
        rangeA = i * threadElements;
        rangeB = ((i + 1) * threadElements) - 1;
        if(i == threadQty - 1) { rangeB += remainder; }
        threads.emplace_back(multThread, rangeA, rangeB, m, matrixA, matrixB, matrixC);
    }

    for(auto& t : threads) {
        t.join();
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

    string resultPrefix = "resultados/";
    string filenameC = resultPrefix + "C" + filenameSuffix;
    //cout << filenameA << endl;
    //cout << filenameB << endl;

    int* matrixA = new int[m * m];
    int* matrixB = new int[m * m];
    readMatrixFromFile(filenameA, m, matrixA);
    readMatrixFromFile(filenameB, m, matrixB);

    int* matrixC = new int[m * m];

    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    multiplyConcurrent(threadQty, m, matrixA, matrixB, matrixC);
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    auto durationNs = duration_cast<nanoseconds>(t2 - t1).count();
    cout << durationNs / 1e6 << "ms" << endl;

    saveMatrixToFile(filenameC, m, matrixC);

    return 0;
}
