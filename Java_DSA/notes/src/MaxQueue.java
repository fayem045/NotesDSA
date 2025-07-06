import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class MaxQueue { //need class
    private Deque<Integer> queue;    // Stores the actual queue elements
    private Deque<Integer> maxDeque; // Stores the max elements in decreasing order

    private MaxQueue() {
        queue  = new ArrayDeque<>();//initialized list
        maxDeque  = new ArrayDeque<>();
    }
    public void enqueue(int x) {
        queue.addLast(x);//na-add na sa queue
        while (!maxDeque.isEmpty() && x > maxDeque.getLast()) {//if not empty
            maxDeque.removeLast();
        }
        maxDeque.addLast(x);
    }
    public List<Integer> dequeue() {//List inside a methods
        if (queue.isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int removed = queue.removeFirst();
        if (removed == maxDeque.getFirst()) {
            maxDeque.removeFirst();
        }
       List<Integer> remainingElements = new ArrayList<>(queue);//to have list []
        return remainingElements;//[ilagay sa list]
    }

    public int getMax() {
        if (!maxDeque.isEmpty()) {
            return maxDeque.getFirst();
        }
        throw new RuntimeException("Queue is empty");
    }
    public int front(){
        if (!queue.isEmpty()) {
            return queue.getFirst();
        }
        throw new RuntimeException("Queue is empty");
    }

    public void printQueue() {
        System.out.println(queue);
    }

    public static void main(String[] args) {
        MaxQueue maxQueue = new MaxQueue();//need in class name

        maxQueue.enqueue(1);	// Queue is now [1]
    	maxQueue.enqueue(3);   	// Queue is now [1, 3]
    	maxQueue.enqueue(2);// Queue is now [1, 3, 2]
        maxQueue.enqueue(4);


        maxQueue.printQueue();
        System.out.println(maxQueue.getMax());     	// returns 3
	    System.out.println(maxQueue.dequeue());    	// Removes 1, queue is now [3, 2]
        System.out.println(maxQueue.front());      	// returns 3
        System.out.println(maxQueue.getMax());     	// returns 3

    }
}
