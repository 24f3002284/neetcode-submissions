class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> freq1;
        unordered_map<char,int> freq2;

        for(char ch:s){
            freq1[ch]++;
        }

        for(char ch:t){
            freq2[ch]++;
        }

        for(auto p: freq1){
            if(freq1[p.first]!=freq2[p.first])
                return false;
        }

    return (s.length()==t.length());
    }
};
