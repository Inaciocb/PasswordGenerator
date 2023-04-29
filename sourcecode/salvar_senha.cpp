#include <fstream>
#include <iostream>

using namespace std;

int main() {
    
    ofstream arquivo("senhas_salvas/senha.txt", ios::out | ios::app);
    
    if (arquivo.is_open()) {
        arquivo << "Senha: " << senha_gerada << endl;
        arquivo.close();
        cout << "Senha salva com sucesso!" << endl;
    } else {
        cout << "Erro ao abrir o arquivo!" << endl;
    }

    return 0;
}
