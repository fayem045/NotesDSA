import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Pract1 {
    public static int[] combine(int[] arr1, int[] arr2) {
        List<Integer> res = new ArrayList<>();
        int i = 0, j = 0;//start sa index yung d array
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                res.add(arr1[i]);//res kasi yung name doon sa ginawang array
                i++;
            }else{
                res.add(arr2[j]);
                j++;
            }
        }
        while (i < arr1.length) {
            res.add(arr1[i]);
            i++;
        }
        while (j < arr2.length) {
            res.add(arr2[j]);
            j++;
        }
        int[] resArray = new int[res.size()];
        for(int k = 0; k < res.size(); k++){
            resArray[k] = res.get(k);
        }
        return resArray;//ibabalik na final output
    }
    public static void longestSubarray(int[] arr, int k) {
        int left = 0, right = 0;
        int windowSum = 0;
        int maxLength = 0;
        int bestLeft = 0;
        int bestRight = -1;

        for (int i = 0; i < arr.length; i++) {
            windowSum += arr[right];

            while(windowSum >= k && left <= right){
                windowSum -= arr[left];
                left++;
            }
            if(right - left +1 > maxLength){
                maxLength = right - left +1;
                bestLeft = left;
                bestRight = right;
            }
        }
        System.out.println("Length of the longest subarray: " + maxLength);
        if (maxLength > 0) {
            System.out.println("Longest subarray: " + Arrays.toString(Arrays.copyOfRange(arr, bestLeft, bestRight + 1)));
        } else {
            System.out.println("No valid subarray found.");
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5, 7};
        int[] arr2 = {2, 4, 1, 7};//start sa front both
        System.out.println(Arrays.toString(combine(arr1, arr2)));//array print

        int[] mergeArray = combine(arr1, arr2);//string
        for (int num : mergeArray) {
            System.out.print(num + " ");
            int[] arr3 = mergeArray;
            int k = 5;
            longestSubarray(arr3, k);

        }
    }
}