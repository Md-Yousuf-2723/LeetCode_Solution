# Problem Link 
https://leetcode.com/problems/plus-one/
## SS of submission
![LeetCode Submission](./images/leetcode62.png)

```C++
class Solution {
public:
    int uniquePaths(int n, int m) {
        
            vector<int>prev(m+1,0),cur(m+1,0);

            prev[1]=1;

            for(int i=1;i<=n;i++){
                for(int j=1;j<=m;j++) cur[j]=cur[j-1]+prev[j];
                prev=cur;
            }

     return prev[m];

    }
};
```
