#include <iostream>

using namespace std;

int main()
{
    long long n;
    cin >> n;
    long long odd, even;
    odd = even = n / 2;
    if (n % 2)
        odd++;
    cout << (even * 2 + even * even - even) - odd * odd;
}