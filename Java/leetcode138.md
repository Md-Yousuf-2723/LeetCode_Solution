# Problem Link 
https://leetcode.com/problems/copy-list-with-random-pointer/

## SS of submission
![LeetCode Submission](./Image/leetcode138.png)

## Solution 1(O(n²) approach)


```JAVA
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        Node dummy = new Node(-1);
        Node tail = dummy;
        Node temp = head;

        while(temp!=null){
            tail.next = new Node(temp.val);

            if(temp.random==null){
                tail.next.random= null;
            }
            
            tail.next.random = temp.random;
            tail = tail.next;
            temp = temp.next;
        }

        Node tail2 = dummy.next;
        tail = dummy;
        temp = head;

      while(temp != null) {
        if(temp.random != null) {
            int steps = 0;
            Node t = head;
            while(t != temp.random) {
                t = t.next;
                steps++;
            }

            for (int i = 0; i < steps; i++) {
                tail2=tail2.next;
                
            }

            tail.next.random=tail2;

        
        }
        tail2 = dummy.next;
        tail = tail.next;
        temp = temp.next;
    }
        
        return dummy.next;

        
    }
}


```

## Optimal solution (O(n))
```JAVA
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    HashMap<Node, Node> visitedNode = new HashMap<Node,Node>();
    public Node copyRandomList(Node head) {
        if(head==null){
            return null;
        }
        if(this.visitedNode.containsKey(head)){
            return this.visitedNode.get(head);
        }
        Node newNode = new Node(head.val,null,null);
        this.visitedNode.put(head,newNode);

        newNode.next = copyRandomList(head.next);
        newNode.random = copyRandomList(head.random);

        return newNode;
        
    }
}
```

