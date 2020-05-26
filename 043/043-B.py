"""
問題文
しぐはキーボードを製作しました。シンプルさを極限まで追求したこのキーボードには、0 キー、1 キー、バックスペースキーの
3つしかキーがありません。
手始めに、しぐはこのキーボードで簡単なテキストエディタを操作してみることにしました。このエディタには常に一つの文字列が表示されます
（文字列が空のこともあります）。エディタを起動した直後では、文字列は空です。キーボードの各キーを押すと、文字列が次のように変化します。

0 キー: 文字列の右端に文字 0 が挿入される。
1 キー: 文字列の右端に文字 1 が挿入される。
バックスペースキー: 文字列が空なら、何も起こらない。そうでなければ、文字列の右端の1文字が削除される。

しぐはエディタを起動し、これらのキーを何回か押しました。しぐが押したキーを順番に記録した文字列sが与えられます。
sの中の文字 0 は 0 キー、文字 1 は 1 キー、文字 B はバックスペースキーを表します。
いま、エディタの画面にはどのような文字列が表示されているでしょうか？

制約
1≦|s|≦10(|s|はsの長さを表す)
sは文字 0, 1, B のみからなる。
正解は空文字列ではない。
===================
tried-01:

improvement:
"""

# === tried-01 ===
s = input()
ans = ""

for i in s:
    if i == "B":
        ans = ans[:-1]
    else:
        ans += i

print(ans)

# === improvement ===