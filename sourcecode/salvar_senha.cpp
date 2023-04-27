#include <fstream>
#include <iostream>

using namespace std;

int main() {
    // Abrir o arquivo
    ofstream arquivo("senhas_salvas/senha.txt", ios::out | ios::app);
    
    // Verificar se o arquivo foi aberto corretamente
    if (arquivo.is_open()) {
        // Escrever a senha no arquivo
        arquivo << "Senha: " << senha_gerada << endl;

        // Fechar o arquivo
        arquivo.close();

        // Exibir mensagem de sucesso
        cout << "Senha salva com sucesso!" << endl;
    } else {
        // Exibir mensagem de erro caso não seja possível abrir o arquivo
        cout << "Erro ao abrir o arquivo!" << endl;
    }

    return 0;
}
