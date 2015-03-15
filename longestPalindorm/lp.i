
%include <std_string.i>
%{
#include <string>
using namespace std;

string longestPalindrome(string s);   
%}

std::string longestPalindrome(std::string s);