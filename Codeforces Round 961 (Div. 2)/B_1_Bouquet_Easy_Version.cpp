#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main()
{
    int t, n, m, val, cart, max_cost, budget;
    int now, next;
    vector<int> petles;
    unordered_map<int, int> counts;
    cin >> t;
    while (t--)
    {
        cin >> n >> m;
        counts.clear();
        petles.clear();
        for (int i = n; i--;)
        {
            cin >> val;
            if (!counts[val])
                petles.push_back(val);
            counts[val]++;
        }
        sort(petles.begin(), petles.end());
        max_cost = 0;
        for (size_t i = 0; i < petles.size() - 1; i++)
        {
            budget = m;
            cart = 0;
            now = petles[i];
            next = petles[i + 1];

            for (int j = 0; j < counts[next]; j++)
            {
                if (budget >= next)
                {
                    cart += next;
                    budget -= next;
                }
            }
            if (now == next - 1)
            {
                for (int j = 0; j < counts[now]; j++)
                {
                    if (budget >= now)
                    {
                        cart += now;
                        budget -= now;
                    }
                }
            }

            if (cart > max_cost)
                max_cost = cart;
        }
        cout << max_cost << endl;
    }
}