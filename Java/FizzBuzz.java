package Java;

import java.util.Scanner;

public class FizzBuzz {

    public static void main(String[] args) {
        /** Program will return 'Fizz' if divisible by 5
         *  will return 'Buzz' if divisible by 3
         *  will return 'FizzBuzz' if divisible by both 3 and 5
         *  will return value if not divisble by 3 nor 5
         *  */ 

        Scanner scanner = new Scanner(System.in);
        System.out.print("Number: ");
        int number = scanner.nextInt();

        if (number % 5 == 0 && number % 3 == 0)
            System.out.println("FizzBuzz");
        else if (number % 5 == 0)
            System.out.println("Fizz");
        else if (number % 3 == 0)
            System.out.println("Buzz");        
        else 
            System.out.println(number);

    }
    
}
