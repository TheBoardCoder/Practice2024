//import scanner
import java.util.Scanner;

public class GasolineCostCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("CPCC Gasoline Services");
        System.out.println("1. Discount");
        System.out.println("2. Premium");

        // Prompt for the brand of gasoline
        System.out.print("Enter the brand of gasoline (1 for Discount, 2 for Premium): ");
        int brandChoice = scanner.nextInt();

        // Prompt for the octane rating
        System.out.print("Enter the octane rating (between 87 and 100): ");
        int octaneRating = scanner.nextInt();

        // Prompt for the amount of gasoline in liters
        System.out.print("Enter the amount of gasoline in liters: ");
        double liters = scanner.nextDouble();

        // Convert liters to gallons
        double gallons = liters * 0.264172;

        // Calculate the cost based on the brand and octane rating
        double costPerGallon;
        if (brandChoice == 1) {
            costPerGallon = 2.49 - (100 - octaneRating) * 0.01;
        } else if (brandChoice == 2) {
            costPerGallon = 2.99 - (100 - octaneRating) * 0.01;
        } else {
            System.out.println("Invalid brand choice.");
            scanner.close();
            return;
        }

        // Calculate the total cost
        double totalCost = costPerGallon * gallons;

        // Display the cost of the gasoline purchase
        System.out.printf("The cost of the gasoline purchase is: $%.2f%n", totalCost);
        
        // Close the scanner
        scanner.close();
    }
}
