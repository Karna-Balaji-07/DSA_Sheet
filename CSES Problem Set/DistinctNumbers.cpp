#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    cin >> n;
    unordered_set<int> distinct;

    for (int i = 0; i < n; ++i) {
        cin >> x;
        distinct.insert(x);
    }

    cout << distinct.size() << '\n';
    return 0;
}
