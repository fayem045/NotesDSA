import java.util.ArrayDeque;
import java.util.Deque;

public class Queue{
    private Deque<Integer> dequeue;

    public Queue(){
        dequeue = new ArrayDeque<>();
    }

    public void push(int q){
        dequeue.push(q);
    }

    public int pop(){
        if(dequeue.isEmpty()){
            return -1;
        }
        return dequeue.pop();
    }
    public boolean isEmpty(){
            return dequeue.isEmpty();
        }

    public int peek(){
        if (isEmpty()){
            throw new NullPointerException("none");
        }
        return dequeue.peek();
    }

    public static void main(String[] args){
        Queue q = new Queue();

        q.push(1);  // Push elements into the deque
        q.push(2);
        System.out.println("Peek: " + q.peek());  // Should print 2 (last pushed element)
        System.out.println("Pop: " + q.pop());    // Should remove and print 2
        System.out.println("Is empty: " + q.isEmpty());  // Should print false
        System.out.println("Pop: " + q.pop());    // Should remove and print 1
    }
}


////Input: s = "hello"
////▪ Output: 2
//public class Pract {
//    public static boolean isVowel(char ch) {
//         ch = Character.toUpperCase(ch);//paramacomapre lahat, convert sa upper lahat
//        return(ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' );
//    }
//    public static int CountV(String str){
//            int count = 0; // Initialize count to 0
//            for (int i = 0; i < str.length(); i++) {
//                if (isVowel(str.charAt(i))) {
//                    ++count;
//                }
//            }
//            return count;
//        }
//    public static int Repeat(String str, char ch) {
//        int count = 0;
//        str = str.toLowerCase();  // Convert string to lower case
//        ch = Character.toLowerCase(ch);  // Convert character to lower case
//
//        for (int i = 0; i < str.length(); i++) {
//            if (str.charAt(i) == ch) {
//                ++count;
//            }
//        }
//        return count;  // Move return statement outside of the loop
//    }
//
//    public static int countLetters(String str) {
//        int count = 0;
//        for (int i = 0; i < str.length(); i++) {
//            if (Character.isLetter(str.charAt(i))) {
//                ++count;
//            }
//        }
//        return count;
//    }
//
//    public static void main(String[] args) {
//            String s = "Hello";
//            System.out.println(CountV(s));
//            System.out.println(Repeat(s, 'l'));
//            System.out.println(countLetters(s));
//        }
//    }
