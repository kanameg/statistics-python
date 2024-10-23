# -----------------------------------------------------------------
# Description: Pythonで学ぶあたらしい統計学 第5章
# 多変量データの統計量

# -----------------------------------------------------------------
# ライブラリのインポートとデータの読み込み
# -----------------------------------------------------------------
import numpy as np
import pandas as pd
from scipy import stats

# データの読み込み
cov_df = pd.read_csv("./datasets/3-5-1-cov.csv")
cov_df


# 5-3. 共分散
# Covariance
# Cov(X, Y) = 1/n Σ (Xi - X_mean) * (Yi - Y_mean)
# 共分散は、2つの変数の関係性を示す統計量

# 5-4. 分散共分散行列
# Covariance Matrix
# Σ = [[Var(X), Cov(X, Y)],
#       [Cov(X, Y), Var(Y)]]

# 5-5. 共分散
# 定義から計算
x = cov_df["x"]
y = cov_df["y"]
n = len(cov_df)
mean_x = np.mean(x)
mean_y = np.mean(y)
cov = sum((x - mean_x) * (y - mean_y)) / n
cov

# 5-6. 分散共分散行列
x_var = np.var(x)
y_var = np.var(y)
print("xの標本分散: ", x_var)
print("yの標本分散: ", y_var)

# numpyのcov関数で分散共分散行列を計算
np.cov(x, y, ddof=0)

# 5-7. ピアソンの積率相関係数
# Pearson Correlation Coefficient
# r = Cov(X, Y) / √(Var(X) * Var(Y))
# -1 <= r <= 1
# 共分散をそれぞれの標準偏差で割り、正規化したもの

# 5-8. 相関行列
# Correlation Matrix
# 複数の変数での相関係数を行列の形式で表現したもの
# 2変数の場合は、以下のようになる
# R = [[1, r],
#      [r, 1]]
# 3変数の場合は、以下のようになる
# R = [[1, r12, r13],
#      [r21, 1, r23],
#      [r31, r32, 1]]
# r11, r22, r33 は1になる
# r12 = r21, r13 = r31, r23 = r32

# 5-9. ピアソンの積率相関係数
# 定義から計算
rho = cov / np.sqrt(x_var * y_var)
rho

# numpyのnp.corrcoef関数で相関行列を計算
np.corrcoef(x, y)


# -----------------------------------------------------------------
# クロス集計表
# -----------------------------------------------------------------
# 5-11. クロス集計表
# Cross Tabulation
# 量的データの関係性を表す場合は、相関係数を使用するが、
# 質的データの関係性を表す場合は、クロス集計表を使用する。

# 5-12. クロス集計表
disease_df = pd.read_csv("./datasets/3-5-2-cross.csv")
disease_df

# クロス集計表
disease_cross = pd.crosstab(disease_df["sunlight"], disease_df["disease"])
disease_cross

shoes_df = pd.read_csv("./datasets/3-5-3-cross2.csv")
shoes_df

# クロス集計表
shoes_cross = pd.pivot_table(
    data=shoes_df, values="sales", aggfunc="sum", index="store", columns="color"
)
shoes_cross

# -----------------------------------------------------------------
