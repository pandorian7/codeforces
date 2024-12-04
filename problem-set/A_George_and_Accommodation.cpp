#include <iostream>

using namespace std;

int main()
{
    int n, pi, qi, rooms = 0;

    cin >> n;
    while (n--)
    {
        cin >> pi >> qi;
        if (qi - pi >= 2)
            rooms++;
    }
    cout << rooms;
}