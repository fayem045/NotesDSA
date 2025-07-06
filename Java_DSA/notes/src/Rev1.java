//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.List;

//public class Rev1 {
//    public static int[] findIntersection(int[] num1, int[] num2) {
//        List<Integer> res = new ArrayList<>();//declare new list
//
//        Arrays.sort(num1);
//        Arrays.sort(num2);
//
//        int i = 0, j = 0;//start sa index yung d array
//        while (i < num1.length && j < num2.length) {
//            if (num1[i] == num2[j]) {
//                    //wala pang laman na same yung new list, get yung ele if wala pa yung i
//                if (res.isEmpty() || res.get(res.size() - 1) != num1[i]) {
//                    // Add to result if it's not a duplicate
//                    res.add(num1[i]);// add to the result if they match
//                }
//                i++;//move on na sya parang si Ella lang
//                j++;//move
//            } else if (num1[i] < num2[j]) {
//                i++; // move in num1
//            } else {
//                j++; // move in num2
//            }
//        }
//
//        int[] resArray = new int[res.size()];//methods para kunin buo mga nagrepeat
//                for(int k = 0; k < res.size(); k++){
//                    resArray[k] = res.get(k);//k yung nagawang last array na dineclare
//                }
//                return resArray;//ibabalik na final output
//            }
//    public static void main(String[] args) {
//        int[] num1 ={4,9,5};
//        int[] num2 ={9,4,9,8,4};
//        //output:2
//        int[] result = findIntersection(num1, num2);
//        System.out.print("[");
//            for (int i = 0; i < result.length; i++) {
//                System.out.print(result[i]);
//                if (i != result.length - 1) {
//                    System.out.print(",");
//                }
//            }
//            System.out.println("]");
//    }
//}

//if namumula args= kulang else if or some parts
//END OF PARCHD= KULANG } CLOSE

////USING HASHET= HINDI SORTERD
/*1.initialized anothr list
 2. Logic to put the elements in new list
 3.Print
 */
//import java.util.ArrayList;
import java.util.HashSet;
//import java.util.List;
import java.util.Set;

public class Rev1 {
    public static int[] findIntersection(int[] num1, int[] num2) {
        Set<Integer> set = new HashSet<>();
        Set<Integer> intersection = new HashSet<>();

        // Add all elements of num1 to the set
        for (int num : num1) {
            set.add(num);
        }

        // Check for intersection with num2
        for (int num : num2) {
            if (set.contains(num)) {
                intersection.add(num); // add to intersection if present in both arrays
            }
        }

        // Convert the result set to an array
        int[] resArray = new int[intersection.size()];
        int index = 0;
        for (int num : intersection) {
            resArray[index++] = num;
        }

        return resArray; // return the final output
    }

    public static void main(String[] args) {
        int[] num1 = {4, 9, 5};
        int[] num2 = {9, 4, 9, 8, 4};

        // Get the result and print it
        int[] result = findIntersection(num1, num2);

        // Output format: [4, 9]
        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i != result.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
