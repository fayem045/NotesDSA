public class PrelimsEx {
    public static int noOfCombinations(int[] arr1, int[] arr2, int target) {
        int comNum = 0;
        for (int num1 : arr1) {
            int num2target = target-num1;
            for (int num2 : arr2) {
                if (num2 == num2target) {
                    comNum++;
                }
            }
        }

        return (comNum > 0) ? comNum : -1;
    }

    public static void main(String[] args) {
        System.out.println(noOfCombinations(new int[]{1,2,3}, new int[]{4,5,6}, 7));
    }
}