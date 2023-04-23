#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <string>

#define TAM_SENHA 30

int main(void)
{
    srand(time(0));
    std::string arq = "ASCII.txt";
    char senha[TAM_SENHA];
    std::ifstream file(arq);

    if (!file.is_open()) {
        std::cerr << "Houve um erro ao abrir o arquivo \"" << arq << "\"" << std::endl;
        return 1;
    }

    std::string opcoes, linha;

    while (std::getline(file, linha))
    {
        opcoes += linha;
    }

    for (int i = 0; i < TAM_SENHA; i++)
    {
        senha[i] = opcoes[rand() % opcoes.size()];
    }

    for (int i = 0; i < TAM_SENHA; i++)
    {
        std::cout << senha[i];
    }
    std::cout << std::endl;

    return 0;
}
