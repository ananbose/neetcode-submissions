class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map <int ,int> seen ;
        for ( auto i: nums) {
            auto it = seen.find(i);
            if (it != seen.end()){
            return true; 
            }
            seen.insert({i, i});
        }
        return false;
    }
};