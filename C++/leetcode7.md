# Problem Link 
https://leetcode.com/problems/reverse-integer/description/

## SS of submission
![LeetCode Submission](./images/leetcode7.png)

```C++
int reverse(int x) {
    int rev = 0;
    while (x != 0) {
        int ld = x % 10;
        if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && ld > 7)) return 0;
        if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && ld < -8)) return 0;
        rev = rev * 10 + ld;
        x /= 10;
    }
    return rev;
}
```
