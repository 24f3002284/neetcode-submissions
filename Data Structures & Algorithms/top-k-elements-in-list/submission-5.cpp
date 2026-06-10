class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int n=nums.size();

        for(int num:nums){
            mp[num]++;
        }

        vector<vector<int>> arr(n+1);

        for(pair p:mp){
            arr[p.second].push_back(p.first);
        }

        int i=n;
        vector<int> ans;
        while(k>0){
            if(arr[i].size()!=0){
                
                for(int it:arr[i]){
                    k--;
                    ans.push_back(it);
                }
            }
            i--;
        }
    return ans;
    }
};
