# Problem Link 
https://leetcode.com/problems/copy-list-with-random-pointer/description/

## SS of submission
![LeetCode Submission](./images/leetcode138.png)

```C++
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        Node* curr = head;
        while (curr) {
            Node* newNode = new Node(curr->val);
            newNode->next = curr->next;
            curr->next = newNode;
            curr = newNode->next;
        }

        curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }

        curr = head;
        Node* newHead = head->next;
        Node* newCurr = newHead;
        while (curr) {
            curr->next = newCurr->next;
            curr = curr->next;
            if (curr) {
                newCurr->next = curr->next;
                newCurr = newCurr->next;
            }
        }

        return newHead;
    }
};
```

## Helpful Resources
Yt video that helped 👉
https://youtu.be/_GBo_CgST1M?si=Eoo9IGxgBkBNmXlQ