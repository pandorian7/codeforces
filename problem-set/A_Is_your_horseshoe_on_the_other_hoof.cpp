#include <iostream>
#include <unordered_set>

using namespace std;

int main()
{
    unordered_set<int> s;
    int tmp;
    for (int i = 0; i < 4; i++)
    {
        cin >> tmp;
        s.insert(tmp);
    }
    cout << 4 - s.size();
}