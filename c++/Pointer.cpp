#include "stdafx.h"
#include "Pointer.h"

using namespace std;

// swap func ----------------------------------------------------------
void swap_val(int a, int b)
{
	int t = a;
	a = b;
	b = t;
}

void swap_ref(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

// Login ----------------------------------------------------------
class Login {
private:
	char site[40];
	char id[20];
	char password[20];
public:
	void print();
	void cin_site();
	void cin_id();
	void cin_password();
};

void Login::print()
{
	cout << site << "/" << id << "/" << password << endl;
}

void printMsgAndGetAnswer(char msg[100], char* ptr)
{
	cout << msg << endl;
	cin >> ptr;
}

void Login::cin_site()
{
	printMsgAndGetAnswer("please enter the site:", site);
}

void Login::cin_id()
{
	printMsgAndGetAnswer("please enter the id:", id);
}

void Login::cin_password()
{
	printMsgAndGetAnswer("please enter the password:", password);
}

// Starcraft ----------------------------------------------------------
class Starcraft
{
	char unit[100];
	int hp;
	int damage;
public:
	Starcraft(char[], int, int);
	void show();
};

Starcraft::Starcraft(char a[100], int b, int c)
{
	strcpy_s(unit, a);
	hp = b;
	damage = c;
}

void Starcraft::show()
{
	cout << unit << "/" << hp << "/" << damage << endl;
}

// Same ----------------------------------------------------------
class Same
{
private:
	int num1;
	int num2;
public:
	void show();
	Same(int, int);
	void equal1(int, int);
	void equal2(int, int);
};

Same::Same(int a, int b)
{
	num1 = a;
	num2 = b;
}

void Same::show()
{
	cout << num1 << "/" << num2 << endl;
}

void Same::equal1(int num1, int num2)
{
	this->num1 = num1;
	this->num2 = num2;
}

void Same::equal2(int num1, int num2)
{
	num1 = num1;
	num2 = num2;
}

// Stack ----------------------------------------------------------
class Stack
{
private:
	int cookie;
	int nacho;
	int kancho;
	int chip;
	static int number;
public:
	Stack(int, int, int, int);
	static void sum(int, int, int, int);
	static void sum_show();
};

int Stack::number = 0;

Stack::Stack(int a, int b, int c, int d)
{
	cookie = a;
	nacho = b;
	kancho = c;
	chip = d;
}

void Stack::sum(int a, int b, int c, int d)
{
	number += (a + b + c + d);
}

void Stack::sum_show()
{
	cout << number << endl;
}

// Mate ----------------------------------------------------------
class Mate
{
private:
	string name;
	int age;
	string relation;
public:
	Mate(string, int, string);
	void show();
};

Mate::Mate(string a, int b, string c)
{
	name = a;
	age = b;
	relation = c;
}

void Mate::show()
{
	cout << name << "/" << age << "/" << relation << endl;
}

// Grade / student ----------------------------------------------------------
class Grade;
class Student
{
private:
	string name;
	string major;
	int studentNumber;
public:
	Student(string, string, int);
	friend void printGrade(Student, Grade);
};

class Grade
{
private:
	double gradeAverage;
public:
	Grade(double);
	friend void printGrade(Student, Grade);
};

Student::Student(string a, string b, int c) :name(a), major(b), studentNumber(c) {}
Grade::Grade(double a) : gradeAverage(a) {}

void printGrade(Student a, Grade b)
{
	cout << a.name << endl;
	cout << a.major << endl;
	cout << a.studentNumber << endl;
	cout << b.gradeAverage << endl;
}

Pointer::Pointer()
{
	// pointer?
	/*int data = 19;
	int* pointer = &data;

	cout << data << "/" << &data << endl;
	cout << *pointer << "/" << pointer << "/" << &pointer << endl;*/

	// pointer operation
	/*char char_num = 1;
	int int_num = 1;
	double double_num = 1;

	char* char_ptr = &char_num;
	int* int_ptr = &int_num;
	double* double_ptr = &double_num;

	cout << char_ptr << "/" << int_ptr << "/" << double_ptr << endl;
	cout << char_ptr + 1 << "/" << int_ptr + 1 << "/" << double_ptr + 1 << endl;

	int num[4] = { 0, 11, 22, 33 };
	int* num_ptr = num;
	cout << num_ptr << "/" << *num_ptr << endl;

	num_ptr++;
	cout << num_ptr << "/" << *num_ptr << endl;

	(*num_ptr)++;
	cout << num_ptr << "/" << *num_ptr << endl;

	++num_ptr;
	cout << num_ptr << "/" << *num_ptr << endl;

	++(*num_ptr);
	cout << num_ptr << "/" << *num_ptr << endl;*/

	// array & pointer
	/*char char_buf[5] = { 1, 2, 3, 4, 5 };
	int int_buf[5] = { 6, 7, 8, 9, 10 };

	char* ptr1 = char_buf;
	int* ptr2 = &int_buf[0];

	cout << char_buf << "/" << *char_buf << endl;
	ptr1++;
	cout << ptr1 << "/" << *ptr1 << endl;

	cout << &int_buf[0] << "/" << *int_buf << endl;
	ptr2 += 2;
	cout << ptr2 << "/" << *ptr2 << endl;*/

	// call by value & call by reference
	/*int a = 100;
	int b = 200;

	swap_val(a, b);
	cout << a << "/" << b << endl;

	swap_ref(&a, &b);
	cout << a << "/" << b << endl;*/

	// class / public / private
	/*Login test;
	test.cin_site();
	test.cin_id();
	test.cin_password();
	test.print();*/

	// object pointer
	/*Starcraft marine("Marine", 40, 6);
	Starcraft zergling("Zergling", 35, 5);
	Starcraft hydralisk("Hydralisk", 80, 10);

	marine.show();

	Starcraft* ptr = &zergling;
	ptr->show();
	ptr = &hydralisk;
	(*ptr).show();*/

	// this pointer
	/*Same s1(1, 2);
	Same s2(3, 4);

	s1.equal1(10,20);
	s1.show();

	s2.equal2(30, 40);
	s2.show();*/

	// static memeber variable
	/*Stack inventory1(10, 20, 30, 40);
	Stack::sum(10, 20, 30, 40);
	Stack::sum_show();

	Stack inventory2(50, 60, 70, 80);
	Stack::sum(50, 60, 70, 80);
	Stack::sum_show();*/

	// object array
	/*Mate aGroup[3] = {
		Mate("name1", 21, "friend"),
		Mate("name2", 50, "mom"),
		Mate("name3", 20, "sister")
		};
		for (int i = 0; i < 3; i++)
		aGroup[i].show();*/

	// friend
	/*Student s("name", "major", 1234);
	Grade g(4.5);
	printGrade(s, g);*/

	// dynamic allocation new/delete
	/*int* p = new int;
	if (p == 0)
		cout << "fail to allocate the memory" << endl;
	else
	{
		*p = 17;
		cout << *p << endl;
		delete p;
	}*/

	// array/object/object array dynamic allocation
	/*int num;
	cout << "enter one positive integer!" << endl;
	cin >> num;

	int* arr = new int[num];
	for (int i = 0; i < num; i++)
		arr[i] = i;

	cout << "size of arr? " << sizeof arr / sizeof(int) << endl;
	for (int i = 0; i < num; i++)
		cout << arr[i] << endl;*/
}

Pointer::~Pointer()
{
}
