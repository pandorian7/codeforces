#include <iostream>

using namespace std;

int main()
{
    int n, val;
    cin >> n;
    int gifts[n];
    for (int i = 0; i < n; i++)
    {
        cin >> val;
        gifts[val - 1] = i + 1;
    }
    for (int i = 0; i < n; i++)
    {
        cout << gifts[i] << " ";
    }
}