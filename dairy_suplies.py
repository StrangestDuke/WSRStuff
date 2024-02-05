import pandas as pd
import json
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

goods_df = pd.read_csv("files to parse/dairy_dataset.csv")
inf = float("inf")

goods_df["LandAreaCategory"] = pd.cut(goods_df["Total Land Area (acres)"], bins=[0,50,100,200, inf], labels=["Small", "Medium", "Large", "Extra Large"])

goods_df["PriceCategory"] = pd.cut(goods_df["Price per Unit"], bins = [0, 10, 20, 30, inf], labels = ["Low", "Medium", "High", "Premium"])

df_col = pd.read_csv("files to parse/dairy_dataset.csv").columns

brand_dummies = pd.get_dummies(goods_df['Brand'], prefix='Brand')

goods_df["ShelfLifeCategory"] = pd.cut(goods_df["Shelf Life (days)"], bins=[0,7,14,30, inf], labels=["Short", "Medium", "Long", "Very Long"])

print(goods_df["Sales Channel"])
storage_dummies = pd.get_dummies(goods_df['Storage Condition'], prefix='Storage')
channel_dummies = pd.get_dummies(goods_df['Sales Channel'], prefix='Channel',prefix_sep=':')
