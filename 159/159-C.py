"""
問題文
正の整数Lが与えられます。 縦、横、高さの長さ (それぞれ、整数でなくてもかまいません) の合計が
Lの直方体としてありうる体積の最大値を求めてください。

制約
1≤L≤1000
Lは整数
"""

# === tried-01 ===
L = int(input())
s = L / 3
print(s ** 3)