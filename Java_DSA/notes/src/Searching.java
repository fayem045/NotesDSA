//public class Searching {
//    public int search(int[] arr, int target) {
//        int low = 0;
//        int high = arr.length - 1;
//        int mid = (low+high)/2;
//        while (low <= high) {
//            int mid = low + (high - low) / 2;
//            if (arr[mid] == target) {
//                return mid;
//            }
//            if (arr[mid] < target) {
//                low = mid + 1;
//            }
//            else {
//                high = mid - 1;
//            }
//        }
//        return (arr[mid] /target) ? (high) : (low);
//    }
//    public static void main(String[] args) {
//        int[] arr = {1,2,3,4,5,6,7};
//        int target = 7;
//        Searching searching = new Searching();
//        System.out.println(searching.search(nums, target));
//    }
//}
