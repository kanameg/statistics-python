# -----------------------------------------------------------------
# Description: Pythonで学ぶあたらしい統計学 第7章
# グラフの活用

# 7-1. データ準備
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# データの読み込み
cov_df = pd.read_csv("./datasets/3-5-1-cov.csv")
cov_df

lineplot_df = pd.read_csv("./datasets/3-7-1-lineplot-data.csv")
lineplot_df

fish_multi_df = pd.read_csv("./datasets/3-6-1-fish_multi.csv")
fish_multi_df

penguins_df = sns.load_dataset("penguins")
penguins_df


# 7-4. 散布図
sns.scatterplot(data=cov_df, x="x", y="y", color="black")
plt.show()

# フォント設定
plt.rcParams["font.family"] = "Ricty"

# 7-5. 散布図の装飾
sns.scatterplot(data=cov_df, x="x", y="y", color="black")
plt.title("散布図", fontsize=20)
plt.xlabel("Xラベル", fontsize=15)
plt.ylabel("Yラベル", fontsize=15)
plt.grid(True)
plt.savefig("./output/7-5-scatterplot.png")
plt.show()


# 7-6. 折れ線グラフ
sns.lineplot(x="x", y="y", data=lineplot_df, color="black")
plt.grid(True)
plt.show()


# 7-7. 棒グラフ
sns.barplot(x="species", y="length", data=fish_multi_df, color="gray")
plt.show()

# 7-8. 箱ひげ図
sns.boxplot(x="species", y="length", data=fish_multi_df, color="gray")
plt.show()

# 7-9. バイオリンプロット
sns.violinplot(x="species", y="length", data=fish_multi_df, color="gray")
plt.show()


# 7-10. axis-levelとfigure-level
# figure-level
sns.relplot(kind="scatter", x="x", y="y", data=cov_df, color="black")
plt.grid(True)
plt.show()

# 7-11. 複数カテゴリのバイオリンプロット
fig, ax = plt.subplots(figsize=(8, 4))
# バイオリンプロット
sns.violinplot(
    x="species", y="body_mass_g", hue="sex", data=penguins_df, palette="gray", ax=ax
)
plt.title("ペンギンの種別体重分布", fontsize=16)
plt.xlabel("種別", fontsize=12)
plt.ylabel("体重(g)", fontsize=12)
plt.legend(title="性別")
plt.show()

# 7-12. 種別、島別、性別の体重分布
sns.catplot(
    kind="violin",
    x="species",
    y="body_mass_g",
    hue="sex",
    col="island",
    data=penguins_df,
    palette="gray",
    height=4,
    aspect=0.7,
)
plt.show()


# 7-13. ペアプロット
sns.pairplot(penguins_df, hue="species", palette="gray")
plt.show()
