import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Customer_Name': ['Amit', 'Riya', 'Karan', 'Neha', 'Amit', 'Pooja', 'Karan', 'Riya'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Headphones', 'Mobile', 'Laptop', 'Tablet'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Electronics'],
    'Quantity': [1, 2, 1, 1, 3, 1, 2, 2],
    'Price': [60000, 25000, 20000, 58000, 1500, 24000, 62000, 19000],
    'Order_Date': pd.to_datetime(['2025-01-05', '2025-01-07', '2025-02-12', '2025-02-15', '2025-03-01', '2025-03-05', '2025-03-07', '2025-03-10']),
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Delhi', 'Chennai', 'Bangalore', 'Mumbai']
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"]*df["Quantity"]
print(df.to_string())
colors = ["red", "blue", "green", "orange"]
Total_Sales_per_Product = df.groupby("Product")["Total_Sales"].sum()
Total_Sales_per_Product.plot(kind="bar", color=colors)
plt.title("Total Sales Per Product")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.ylabel("Sales")
#plt.legend()
plt.show()

Category_wise_Sales_Distribution = df.groupby("Category")["Total_Sales"].sum()
'''Category_wise_Sales_Distribution.plot(kind="pie", labels=Category_wise_Sales_Distribution.index)
plt.title("Category-wise Sales Distribution")
plt.show()'''

plt.figure(figsize=(6,6))
Category_wise_Sales_Distribution.plot(
    kind="pie",
    autopct='%1.1f%%',            # show percentage
    startangle=90,                # rotate for better alignment
    colors=['gold', 'skyblue'],   # consistent color scheme
    shadow=True                   # add slight 3D effect
)
plt.title("Category-wise Sales Distribution", fontsize=14, fontweight='bold')
plt.ylabel("")  # hide unnecessary 'Total_Sales' label
plt.show()


City_wise_Number_of_Orders= df.groupby("City")["Order_ID"].count()

City_wise_Number_of_Orders.plot(kind="bar", color=colors)
plt.title("City Wise Number of Orders")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.ylabel("Order")
plt.legend()
plt.show()


'''Quantity_vs_Price = df.groupby("Quantity")["Price"]
Quantity_vs_Price.plot(kind="scatter")'''
plt.scatter(df["Quantity"], df["Price"])
plt.title("Quantity vs Price Scatter Plot")
plt.grid(True)
plt.show()


product_price = df.groupby("Product")["Quantity"].sum()
product_price.plot(kind="line", marker="*", color="g")
plt.title("Product-wise Quantity Sales")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.legend()
plt.xticks(rotation=45)
plt.show()
