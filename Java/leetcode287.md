# Problem Link

https://leetcode.com/problems/find-the-duplicate-number

## SS of submission

![LeetCode Submission](./image/leetcode287.png)

```Java
class Solution {
    public int findDuplicate(int[] nums) {

        int slow = nums[0];
        int fast = nums[nums[0]];

        while(slow!=fast){
            slow = nums[slow];
            fast = nums[nums[fast]];
        }

        slow = 0;
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }

        return fast;
        }
}


```

## Helpful Resources
https://youtu.be/wjYnzkAhcNk