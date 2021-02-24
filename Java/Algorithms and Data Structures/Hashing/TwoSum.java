import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer,Integer> numsMap = new HashMap<Integer,Integer>();
        for(int i=0; i<nums.length;i++){
            numsMap.put(nums[i], i);
        }
        for(int i=0;i<nums.length;i++){
            if(numsMap.containsKey(target - nums[i])){
                result[0] = nums[i];
                result[1] = target - nums[i]; 
            }
        }
        System.out.println(Arrays.toString(result));
        return result;
    }
    public static void main(String[] args) {
        int[] nums = {1,4,6,7,8,3};
        int target = 11;
        twoSum(nums, target);
    }
}
