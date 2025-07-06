public class CustomDeque {
    private int[] dequeArray;
    private int front, rear, size, capacity;

    // Constructor to initialize the deque
    public CustomDeque(int capacity) {
        this.capacity = capacity;
        dequeArray = new int[capacity];
        front = -1;
        rear = 0;
        size = 0;
    }

    // Check if the deque is full
    public boolean isFull() {
        return size == capacity;
    }

    // Check if the deque is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Add an element to the front of the deque
    public void insertFront(int element) {
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
    public void insertRear(int element) {
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

    // Delete an element from the front of the deque
    public int deleteFront() {
        if (isEmpty()) {
            throw new RuntimeException("Deque Underflow");
        }

        int element = dequeArray[front];

        if (front == rear) { // Only one element was present
            front = -1;
            rear = -1;
        } else if (front == capacity - 1) { // Wrap around
            front = 0;
        } else {
            front++;
        }

        size--;
        return element;
    }

    // Delete an element from the rear of the deque
    public int deleteRear() {
        if (isEmpty()) {
            throw new RuntimeException("Deque Underflow");
        }

        int element = dequeArray[rear];

        if (front == rear) { // Only one element was present
            front = -1;
            rear = -1;
        } else if (rear == 0) { // Wrap around
            rear = capacity - 1;
        } else {
            rear--;
        }

        size--;
        return element;
    }

    // Get the front element of the deque
    public int getFront() {
        if (isEmpty()) {
            throw new RuntimeException("Deque is empty");
        }
        return dequeArray[front];
    }

    // Get the rear element of the deque
    public int getRear() {
        if (isEmpty()) {
            throw new RuntimeException("Deque is empty");
        }
        return dequeArray[rear];
    }

    public int getSize() {
        return size;
    }

    // Main method to test the deque operations
    public static void main(String[] args) {
        CustomDeque deque = new CustomDeque(5);

        deque.insertFront(1);
        deque.insertFront(2);
        deque.insertFront(3);
        deque.insertRear(4);
        deque.insertRear(5);

        // Insert elements at the rear
        deque.insertRear(10);
        deque.insertRear(20);
        deque.insertRear(30);

        // Insert elements at the front
        deque.insertFront(5);
        deque.insertFront(1);

        // Print front and rear elements
        System.out.println("Front element: " + deque.getFront()); // Output: 1
        System.out.println("Rear element: " + deque.getRear());   // Output: 30

        // Delete elements from the front
        System.out.println("Deleted from front: " + deque.deleteFront()); // Output: 1
        System.out.println("Deleted from front: " + deque.deleteFront()); // Output: 5

        // Delete elements from the rear
        System.out.println("Deleted from rear: " + deque.deleteRear()); // Output: 30
        System.out.println("Deleted from rear: " + deque.deleteRear()); // Output: 20

        // Print front and rear elements after deletions
        System.out.println("Front element after deletions: " + deque.getFront()); // Output: 10
        System.out.println("Rear element after deletions: " + deque.getRear());   // Output: 10
    }
}
