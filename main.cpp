#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <string>

#define TAM_SENHA 30

int main(void)
{
    srand(time(0));
    std:: string arq = "ASCII.txt", senha[30];
    std:: ifstream file(arq);

    if(!(file.is_open())) {
        std:: cerr << "Houve um erro ao abrir o arquivo \""<< arq << "\"" << std:: endl;
        return 1;
     }

    std::string opcoes, linha;

    while(std::getline(file, linha))
    {
        opcoes += linha;
    }

    for(int i = 0; i < TAM_SENHA; i++)
    {
        senha[i] += (opcoes[rand() % opcoes.size()]);
    }

    std::cout << senha << std::endl;

    return 0;
}
