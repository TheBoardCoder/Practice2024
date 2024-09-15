//import scanner
import java.util.Scanner;

//declare class
public class GuitarLessonMembership2 {

   //declare main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String membershipType = getMembershipType();
        double baseCost = getBaseCost(membershipType);
        double freeLessons = getNumFreeLessons(membershipType);
        double hourlyRate = getHourlyRate(membershipType);

        displayInfo(membershipType, freeLessons, hourlyRate, baseCost);

        int totalLessonsBooked = 0;
        double totalHours = 0;
        double totalLessonCharges = 0;
        
        System.out.print("Enter y or yes to book a guitar lesson. Enter n or no to stop and process your invoice: ");
        String response = scanner.nextLine().trim();
        
        while (!response.equalsIgnoreCase("y") && !response.equalsIgnoreCase("yes")) {
            if (response.equalsIgnoreCase("n") || response.equalsIgnoreCase("no")) {
                break;
            } else if (response.equalsIgnoreCase("y") || response.equalsIgnoreCase("yes")) {

                double numHours = getNumHours(membershipType, freeLessons, hourlyRate);
                double lessonCost = getPriceLesson(freeLessons, hourlyRate, numHours);

                totalLessonsBooked++;
                totalHours += numHours;
                totalLessonCharges += lessonCost;

                if (freeLessons > 0) {
                    freeLessons--;
                }

            displayInvoice(baseCost, totalLessonsBooked, totalHours, totalLessonCharges);

            scanner.close();
            } else {
            System.out.println("\nERROR: Invalid response. Try again.\n");
            System.out.print("\nEnter y or yes to book a guitar lesson. Enter n or no to stop and process your invoice: ");
            response = scanner.nextLine().trim();
            }
    }
    }
    
    // declare get membershiptype
    public static String getMembershipType() {
        Scanner scanner = new Scanner(System.in);
        String membershipType;
        System.out.println("Book your Guitar Lesson Today!\n");
        System.out.print("Enter your type of Membership: 'Silver' or 'Gold': ");
        membershipType = scanner.nextLine().trim();
        while (!membershipType.equalsIgnoreCase("Silver") && !membershipType.equalsIgnoreCase("Gold")) {
            if (!membershipType.equalsIgnoreCase("Silver") && !membershipType.equalsIgnoreCase("Gold")) {
                System.out.println("\nERROR: Invalid membership entered. Try again.");
                System.out.print("\nEnter your type of Membership: 'Silver' or 'Gold': ");
                membershipType = scanner.nextLine().trim();
            }
        }
        return membershipType;
    }
    // declare get base cost method
    public static double getBaseCost(String membershipType) {
        if (membershipType.equalsIgnoreCase("Silver")) {
            return 56.45;
        } else if (membershipType.equalsIgnoreCase("Gold")) {
            return 75.85;
        }
        return 0;
    }
    
    // declare get number of free lessons method
    public static double getNumFreeLessons(String membershipType) {
        if (membershipType.equalsIgnoreCase("Silver")) {
            return 1.0;
        } else if (membershipType.equalsIgnoreCase("Gold")) {
            return 3.0;
        }
        return 0;
    }
    
    // declare get hourly rate method
    public static double getHourlyRate(String membershipType) {
        if (membershipType.equalsIgnoreCase("Silver")) {
            return 18.95;
        } else if (membershipType.equalsIgnoreCase("Gold")) {
            return 16.75;
        }
        return 0;
    }

    // declare get number of hours method
    public static double getNumHours(String membershipType, double freeLessons, double hourlyRate) {
        Scanner scanner = new Scanner(System.in);
        double numHours;
        String lessonsLeft = String.format("%.2f", freeLessons);
        System.out.println("\nNote: You have " + lessonsLeft + " remaining free guitar lesson with your Silver membership");
        System.out.println("You will be charged at a rate of " + hourlyRate + " per hour for guitar lessons if you exceed the free lessons.");
        System.out.print("How many hours are you looking to book for this guitar lesson? (min 1 hour - max 3.5 hour): ");
        numHours = scanner.nextDouble();
            
        while (numHours < 1 && numHours > 3.5) {
            if (numHours < 1 && numHours > 3.5) {
                System.out.println("\nError you must input between 1 and 3.5 hours. Try again.");
                System.out.print("\nHow many hours are you looking to book for this guitar lesson? (min 1 hour - max 3.5 hour): ");
                numHours = scanner.nextDouble();
            }
        }
        return numHours;
    }
    
    // declare display info method
    public static void displayInfo(String membershipType, double freeLessons, double hourlyRate, double baseCost) {
        System.out.println("------------------------------------------------------------------------------");
        System.out.println("Membership Type: " + membershipType);
        System.out.println("Free Guitar Lessons Included: " + freeLessons);
        System.out.println("Hourly Rate for Guitar Lessons: $" + hourlyRate);
        System.out.println("------------------------------------------------------------------------------");
        if (membershipType.equalsIgnoreCase("Silver")) {
            System.out.println("Silver Membership Base Cost: $" + baseCost);
        } else {
            System.out.println("Gold Membership Base Cost: $" + baseCost);
        }
        System.out.println("------------------------------------------------------------------------------");
        System.out.println();
    }
    
    // declare displayinvoice method
    public static void displayInvoice(double baseCost, int totalLessonsBooked, double totalHours, double totalLessonCharges) {
        System.out.println("\nInvoice:");
        System.out.println("Base Cost of Membership: $" + baseCost);
        System.out.println("Total Lessons Booked: " + totalLessonsBooked);
        System.out.println("Total Hours of Lessons: " + totalHours);
        System.out.println("Total Lesson Charges: $" + totalLessonCharges);
        System.out.println("Total Charges: $" + (baseCost + totalLessonCharges));
    }
    
    //declare get price lesson method
    public static double getPriceLesson(double freeLessons, double hourlyRate, double numHours) {
        if (freeLessons > 0) {
            return 0;
        } else {
            return hourlyRate * numHours;
        }
    }
}
