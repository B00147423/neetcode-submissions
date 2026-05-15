class Solution {

    vector<vector<int>> res;
    vector<int> curr;
public:
    vector<vector<int>> combine(int n, int k) {
        dfs(n, k, 1);
        return res;
    }
private:
    void dfs(int n, int k, int i){
        if(curr.size() == k){
            res.push_back(curr);
            return;
        }

    
        for(int num = i; num <= n; num++)
        {
            curr.push_back(num);
            dfs(n, k, num + 1);
            curr.pop_back();
        }
    }
};

/*
retur nall possible combinations of k nums chosen fro m1 to n; 
Input: n = 3, k = 2


i = 1

append res = 1, 

i = 2, append res = 2

i == k 

*/