class MyQueue {
    Stack<Integer> bucket;
    Stack<Integer> q;
    
    public MyQueue() {
        bucket=new Stack<>();
        q=new Stack<>();
    }
    
    public void push(int x) {
        while(!q.empty()){
            bucket.push(q.pop());
        }
        q.push(x);
        while(!bucket.empty()){
            q.push(bucket.pop());
        }
    }
    
    public int pop() {
        return q.pop();
    }
    
    public int peek() {
        return q.peek();
    }
    
    public boolean empty() {
        return q.size()==0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */