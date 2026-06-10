class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        
        for(string word:strs){
            string cnt(26,'0');
            for(char ch:word){
                cnt[(ch-'a')]++;
            }    

            mp[cnt].push_back(word);
        }

        vector<vector<string>> ans;
        for(auto p:mp){
            ans.push_back(p.second);
        }

    return ans;
    }
};
