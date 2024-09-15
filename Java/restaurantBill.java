import java.util.Scanner;//for reading user input

public class restaurantBill
{
   public static void main(String[] args)
   {
       //declare variables
      Scanner keyboard = new Scanner(System.in);
      double mealPrice, totalTaxCost, totalTipCost, totalCost;
      
      //set the constants
      final double TAX = 0.0675;
      final double TIP = 0.20;
      
      //give the user instructions
      System.out.println("This program calculates the tax and tip cost of a meal.");
      System.out.print("Enter the price of the meal: ");
      mealPrice = keyboard.nextDouble();
      scanner.close()
      
      //calcuate the meal cost
      totalTaxCost = mealPrice * TAX;
      totalTipCost = mealPrice * TIP;
      totalCost = mealPrice + totalTaxCost + totalTipCost;
      
      //print the results
      System.out.printf("The cost of this meal is $%,.2f%n", mealPrice);
      System.out.printf("The amount of taxes on this meal is $%,.2f%n", totalTaxCost);
      System.out.printf("The the tip amount for this meal is $%,.2f%n", totalTipCost);
      System.out.printf("The total cost of this meal is $%,.2f%n", totalCost);
   }
}