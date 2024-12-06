#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t, n, m, words, accepting;
    string s;
    cin >> t;
    while (t--)
    {
        words = 0;
        cin >> n >> m;
        accepting = 1;
        while (n--)
        {
            cin >> s;
            if (s.length() <= m)
            {
                if (accepting)
                {
                    words++;
                    m -= s.length();
                }
            }
            else
            {
                accepting = 0;
            }
        }
        cout << words << endl;
    }
}