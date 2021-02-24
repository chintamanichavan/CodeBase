public class ValidPalindrome {
    public static boolean validPalindrome(String args) {
        char strLetter = (char)0;
        StringBuilder sb = new StringBuilder();
        String reverseOut = "";
        for(int i= args.length() - 1;i >= 0;i--){
            strLetter = args.charAt(i);
            reverseOut = sb.append(strLetter).toString();
        }
        if ( args.equals(reverseOut)){
            System.out.println("It is a valid PalinDrome.");
            return true;
        }
        return false;
    }
    public static void main(String[] args) {
        String input = "dad";
        validPalindrome(input);
    }
}
