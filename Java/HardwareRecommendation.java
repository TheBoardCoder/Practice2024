


import java.util.Scanner;

public class HardwareRecommendation {

    static final double CLOCK_SPEED_GPU_LOW_THRESHOLD = 800;
    static final double CLOCK_SPEED_GPU_HI_THRESHOLD = 2000;
    static final double CLOCK_SPEED_CPU_LOW_THRESHOLD = 1000;
    static final double CLOCK_SPEED_CPU_HI_THRESHOLD = 5500;

    static final int CORES_LOW_THRESHOLD = 1;
    static final int CORES_HI_THRESHOLD = 20;

    static int computerNum = 0;
    static double totalPerformanceScore = 0.0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double averagePerformanceScore = 0.0;
        char repeat;

        do {
            displayTitle();

            System.out.print("Please enter the type of processor: ");
            String processor = scanner.nextLine();

            double gpuClockSpeed;
            do {
                System.out.print("Please enter the clock speed (in Megahertz) of your graphics card: ");
                gpuClockSpeed = scanner.nextDouble();
                if (gpuClockSpeed < CLOCK_SPEED_GPU_LOW_THRESHOLD || gpuClockSpeed > CLOCK_SPEED_GPU_HI_THRESHOLD) {
                    System.out.println("The clock speed should be between " + CLOCK_SPEED_GPU_LOW_THRESHOLD + " and " + CLOCK_SPEED_GPU_HI_THRESHOLD + " Megahertz");
                }
            } while (gpuClockSpeed < CLOCK_SPEED_GPU_LOW_THRESHOLD || gpuClockSpeed > CLOCK_SPEED_GPU_HI_THRESHOLD);

            double cpuClockSpeed;
            do {
                System.out.print("Please enter the clock speed (in Megahertz) of your processor: ");
                cpuClockSpeed = scanner.nextDouble();
                if (cpuClockSpeed < CLOCK_SPEED_CPU_LOW_THRESHOLD || cpuClockSpeed > CLOCK_SPEED_CPU_HI_THRESHOLD) {
                    System.out.println("The clock speed should be between " + CLOCK_SPEED_CPU_LOW_THRESHOLD + " and " + CLOCK_SPEED_CPU_HI_THRESHOLD + " Megahertz");
                }
            } while (cpuClockSpeed < CLOCK_SPEED_CPU_LOW_THRESHOLD || cpuClockSpeed > CLOCK_SPEED_CPU_HI_THRESHOLD);

            int cpuCoreNumber;
            do {
                System.out.print("Please enter the number of cores of your processor: ");
                cpuCoreNumber = scanner.nextInt();
                if (cpuCoreNumber < CORES_LOW_THRESHOLD || cpuCoreNumber > CORES_HI_THRESHOLD) {
                    System.out.println("The number of cores should be between " + CORES_LOW_THRESHOLD + " and " + CORES_HI_THRESHOLD);
                }
            } while (cpuCoreNumber < CORES_LOW_THRESHOLD || cpuCoreNumber > CORES_HI_THRESHOLD);

            scanner.nextLine(); // consume the newline

            char overclock;
            do {
                System.out.print("Is the hardware overclock-friendly? (Enter y for yes or n for no): ");
                overclock = scanner.nextLine().toLowerCase().charAt(0);
                if (overclock != 'y' && overclock != 'n') {
                    System.out.println("Error: the response should be y for yes or n for no");
                }
            } while (overclock != 'y' && overclock != 'n');

            int monitorResolution = getMenuChoice(scanner);
            double multiplier = getMultiplierValue(monitorResolution);
            String monitorResolutionAsString = getResolutionString(monitorResolution);
            double performanceScore = calculatePerformanceScore(gpuClockSpeed, cpuClockSpeed, cpuCoreNumber, multiplier);
            String recommendedQuality = getRecommendedQuality(performanceScore);

            displayInformation(gpuClockSpeed, cpuClockSpeed, cpuCoreNumber, monitorResolutionAsString, performanceScore, recommendedQuality, overclock);

            System.out.print("Would you like to check another recommendation? Enter y for yes or n for no: ");
            repeat = scanner.nextLine().toLowerCase().charAt(0);

            computerNum++;
            totalPerformanceScore += performanceScore;

        } while (repeat == 'y');

        if (computerNum > 0) {
            averagePerformanceScore = totalPerformanceScore / computerNum;
        }
        System.out.println("Average performance score: " + averagePerformanceScore);
        scanner.close();
    }

    private static void displayTitle() {
        System.out.println("Hardware Recommendation System");
    }

    private static int getMenuChoice(Scanner scanner) {
        System.out.print("Please enter the monitor resolution (1 for 720p, 2 for 1080p, 3 for 1440p, 4 for 4K): ");
        return scanner.nextInt();
    }

    private static double getMultiplierValue(int monitorResolution) {
        switch (monitorResolution) {
            case 1:
                return 1.0;
            case 2:
                return 1.5;
            case 3:
                return 2.0;
            case 4:
                return 2.5;
            default:
                return 1.0;
        }
    }

    private static String getResolutionString(int monitorResolution) {
        switch (monitorResolution) {
            case 1:
                return "720p";
            case 2:
                return "1080p";
            case 3:
                return "1440p";
            case 4:
                return "4K";
            default:
                return "Unknown";
        }
    }

    private static double calculatePerformanceScore(double gpuClockSpeed, double cpuClockSpeed, int cpuCoreNumber, double multiplier) {
        return (gpuClockSpeed * 0.5 + cpuClockSpeed * 0.3 + cpuCoreNumber * 0.2) * multiplier;
    }

    private static String getRecommendedQuality(double performanceScore) {
        if (performanceScore > 15000) {
            return "Ultra";
        } else if (performanceScore > 10000) {
            return "High";
        } else if (performanceScore > 5000) {
            return "Medium";
        } else {
            return "Low";
        }
    }

    private static void displayInformation(double gpuClockSpeed, double cpuClockSpeed, int cpuCoreNumber, String monitorResolutionAsString, double performanceScore, String recommendedQuality, char overclock) {
        System.out.println("GPU Clock Speed: " + gpuClockSpeed + " MHz");
        System.out.println("CPU Clock Speed: " + cpuClockSpeed + " MHz");
        System.out.println("CPU Core Number: " + cpuCoreNumber);
        System.out.println("Monitor Resolution: " + monitorResolutionAsString);
        System.out.println("Performance Score: " + performanceScore);
        System.out.println("Recommended Quality: " + recommendedQuality);
        System.out.println("Overclock-friendly: " + (overclock == 'y' ? "Yes" : "No"));
    }
}
