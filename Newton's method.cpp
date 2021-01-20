// Newton's method.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#define e 2.7

using namespace std;

double initial_function(double x){

	return 3 * x - 14 + pow(e, x);
	//return cos(2.0 / x) - 2.0 * sin(1.0 / x) + 1.0 / x;

}

double first_derivative_function(double x){

	return 3 + pow(e, x);
	//return 2.0 * sin(2.0 / x) / pow(x, 2.0) - 1.0 / pow(x, 2.0) + 2.0 * cos(1.0 / x) / pow(x, 2.0);
}

double second_derivative_function(double x){

	return pow(e, x);
	//return 2.0 / pow(x, 3.0) - 4.0 * cos(2.0 / x) / pow(x, 4.0) - 4.0 * cos(1.0 / x) / pow(x, 3.0) + 2.0 * sin(1.0 / x) / pow(x, 4.0);
}

void dotted_line() {

	for (int i = 0; i < 80; i++)
	{
		cout << "-";
	}
	cout << endl;
}

void Newtons_method(double a, double b, double eps){

	double x, m, n, k, last_x;

	cout << endl << "Найдем производную F(x) заключенную на отрезке [" << a << ";" << b << "]" << endl << endl;
	cout << "F  (" << a << ") = " << initial_function(a) << endl;
	cout << "F' (" << a << ") = " << first_derivative_function(a) << endl;
	cout << "F''(" << a << ") = " << second_derivative_function(a) << endl << endl;
	cout << "F  (" << b << ") = " << initial_function(b) << endl;
	cout << "F' (" << b << ") = " << first_derivative_function(b) << endl;
	cout << "F''(" << b << ") = " << second_derivative_function(b) << endl << endl;

	if ((initial_function(a) * second_derivative_function(a)) > 0){
	
		x = a;
		cout << endl << "Отсюда мы видим что F(" << a << ") * F''(" << a << ") > 0 =>" << endl << "x0 = " << x << " возьмем в качестве начального приближения." << endl << endl;
	}
	else{

		if ((initial_function(b) * second_derivative_function(b)) > 0){

			x = b;
			cout << endl << "Отсюда мы видим что F(" << b << ") * F''(" << b << ") > 0 =>" << endl << "x0 = " << x << " возьмем в качестве начального приближения." << endl << endl;
		}
		else{

			cout << endl << "Условие сходимости не выполнено." << endl;
			x = -10E10;
		}
	} 
	
	m = fabs(first_derivative_function(x));
	cout << "Найдем точку m = max|F'(x)| = " << m << endl << endl << endl;
	
	last_x = x;

	dotted_line();
	cout << endl;
	if (x > -10E10) {

		k = 0;

		while (true) {

			x = x - initial_function(x) / first_derivative_function(x);
			n = fabs(initial_function(x) / m);
			k += 1;

			cout << "x" << k << " = " << last_x << " - F(" << last_x << ")/F'(" << last_x << ") = " << last_x << " - " << initial_function(last_x) << "/" << first_derivative_function(last_x) << " = " << x << endl << endl;

			last_x = x;
			if (n < eps) { break; }
		}
	}

	dotted_line();

	cout << endl << "Корень уравнения с точностью "<< eps << " равен x = " << x << endl;
	cout << "Количество итераций = " << k << endl;

}


int main()
{
	setlocale(LC_ALL, "Russian");
	double a, b, eps;
	cout << "\nВведите начальный (нижний) предел a = ";
	cin >> a;

	while (!(cin) || cin.get() != '\n') {

		cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << "\n\nНижний предел a = ";
		cin >> a;
	}

	cout << "\n\nВведите конечный (верхний) предел b = ";
	cin >> b;

	while (!(cin) || cin.get() != '\n') {

		cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << "\n\nВерхний предел b = ";
		cin >> b;
	}

	cout << "\n\nВведите желаемую точность = ";
	cin >> eps;

	while (!(cin) || cin.get() != '\n') {

		cout << "\nНеправильный ввод. Пожалуйста, попробуйте еще раз:";
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << "\n\nЖелаемая точность (eps) = ";
		cin >> eps;
	}
	
	dotted_line();
	Newtons_method(a, b, eps);
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
