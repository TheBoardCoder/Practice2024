import java.util.Scanner;//for reading user input

public class Gasoline
{
   public static void main(String[] args)
   {
      //declare variables here
      Scanner keyboard = new Scanner(System.in);
      int gasolineBrand, octane;
      double gasInLiters, gasInGallons, totalCost = 0, basePrice = 0;
   
      //conversion factor from liters to gallons
      final double GALLONS_PER_LITER = .264172; 
      
      //prices based on brand
      final double DISCOUNT_BASE_PRICE = 2.49;
      final double PREMIUM_BASE_PRICE = 2.99;
      
      //menu options
      final int DISCOUNT = 1;

   
      //display a menu for gas type and read the user's choice
      System.out.println("CPCC Gasoline Services");
      System.out.println("\t1. Discount");
      System.out.println("\t2. Premium");
      System.out.print("Enter the brand type: ");
      gasolineBrand = keyboard.nextInt();
   
      //get the octane rating
      System.out.print("Enter the octane rating: ");
      octane = keyboard.nextInt();
   	
      //get the amount of gas in liters
      System.out.print("Enter the amount of gasoline in liters: ");
      gasInLiters = keyboard.nextDouble();
   
      //convert liters to gallons
      gasInGallons = gasInLiters * GALLONS_PER_LITER; 
      
      //figure out cost of gas based on brand and octane amount
      if(gasolineBrand == DISCOUNT)
      {
         basePrice = DISCOUNT_BASE_PRICE;
      }
      else//we know it's premium
      {
         basePrice = PREMIUM_BASE_PRICE;      
      }
      
      //calculate the total cost
      totalCost = (basePrice - ( 100 - octane) * 0.01) * gasInGallons;
      //print out the total cost, making sure to format it as currency
      System.out.printf("\nThe cost of the gasoline is $%.2f",totalCost);
   
   }
}