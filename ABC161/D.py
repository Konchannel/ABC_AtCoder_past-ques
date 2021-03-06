"""
問題文
正の整数Xが以下の条件を満たすとき、Xはルンルン数であると言います。
Xを(leading zeroなしで)十進数表記した際に、隣り合うどの2つの桁の値についても、差の絶対値が 1以下
例えば、1234, 1, 334 などはルンルン数ですが、
31415, 119, 13579 などはルンルン数ではありません。

正の整数Kが与えられます。小さい方から K番目のルンルン数を求めてください。

制約
1≤K≤10^5
入力はすべて整数である。

===================
improvement:
3桁のルンルン数で、上2桁が12なら、3桁目は 1 or 2 or 3 。
小さいほうからルンルン数を列挙していくなら、そのルンルン数に末尾1桁、隣り合う数字を足してもルンルン数になる。
これを繰り返すことでルンルン数だけを列挙することができる。
言われてみればこの実装で動くのは理解できるが、
時間内にこれを思いつくことが出来なかった。悔しい。
特にdequeを使う動きは思いつかなかった、次回に活かしたい。
"""

# === improvement ===
from collections import deque

K = int(input())

q = deque(range(1, 10))

for i in range(K):
    x = q.popleft()
    r = x % 10
    y = 10 * x + r
    if r != 0:
        q.append(y - 1)
    q.append(y)
    if r != 9:
        q.append(y + 1)

print(x)
