#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <string>
#include <random>
#include <functional>

#define TAM_SENHA 30

int main(void)
{


    int seed = time(0) * 1000 + clock();
    auto dice = std::bind(std::uniform_int_distribution<>(1,6),std::mt19937(seed));
    int twoDiceRoll = dice() + dice();
    srand(seed);
    std::string arq = "../ASCII.txt";
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

    std::ofstream ofs;
    //ofs.open("senha.txt", std::ofstream::out | std::ofstream::trunc);
    ofs << senha;
    ofs.close();

    return 0;
}
