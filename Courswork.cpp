// Courswork.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>
#include <iomanip> 

using namespace std;


double function(double x) 
{
    //return sqrt(1 + 2 * pow(x, 2) - pow(x, 3));
    return 1 / sqrt(3 + pow(x, 5));
    //return sqrt(pow(x, 2) + 3);
}


double simpsons(double function(double x), double a, double b, int n)
{
    double h, integral, x, sum = 0;
    int i;

    h = fabs(b - a) / n;

    for (i = 1; i < n; i++){

        x = a + i * h;

        if (i % 2 == 0) {
            sum = sum + 2 * function(x);
        }
        else {
            sum = sum + 4 * function(x);
        }
    }

    integral = (h / 3) * (function(a) + function(b) + sum);

    return integral;
}



int main()
{
    double a, b, h, sum = 0, integral, x, eps, new_integral;
    int n, i = 2;

    setlocale(LC_ALL, "Russian");
    cout << "\nВведите начальный (нижний) предел a = ";
    cin >> a;

    while (!(cin) || cin.get() != '\n'){

        cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "\n\nНижний предел a = ";
        cin >> a;
    }

    cout << "\n\nВведите конечный (верхний) предел b = ";
    cin >> b;

    while (!(cin) || cin.get() != '\n'){

        cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "\n\nВерхний предел b = ";
        cin >> b;
    }

    cout << "\n\nВведите желаемую точность = ";
    cin >> eps;

    while (!(cin) || cin.get() != '\n'){

        cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "\n\nЖелаемая точность (eps) = ";
        cin >> eps;
    }

    new_integral = simpsons(function, a, b, i);

    do {

        integral = new_integral;
        i += 2;
        new_integral = simpsons(function, a, b, i);

    } while (fabs(new_integral - integral) >= eps);
    
    cout << "\n\nИнтеграл равен " << fixed << setprecision(4) << new_integral << " для " << i << " подинтервалов.\n";
    cin.get();
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
