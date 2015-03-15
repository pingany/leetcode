#include <string>
#include <iostream>
using namespace std;

bool isPalindorm[1000][1000] = {0};

void updateResult(int i , int j, int result[]) {
    int k = j -i +1;
    if (k > result[0]) {
        result[0] = k;
        result[1] = i;
        result[2] = j;
    }
}
string longestPalindrome(string s) {
    int n = s.length();
    if (n == 0)
        return "";
    int result[] = {1, 0, 0};
    for(int i = n-1; i >=0 ; i--) {
        isPalindorm[i][i] = true;
        if (i + 1 < n) {
            bool ok = isPalindorm[i][i+1] = s[i] == s[i+1];
            if(ok)
                updateResult(i , i+1, result);
        }
        for (int j = i+2; j < n; j++) {
            bool ok = isPalindorm[i][j] = s[i] == s[j] and isPalindorm[i+1][j-1];
            if(ok)
                updateResult(i, j, result);
        }
    }
    return s.substr(result[1], result[2]+1-result[1]);
}

class Solution {
public:
    string longestPalindrome(string s) {
        return ::longestPalindrome(s);
    }
};

int main() {
    cout << (Solution().longestPalindrome("a")) << endl;
}