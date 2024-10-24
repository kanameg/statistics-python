# -----------------------------------------------------------------
# Description: Pythonで学ぶあたらしい統計学 第6章
# 層別分析

# 6-2. 整然データ
# Tidy Data
# 整然データは、データ分析に適した形式に整形されたデータ
# 整然データの特徴
# 1. 個々の変数が1つの列になる
# 2. 個々の観測が1つの行になる
# 3. 個々の観測の構成単位の累計が1つのテーブルになる
# 4. 個々の値が1つのセルになる


# -----------------------------------------------------------------
# ライブラリのインポートとデータの読み込み
# -----------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats

# データの読み込み
fish_multi_df = pd.read_csv("./datasets/3-6-1-fish_multi.csv")
fish_multi_df

len(fish_multi_df)
fish_multi_df["species"].value_counts()
fish_multi_df["length"].mean()

# 6-7. グループ別の統計量の計算
# 平均値
# fish_multi_df.query('species == "A"')["length"].mean()
grouped = fish_multi_df.groupby("species")
grouped.mean()

# 要約統計量
grouped.describe()

# 6-8. ペンギンデータの読み込み
penguins_df = sns.load_dataset("penguins")
penguins_df

# ペンギンの種類の度数
penguins_df["species"].value_counts()

# Torgersen島のペンギンの種類の度数
penguins_df.query('island == "Torgersen"')["species"].value_counts()
# Adelieしかいない

# 6-9. ペンギンデータの層別分析
grouped_penguins = penguins_df.groupby(["species", "sex"])
print(grouped_penguins.mean()["body_mass_g"])


# 6-10. 欠損値の扱い
penguins_df[["species", "body_mass_g"]].head(10)

grouped_sp = penguins_df.groupby("species")
grouped_sp.count()["body_mass_g"]
# Adelieは152データがあるのに、151となっている、欠損値があるデータが削除されている

# ------------------------------------------------------------
# ヒストグラム
# ------------------------------------------------------------

# 6-12. 魚の種類ごとのヒストグラム
bins = np.arange(2, 11, 1)
bins
sns.histplot(x="length", hue="species", data=fish_multi_df, bins=bins, palette="gray")
plt.show()
