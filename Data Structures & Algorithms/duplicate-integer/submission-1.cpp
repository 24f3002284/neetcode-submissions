class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    //     sort(nums.begin(),nums.end());
    //     int n=nums.size();

    //     for(int i=0;i<n-1;i++){
    //         if(nums[i]==nums[i+1]) return true;
    //     }
    // return false;

    //TC=O(n)
    unordered_set<int> st;
    int n=nums.size();
    for(int i=0;i<n;i++){
        st.insert(nums[i]);
    }
    return st.size()!=n;
    }
};