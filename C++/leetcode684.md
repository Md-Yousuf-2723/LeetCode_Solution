# Problem Link 
https://leetcode.com/problems/redundant-connection/description/

## SS of submission
![LeetCode Submission](./images/leetcode684.png)

```C++
// TC: O(1)
class DSU{
    vector<int> parent, size, rank;
public:
    DSU(int n){
        for(int i = 0; i <= n; i++){
            parent.push_back(i);
            size.push_back(1);
            rank.push_back(0);
        }    
    }

    int findParent(int node){
        if(parent[node] == node){
            return node;
        }
        return parent[node] = findParent(parent[node]); // Path compression
    }
    
    void unionBySize(int u, int v){
        u = findParent(u); // Ultimate Parent of u in it's set
        v = findParent(v); // Ultimate Parent of v in it's set
        
        // Both are from same set
        if(u == v){
            return;
        }

        // Connect Smaller to the Bigger set
        if(size[u] < size[v]){
            parent[u] = v;
            size[v] += size[u];
        }else{
            parent[v] = u;
            size[u] += size[v];
        }
    }

    void unionByRank(int u, int v){
        u = findParent(u); // Ultimate Parent of u in it's set
        v = findParent(v); // Ultimate Parent of v in it's set
        
        // They are from same set
        if(u == v){
            return;
        }

        // Connect smaller rank to higher rank
        if(rank[u] == rank[v]){
            parent[v] = u;
            rank[u]++;
        }else if(rank[u] > rank[v]){
            parent[v] = u;
        }else{
            parent[u] = v;
        }
    }
};


class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<vector<int>> ans;
        DSU dsu(edges.size());
        for(auto u : edges){
            if(dsu.findParent(u[0]) != dsu.findParent(u[1])){
                dsu.unionByRank(u[0], u[1]);
            }else{
                ans.push_back({u[0], u[1]});
            }
        }
        return ans.back();      
    }
};
```

## Helpful Resources
- Go to [AlgoVerse](https://algooverse.vercel.app/) and check out DSU code for better understanding. GOOD LUCK!
