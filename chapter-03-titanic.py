import numpy as np
import pandas as pd

# データの読み込み
df = pd.read_csv("datasets/titanic/train.csv")
df

# ------------------------------
# カテゴリデータの度数分布
# 客室の等級で度数をカウント
# ------------------------------
df["Pclass"].value_counts().sort_index()

# ------------------------------
# 数値データの度数分布
# 5歳刻みの階級で人数を集計(Pandasを利用)
# ------------------------------
df["Age"].dropna().value_counts(bins=np.arange(0, 100, 5), sort=False)


import seaborn as sns
from matplotlib import pyplot as plt

# フォント設定
plt.rcParams["font.family"] = "Hiragino Sans"

# 乗船者の年齢のヒストグラムを描画
age = df["Age"].dropna()
sns.histplot(age, bins=np.arange(0, 100, 5))
plt.title("年齢のヒストグラム")
plt.xlabel("年齢")
plt.ylabel("人数")
plt.show()
