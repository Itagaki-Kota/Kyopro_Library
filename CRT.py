#中国剰余定理 Chinese Remainder Theorem  (https://qiita.com/R_olldIce/items/3e2c80baa6d5e6f3abe9)(https://yukicoder.me/problems/no/2117)

"""
A ≡ X1 (mod Y1)
A ≡ X2 (mod Y2)

(Y1とY2は自然数で, 互いに素)
上の連立合同式が成り立つ非負整数Aは, Y1 * Y2未満にただ一つ存在する

"""


"""
連立合同式 (Yiは自然数)
A ≡ X1 (mod Y1)
A ≡ X2 (mod Y2)
.
.
.
A ≡ Xi (mod Yi)
.
.
.

を解いて, A ≡ r (mod d) の rとdを返す。
解が存在しないなら, r, m = [0, 0] が返る。

"""

def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    # 初期状態
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        # 遷移の準備
        u = s // t

        # 遷移
        s -= t * u
        m0 -= m1 * u

        # swap
        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0: m0 += b // s
    return s, m0


def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0, m0 = 0, 1  # 初期値 x = 0 (mod 1)
    for i in range(n):
        assert m[i] >= 1

        #r1, m1は遷移に使う値
        r1, m1 = r[i] % m[i], m[i]

        #m0がm１以上になるようにする。
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0

        # m0がm1の倍数のとき gcdはm1、lcmはm0
        # 解が存在すれば何も変わらないので以降の手順はスキップ
        if m0 % m1 == 0:
            if r0 % m1 != r1: return [0, 0]
            continue

        #  拡張ユークリッドの互除法によりgcd(m0, m1)と m0 * im = gcd (mod m1) を満たす imを求める
        g, im = inv_gcd(m0, m1)

        # 解の存在条件の確認
        if (r1 - r0) % g: return [0, 0]


        u1 = m0 * m1 // g
        r0 += (r1 - r0) // g * m0 * im % u1
        m0 = u1


    return [r0, m0]



"""
A ≡ 3 (mod 5)
A ≡ 4 (mod 7)
ならば, 
X = [3, 4]
Y = [5, 7]
print(crt(X, Y))  # [18, 35]

解は A ≡ 18 (mod 35)

"""


"""
(yukicoder367)

B0, C0 = map(int, input().split())
B1, C1 = map(int, input().split())


X = [C0, C1]  # X = [X1, X2 ・・・]
Y = [B0, B1]  # Y = [Y1, Y2 ・・・]
r, m = crt(X, Y)
if r == 0 and m == 0:
    print("NaN")
else:
    print(r)
"""






"""
paiza(https://paiza.jp/works/mondai/prime_number_primer/prime_number_primer__chinese_remainder_theorem/edit?language_uid=python3&t=9717fea4c1ed635adfd62cc9efc1da4b)
paizaの中国剰余定理(工夫した全探索)

Z ÷ m1 = ◇ ... b1   ①
Z ÷ m2 = ■ ... b2   ②

(m1, m2 > 0)
(Zは m1 * m2 未満。Zを求めよ)

TLEするので, ◇でループを回す。
◇を決め打つと, ①式より, Zが一時的に決まり,Z % m2 == b2 ならok!
◇のループの上限が問題なのだが,
Z = m1*◇ + b1
Z < m1 * m2より, m1 * ◇ + b1 < m1 * m2
m1 * ◇ + b1 - m1 * m2 < 0
m1(◇ - m2) < -b1
m1 > 0より, 
◇ - m2 < -b1/m1
◇ < -b1/m1 + m2
余りの関係より, b1 < m1なので,
◇ < m2


m1, m2, b1, b2 = map(int, input().split())

for q in range(m2 + 5):
    Z = m1 * q + b1
    if Z % m2 == b2:
        print(Z)
        exit()
"""
