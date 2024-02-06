import pandas as pd
import json
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from datetime import datetime, timedelta

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

goods_df['Production Date'] = pd.to_datetime(goods_df['Production Date'])
production_month_bins = pd.date_range(start = goods_df['Production Date'].min(), end =  goods_df['Production Date'].max(), freq = 'M')
goods_df['ProductionMonth'] = pd.cut(goods_df['Production Date'], bins = production_month_bins, labels=range(1, len(production_month_bins)), include_lowest=True)

goods_df['StockCategory'], stock_bins = pd.qcut(goods_df["Quantity in Stock (liters/kg)"], q=4, labels=["Low","Medium","High"])

goods_df["RevenueCategory"] = pd.qcut(goods_df["Approx. Total Revenue(INR)"], q=4, labels=["Low","Medium","High","Premium"])

goods_df["ReorderCategory"] = pd.qcut(goods_df["Reorder Quantity (liters/kg)"], q=4, labels=["Low","Medium","High","Very High"])




stock_category_plot = goods_df['StockCategory'].value_counts().plot(kind = 'bar',
                                                                    xlabel="Stock Category",
                                                                    ylabel="Count",
                                                                    title ="Distribution of Stock Categories",
                                                                    figsize=(10,6))

goods_df.sort_values(goods_df['ProductionMonth'], ascending = True, inplace = True)

monthly_production_plot =goods_df['StockCategory'].value_counts().plot(kind = 'bar',
                                                                       xlabel="Stock Category",
                                                                       ylabel="Count",
                                                                       title ="Distribution of Stock Categories",
                                                                       figsize=(10,6))

monthly_production = goods_df.groupby("ProductionMonth")['Quantity (liters/kg)'].sum()
monthly_production_plot = monthly_production.plot(kind="line", marker="o",
                                                  xlabel = "Production Month",
                                                  ylabel = "Total Quality",
                                                  title='Monthly Production Trends',
                                                  figsize = [10,6])

median_quantity_sold = goods_df.groupby("ShelfLifeCategory")["Quantity Sold (liters/kg)"].median()
total_revenue = goods_df.groupby("PriceCategory")["Approx. Total Revenue(INR)"].sum()