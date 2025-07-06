//hash- duplicate
//hashmap-satrt left index identitify duplicate
import java.util.HashMap;
import java.util.Map;

public class Rev2 {
    public static int firstRepeat(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();//new map for repeacting elements

        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(nums[i])) {
                return seen.get(nums[i]); // Return the index of the first occurrence
            }
            seen.put(nums[i], i);
        }

        return -1; // Return -1 if no repeating element is found
    }

    public static void main(String[] args) {
        int[] nums = {4, 5,9, 8, 7};

        int firstRepeat = firstRepeat(nums);

        if (firstRepeat != -1) {
            int element = nums[firstRepeat];//here dapat para hindi magerror, it only does if meant yung condi
            System.out.println("First repeating element is " + element  +" at index " + firstRepeat);
        } else {
            System.out.println("-1");
        }
    }
}


//import java.util.Arrays;
//import java.util.List;
//import java.util.Objects;
//
//public class Rev2 {
//    public static String firstRepeat(int[] nums) {
//        int left = 0; // Pointer starting from the beginning
//        int right = nums.length - 1; // Pointer starting from the end
//
//        while (left != right) {
//            int minuend = nums[left] - nums[right];
//
//            if (minuend == 0) {
//                return String.format("[ %d ]", nums[left], nums[right], minuend); // Pair found, return true
//            } else {
//                left++; // Move the left pointer to increase the sum
//                right--; // Move the right pointer to decrease the sum
//            }
//        }
//
//        return "-1"; // No pair found, return false
//    }
//
//    public static void main(String[] args) {
//        int[] nums = {4, 5, 7, 8, 7};
//        int target = 0;
////output:3
//        int firstRepeat = firstRepeat(nums);
//
//        if (firstRepeat != -1) {
//            System.out.println("First repeating element is " + target + " is at index " + firstRepeat);
//        } else {
//            System.out.println("-1");
//
//        }
//    }
//}