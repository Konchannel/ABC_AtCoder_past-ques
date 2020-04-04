"""
問題文
長さが奇数である文字列Sが以下の条件をすべて満たすとき、Sは「強い回文」であるといいます。
Sは回文である。
NをSの長さとするとき、Sの1文字目から(N−1)/2文字目まで(両端含む)からなる文字列は回文である。
Sの (N+3)/2文字目から N文字目まで(両端含む)からなる文字列は回文である。
Sが強い回文かどうかを判定してください。

制約
Sは英小文字のみからなる
Sの長さは3以上99以下の奇数

===================
improvement:
reverseを別変数にとらず、if文をワンライナーで書いた。
(n-1)//2など、頻出する計算は、変数に取ったほうがわかりやすいかも。この場合のdivのように、数式が読みやすくなる。
"""

# === tried-01 ===
s = input()
n = len(s)
s1 = s[0:(n-1)//2]
s1r = s[(n-1)//2-1::-1]
s2 = s[(n+3)//2 - 1:]
s2r = s[:(n+3)//2 - 2:-1]

if s == s[::-1] and s1 == s1r and s2 == s2r:
    print("Yes")
else:
    print("No")


# === improvement ===
div = len(s)//2
pre = s[:div]
post = s[div+1:]
print('Yes' if pre == pre[::-1] and post == post[::-1] else 'No')