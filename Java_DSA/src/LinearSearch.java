import java.util.Arrays;
import java.util.EnumSet;
import java.util.List;
import java.util.Objects;

    public class LinearSearch{
         static int search(int[] nums, int target) {
            for(int index = 0; index < nums.length; index++) {
            if (nums[index] == target) {
                return index;
            }
        }
            return -1;
    }
    public static void main(String[] args) {
        int[] nums= {1,2,3,4,5,6,7,8,9,10};
        int target = 8;
        //ginawa ko na static taas- LinearSearch ls = new LinearSearch()//abstraction- pwede pa 2

        //LinearSearch ls2 = new LinearSearch//d directly, pasok sa ls, gumagamit ng copy nya
        System.out.println(search(nums, target));

    }
}