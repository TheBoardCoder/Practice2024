import java.util.Scanner; //for reading user input

public class speedOfSound
{
   public static void main(String[] args)
   {
      //declare and initialize variables
      Scanner keyboard = new Scanner(System.in);
      int time = 0, distance = 0;
      
      //declare constants
      final int AIR = 1100, WATER = 4900, STEEL = 16400;
      
      //give the user instructions
      System.out.println("This program calculates the approximate time it takes sound to travels through \n" 
      + "air, water, or steel once given a distance from a user.\n");
      System.out.print("Please enter air, water, or steel: ");
      String medium = keyboard.nextLine();
      System.out.print("Please enter the distance the sound wave will travel (As an integer): ");
      distance = keyboard.nextInt();
      
      //calculate the time it takes sound to travel through the medium
      if (medium.equals("air")){
      time = distance/AIR;
      } else if (medium.equals("water")){
      time = distance/WATER;
      } else if (medium.equals("steel")){
      time = distance/STEEL;
      } else{
      System.out.println(medium);
      System.out.println("Error: Medium not recognized.");
      System.exit(1);
      }
      
      //display the results
      System.out.printf("Sound takes %,d seconds to travel %,d feet through %s.", time, distance, medium);
   }
}  
