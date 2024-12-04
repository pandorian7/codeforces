#include <iostream>

using namespace std;

int main()
{
    int n, mag1, mag2, groups = 1;
    cin >> n;
    n--;
    cin >> mag1;
    while (n--)
    {
        cin >> mag2;
        if (mag1 != mag2)
            groups++;
        mag1 = mag2;
    }
    cout << groups;
}