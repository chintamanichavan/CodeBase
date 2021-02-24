
public class ReverseString {
    public static String reverseString(String args) {
        char strLetter = (char)0;
        StringBuilder sb = new StringBuilder();
        String reverseOut = "";
        for(int i= args.length() - 1;i >= 0;i--){
            strLetter = args.charAt(i);
            reverseOut = sb.append(strLetter).toString();
        }
        System.out.println(reverseOut);
        return reverseOut;
    }
    public static void main(String[] args) {
        String input = "lilac";
        reverseString(input);
    }
}
