/* Simple Calculator with functions to perform addition, subtraction,
division and multiplication. This simple program does not handle floats
*/

#include <iostream>

using namespace std;

// User's choice for numbers to perform math functions
int firstNumber = 0;
int secondNumber = 0; 

// Functions to perform math equations
void addition() {
    cout << firstNumber + secondNumber; 
}

void subtraction() {
    cout << firstNumber - secondNumber;
}

void multiplication() {
    cout << firstNumber * secondNumber;
}

void division() {
    cout << firstNumber / secondNumber;
}


int main() {
    int userInput = 0;

    // User Interface for math choice
    cout << "* * * * * * * * * * * * * * *\n";
    cout << "* Press 1 for addition      *\n";
    cout << "* Press 2 for subtraction   *\n";
    cout << "* Press 3 for multiplication*\n";
    cout << "* Press 4 for division      *\n";
    cout << "* * * * * * * * * * * * * * *\n";

    cin >> userInput;

    if (userInput == 1) {
        cout << "Enter first number: \n";
        cin >> firstNumber;
        cout << "Enter second number: \n";
        cin >> secondNumber;
        addition();
        return 0;

    } else if (userInput == 2) {
        cout << "Enter first number: \n";
        cin >> firstNumber;
        cout << "Enter second number: \n";
        cin >> secondNumber;
        subtraction();
        return 0;

    } else if (userInput == 3) {
        cout << "Enter first number: \n";
        cin >> firstNumber;
        cout << "Enter second number: \n";
        cin >> secondNumber;
        multiplication();
        return 0;

    } else if (userInput == 4) {
        cout << "Enter first number: \n";
        cin >> firstNumber;
        cout << "Enter second number: \n";
        cin >> secondNumber;
        division();
        return 0;
    } 
    else {
        cout << "Not a valid selection, try again.\n";
    }
    return 0;
}