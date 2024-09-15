import java.util.Scanner; //for reading user input

public class GuitarLessonMembership
{
   public static void main(String[] args)
   {
      //declare and initialize variables
      Scanner keyboard = new Scanner(System.in);
      double discountedAmt = 0, finalAmt = 0, subtotal = 0, mins = 0, hours = 0, hourlyRate = 0;
      
      //declare the constants
      final double WEIGHTLIFTING_RATE = 59.99;
      final double CARDIO_RATE = 49.99;
      final double DISCOUNT_RATE = 0.15;
      
      //give the user instructions
      System.out.println("This program calculates the bill for a personal training session at the gym.\n");
      System.out.println("Choose from one of the following types of training sessions:");
      System.out.println("\tW - Weightlifting Session");
      System.out.println("\tC - Cardio Session");
      System.out.print("Enter your choice (W or C):");
      String sessionType = keyboard.nextLine();
      if (sessionType.equals("w") || sessionType.equals("W")){
         hourlyRate = WEIGHTLIFTING_RATE;
         System.out.println("\nWeightlifting rate: " + WEIGHTLIFTING_RATE + " per hour");
      }
      else if (sessionType.equals("c") || sessionType.equals("C")){
         hourlyRate = CARDIO_RATE;
         System.out.println("\nCardio session rate: " + CARDIO_RATE + " per hour");
      }
      else {
         System.out.println("\nInvalid entry. Cardio training session booked.");
         hourlyRate = CARDIO_RATE;
         sessionType = "cardio";
      }
      System.out.print("\nPlease enter the duration of the training session in minutes (min: 40 - max: 120): ");
      mins = keyboard.nextDouble();
      keyboard.nextLine();
      if (mins > 120 || mins < 40) {
         System.out.println("\nInvalid entry. 45 minute training session booked.\n");
         mins = 45;
      }
      System.out.print("If you have a discount code please enter it here. If not hit enter: ");
      String discountCode = keyboard.nextLine();
      
      
      //perform the calculations
      hours = mins / 40;
      subtotal = hourlyRate * hours;
      if (discountCode.equals("FITNESS15OFF")){
         discountedAmt = (subtotal * DISCOUNT_RATE);
         System.out.println("\n15% Discount Applied");
         }
      else{
         System.out.println("\nInvalid code. No discount applied.");
      }
      finalAmt = subtotal - discountedAmt;
      
      //display the results
      System.out.printf("\nThe training session %s was booked for %.2f hours.", sessionType, hours);
      System.out.printf("The hourly rate for the session was $%.2f per hour, \nthe subtotal was $%.2f," 
      + " the amount discounted was $%.2f, and the final amount for the session was $%.2f."
      ,hourlyRate, subtotal, discountedAmt, finalAmt);
      }
}  