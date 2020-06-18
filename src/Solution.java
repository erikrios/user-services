import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Solution {

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {
        int totalValleys = 0;
        int state = 0;
        String preState = "";

        for (int i = 0; i < n; i++) {
            char currentState = s.charAt(i);
            boolean isSeaLevel;

            if (currentState == 'D') {
                state--;
            } else {
                state++;
            }

            if (state == 0) {
                isSeaLevel = true;
            } else if (state < 0) {
                isSeaLevel = false;
                preState = "Valleys";
            } else {
                isSeaLevel = false;
                preState = "Mountain";
            }

            if (isSeaLevel && preState.equalsIgnoreCase("Valleys")) {
                totalValleys++;
            }
        }

        return totalValleys;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\\r\\n|[\\n\\r\\u2028\\u2029\\u0085])?");

        String s = scanner.nextLine();

        int result = countingValleys(n, s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
