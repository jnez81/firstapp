/* This program will return 'Fizz' if divisible by 5
 *  will return 'Buzz' if divisible by 3
 *  will return 'FizzBuzz' if divisible by both 3 and 5
 *  will return value if not divisble by 3 nor 5
*/

#include <iostream>

using namespace std; 

int main() {
    // User input for number
    int number = 0;
    cout << "Enter number: \n";
    cin >> number; 

    if ((number % 3 == 0) && (number % 5 == 0)) {
        cout << "FizzBuzz";

    } else if (number % 3 == 0) {
        cout << "Buzz";

    } else if (number % 5 == 0) {
        cout << "Fizz";

    } else {
        cout << number; 
    }
}