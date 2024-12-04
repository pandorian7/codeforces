#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int easy = 1;
    int res;
    while (n--)
    {
        cin >> res;
        if (res)
        {
            easy = 0;
            break;
        }
    }
    cout << (easy ? "EASY" : "HARD");
}