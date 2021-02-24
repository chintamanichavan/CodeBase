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

/*
Two Sum
Given an array of integers, return the indices of the two numbers whose sum is equal to a given target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Solution:
METHOD 1. Naive approach: Use two for loops

The naive approach is to just use two nested for loops and check if the sum of any two elements in the array is equal to the given target.

Time complexity: O(n^2)

METHOD 2. Use a HashMap (Most efficient)

You can use a HashMap to solve the problem in O(n) time complexity. Here are the steps:

    Initialize an empty HashMap.
    Iterate over the elements of the array.
    For every element in the array -
        If the element exists in the Map, then check if it’s complement (target - element) also exists in the Map or not. If the complement exists then return the indices of the current element and the complement.
        Otherwise, put the element in the Map, and move to the next iteration.

Time complexity: O(n)

METHOD 3. Use Sorting along with the two-pointer sliding window approach

There is another approach which works when you need to return the numbers instead of their indexes. Here is how it works:

    Sort the array.
    Initialize two variables, one pointing to the beginning of the array (left) and another pointing to the end of the array (right).
    Loop until left < right, and for each iteration
        if arr[left] + arr[right] == target, then return the indices.
        if arr[left] + arr[right] < target, increment the left index.
        else, decrement the right index.

This approach is called the two-pointer sliding window approach. It is a very common pattern for solving array related problems.

Time complexity: O(n*log(n))
*/
