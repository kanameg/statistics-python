# -----------------------------------------------------------------
# Description: Pythonで学ぶあたらしい統計学 第4章
# 1変量データの統計量

# -----------------------------------------------------------------
# ライブラリのインポートとデータの読み込み
# -----------------------------------------------------------------
import stat

import numpy as np
import pandas as pd
from scipy import stats

# データの読み込み
fish_length_df = pd.read_csv("./datasets/3-4-1-fish-length.csv")
fish_length_df

# データフレームとarrayの変換
fish_length = fish_length_df["length"].to_numpy()
fish_length

# 4-3. サンプルサイズ
len(fish_length_df)

# 4-4. 合計値
print(fish_length_df["length"].sum())
print(fish_length.sum())

# 4-5. 標本平均
print(fish_length_df["length"].mean())
print(fish_length.mean())

# 4-7. 標本分散
print(fish_length_df["length"].var(ddof=0))
print(fish_length.var())  # numpyのデフォルトは標本分散

# 4-9. 不偏分散
print(fish_length_df["length"].var())  # pandasのデフォルトは不偏分散
print(fish_length.var(ddof=1))

# 4-11. 標準偏差 (標本標準偏差)
print(round(fish_length_df["length"].std(ddof=0), 3))
print(round(fish_length.std(ddof=0), 3))

# 4-13. 変動係数
# Coefficient of Variation (CV) = （標本）標準偏差 / 平均値
# 標準偏差を平均値で割ることにより、ばらつきの大きさを正規化し、比較を可能にします。
# ※ 平均値が0の場は、CVは計算できません。比を計算しているので比例尺度のデータにのみ適用できます。
cv = fish_length_df["length"].std(ddof=0) / fish_length_df["length"].mean()
print(round(cv, 3))

# 4-15. 標準化
# Z-score = (X - 平均値) / 標準偏差
# 統計量ではない、データの平均を0、標準偏差を1にする操作

# z = (fish_length_df["length"] - fish_length_df["length"].mean()) / fish_length_df[
#     "length"
# ].std(ddof=0)
# print(z.head())

z = stats.zscore(fish_length_df["length"])
print(round(z, 3))

# 4-17. 最小値・最大値
print(fish_length_df["length"].min())
print(fish_length.min())

print(fish_length_df["length"].max())
print(fish_length.max())

# 4-18. 中央値
print(fish_length_df["length"].median())
print(np.median(fish_length))

# 4-19. 四分位数
# 第一四分位数（Q1）：データの下から25%の位置にある値
print(fish_length_df["length"].quantile(q=0.25))
print(np.quantile(fish_length, 0.25))
print(np.percentile(fish_length, 25))

# 第三四分位数（Q3）：データの下から75%の位置にある値
print(fish_length_df["length"].quantile(q=0.75))
print(np.quantile(fish_length, 0.75))
print(np.percentile(fish_length, 75))

# 4-20. 最頻値
print(fish_length_df["length"].mode())
print(stats.mode(fish_length))

# 4-21. describeメソッド
print(fish_length_df["length"].describe())
print(stats.describe(fish_length))

# -----------------------------------------------------------------
