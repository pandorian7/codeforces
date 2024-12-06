#include <bits/stdc++.h>
using namespace std;
#define M 1000000001

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, tmp;
    vector<int> longest(M, 0);

    while (n--)
    {
        cin >> tmp;
        longest[tmp] = longest[tmp - 1] + 1;
    }

    return 0;
}