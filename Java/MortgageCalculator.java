package Java;

import java.text.NumberFormat;
import java.util.Scanner;

public class MortgageCalculator {

    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        // User input scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        double annualInterestRate = scanner.nextDouble();
        double monthlyInterestRate = annualInterestRate / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period (Years): ");
        int loanPeriod = scanner.nextInt();
        int numberOfPayments = loanPeriod * MONTHS_IN_YEAR;

        double mortgage = principal 
                    * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments))
                    / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: " + mortgageFormatted);

    }
    
}
