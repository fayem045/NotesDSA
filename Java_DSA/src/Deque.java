import java.util.ArrayDeque;
import java.util.Deque;

public class DeqPract {
    private String[] dequeArray;
    private int front, rear, size, capacity;

    public DeqPract(int capacity) {
        this.capacity = capacity;
        dequeArray = new String[capacity];
        front = -1;
        rear = 0;
        size = 0;
    }

    // Check if the deque is full
    public boolean isFull() {
        return size == capacity;
    }
    public void insertFront(String element) {
        if (isFull()) {
            System.out.println("Deque Overflow");
            return;
        }

        if (front == -1) { // First element to be inserted
            front = 0;
            rear = 0;
        } else if (front == 0) { // Front at the first position, wrap around
            front = capacity - 1;
        } else {
            front--;
        }

        dequeArray[front] = element;
        size++;
    }

    // Add an element to the rear of the deque
    public void insertRear(String element) {
        if (isFull()) {
            System.out.println("Deque Overflow");
            return;
        }

        if (front == -1) { // First element to be inserted
            front = 0;
            rear = 0;
        } else if (rear == capacity - 1) { // Rear at the last position, wrap around
            rear = 0;
        } else {
            rear++;
        }

        dequeArray[rear] = element;
        size++;
    }

    // Get the front element of the deque
    public String getFront() {
        if (size == 0) {
            throw new RuntimeException("Deque is empty");
        }
        return dequeArray[front];// Return the front element
    }

    public static void main(String[] args) {
        DeqPract deque = new DeqPract(5);

        deque.insertFront("Okay");
        deque.insertFront("Ka");
        deque.insertFront("lang");
        deque.insertRear("ba");
        deque.insertRear("Self?");
        deque.insertRear("yes");


        // Example usage
        System.out.println("Front element after insertions: " + deque.getFront());
    }
}
