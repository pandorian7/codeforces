#include <iostream>

using namespace std;

int main()
{
    int t, n;
    int sum1, sum2, sum, n1, n2, val, div1, div2;
    cin >> t;
    while (t--)
    {
        cin >> n;
        n1 = n2 = n / 2;
        if (n % 2)
            n1++;
        sum1 = sum2 = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> val;
            if (i % 2 == 0)
            {
                sum1 += val;
            }
            else
            {
                sum2 += val;
            }
        }
        sum = sum1 + sum2;
        div1 = sum1 / n1;
        div2 = sum2 / n2;
        if (sum1 % n1 == 0 && sum2 % n2 == 0 && div1 == div2 && div1 >= 0)
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }
        cout << endl;
    }
}