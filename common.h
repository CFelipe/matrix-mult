#include <iostream>
#include <fstream>

using namespace std;

inline void printMatrix(int m, int matrix[]) {
    int i, j;
    for(i = 0; i < m; ++i) {
        for(j = 0; j < m; ++j) {
            cout << matrix[(i * m) + j] << " | ";
        }
        cout << endl;
    }
}

inline int readMatrixFromFile(string filename, int m, int matrix[]) {
    ifstream file;
    file.open(filename);

    if(!file.is_open()) {
        cout << "Arquivo inválido" << endl;
        return 1;
    }

    int m2, m3;
    file >> m2 >> m3;
    //cout << "m2: " << m2 << endl;
    //cout << "m3: " << m3 << endl;
    int i, j;
    for(i = 0; i < m; ++i) {
        for(j = 0; j < m; ++j) {
            file >> matrix[(m * i) + j];
        }
    }

    file.close();

    return 0;
}

