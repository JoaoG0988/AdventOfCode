#include <iostream>

using namespace std;

int main()
{
    int pos = 50;
    int cont = 0;

    string entrada;
    while (cin >> entrada)
    {
        if (entrada.empty())
        {
            break;
        }

        char move = entrada[0];

        if (entrada.length() < 2)
        {
            continue;
        }

        try
        {
            int passos = stoi(entrada.substr(1));

            if (move == 'R')
            {
                cont += (pos + passos) / 100;
                pos = (pos + passos) % 100;
            }
            else if (move == 'L')
            {
                int dist_ate_zero = (100 - pos) % 100;
                cont += (dist_ate_zero + passos) / 100;
                pos = (pos - passos) % 100;
                if (pos < 0)
                {
                    pos += 100;
                }
            }
            cout << cont << endl;
        }
        catch (const invalid_argument &e)
        {
            cerr << "Formato inválido: " << entrada.substr(1) << endl;
        }
    }
    cout << endl;
    return 0;
}