# Description: Pythonで学ぶあたらしい統計学 第3章

# -----------------------------------------------------------------
# ライブラリのインポート
# -----------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pyparsing import line

# フォント設定
plt.rcParams["font.family"] = "HackGen"

# データの読み込み
fish_speceise_df = pd.read_csv("./datasets/3-3-1-fish-species.csv")
fish_speceise_df


# -----------------------------------------------------------------
# 質的変数（カテゴリデータ）の度数分布表を作成
fish_speceise_df["species"].value_counts(sort=False)

# 度数分布表を可視化
sns.countplot(data=fish_speceise_df, x="species")
plt.show()

# 量的変数（数値データ）の度数分布表を作成
fish_length_df = pd.read_csv("./datasets/3-3-2-fish-length.csv")
fish_length_df

# 階級を3つに指定して度数分布表を作成
fish_length_df["length"].value_counts(bins=3, sort=False)

# 階級の最大値と最小値を指定して度数分布表を作成
freq = fish_length_df["length"].value_counts(bins=np.arange(0, 6, 1), sort=False)
freq

# 相対度数分布表 (度数 / 全データ数)
rel_freq = freq / freq.sum()
rel_freq

# 相対度数分布表
fish_length_df["length"].value_counts(
    bins=np.arange(0, 6, 1), sort=False, normalize=True
)

# 累積度数分布表 cumsum()を使用する
freq.cumsum()

# 累積相対度数分布表
rel_freq.cumsum()

# -----------------------------------------------------------------
# ヒストグラム
# -----------------------------------------------------------------
sns.histplot(data=fish_length_df, x="length", bins=np.arange(0, 6, 1))
plt.show()

# 相対度数を使用したヒストグラム
# stat="density"を指定すると、相対度数を使用したヒストグラムが描画される
sns.histplot(data=fish_length_df, x="length", bins=np.arange(0, 6, 1), stat="density")
plt.show()

# 階級の幅が異なるヒストグラム
sns.histplot(data=fish_length_df, x="length", bins=[0, 1, 2, 5], stat="density")
plt.show()

# -----------------------------------------------------------------
# カーネル密度推定
# -----------------------------------------------------------------
sns.kdeplot(data=fish_length_df, x="length", fill=True)
plt.show()

# バンド幅を変更
sns.kdeplot(data=fish_length_df, x="length", color="black", label="default")
sns.kdeplot(
    data=fish_length_df,
    x="length",
    bw_adjust=0.4,
    color="black",
    linestyle="dashed",
    label="bw_adjust=0.4",
)
sns.kdeplot(
    data=fish_length_df,
    x="length",
    bw_adjust=2,
    color="black",
    linestyle="dotted",
    label="bw_adjust=2",
)
plt.legend()
plt.show()

# -----------------------------------------------------------------
