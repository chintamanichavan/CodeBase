public class ReverseInteger {
    public static int reverseInteger(int args) {
        int reverseOut = 0,input = args,rem = 0;
        while(input > 0){
            rem = input % 10;
            input = input / 10;
            reverseOut = (reverseOut * 10) + rem;
        }
        System.out.println(reverseOut);
        return reverseOut;
    }
    public static void main(String[] args) {
        int input = 89;
        reverseInteger(input);
    }
}
