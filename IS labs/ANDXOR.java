public class ANDXOR {
    public static void main(String[] args) {
        String str = "Yash Bhamare";

        System.out.println("Original String: " + str);

        System.out.println("Result of AND operation with 127:");
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            int result = ch & 127;
            System.out.print( (char)result+ "    ");
        }
        System.out.println();

        System.out.println("Result of XOR operation with 127:");
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            int result = ch ^ 127;
            System.out.print( (char)result+"    ");
        }
        System.out.println();
    }
}
