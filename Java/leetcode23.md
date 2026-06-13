# Problem Link

https://leetcode.com/problems/merge-k-sorted-lists

## SS of submission

![](./Image/leetcode23.png)

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for(ListNode list : lists){
            while(list != null){
                minHeap.add(list.val);
                list = list.next;
            }

        }

        ListNode dummy = new ListNode(69);
        ListNode merged = dummy;

        while(!minHeap.isEmpty()){
            merged.next = new ListNode(minHeap.remove());
            merged = merged.next;
        }

        return dummy.next;

    }
}

```
