// LongestPalindromicSubstring.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string longestPalindrome(string s)
{
    vector<vector<bool>> dp(s.length(), vector<bool>(s.length(), false));
    int maxLen = 1;
    int start = 0;
    
    for (int i = 0; i < s.length(); i++)
    {
        dp[i][i] = true;
    }

    for (int i = 0; i < s.length() - 1; i++)
    {
        if (s[i] == s[i + 1])
        {
            dp[i][i + 1] = true;
            start = i;
            maxLen = 2;
        }
    }

    for (int length = 3; length <= s.length(); length++)
    {
        for (int i = 0; i <= s.length() - length; i++)
        {
            int j = i + length - 1;

            if (s[i] == s[j] && dp[i + 1][j - 1])
            {
                dp[i][j] = true;

                if (length > maxLen)
                {
                    start = i;
                    maxLen = length;
                }
            }
        }
    }

    return s.substr(start, maxLen);
}

int main()
{

    cout << longestPalindrome("abcdadafasuaiausgvalalk");
}