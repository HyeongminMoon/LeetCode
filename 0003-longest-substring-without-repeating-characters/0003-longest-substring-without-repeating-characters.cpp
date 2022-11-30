class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string cur_string = "";
        int max_len = 0;
        
        for(char _letter: s){
            cur_string = GetLastSplit(cur_string, _letter);
            cur_string += _letter;
            
            if (cur_string.length() > max_len){
                max_len = cur_string.length();
            }
        }
        
        return max_len;
        
    }
    
    string GetLastSplit(string s, char letter){
        for(int i=0; i < s.size(); i++){
            if (s.at(i) == letter){
                return s.substr(i+1);
            }
        }
        return s;
    }
};