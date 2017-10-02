#include <iostream>
#include <fstream>

using namespace std;

inline void saveMatrixToFile(string filename, int m, int matrix[]) {
    ofstream file;
    file.open(filename);

    int i, j;
    for(i = 0; i < m; ++i) {
        for(j = 0; j < m; ++j) {
            file << matrix[(i * m) + j] << " | ";
        }
        file << endl;
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

    int i, j;
    for(i = 0; i < m; ++i) {
        for(j = 0; j < m; ++j) {
            file >> matrix[(m * i) + j];
        }
    }

    file.close();

    return 0;
}

