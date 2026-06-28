import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\THINK PAD\Downloads\archive (3)\netflix_titles.csv")
print(df.columns)
top_ratings = df["rating"].value_counts().head(8)
plt.figure(figsize=(10,6))
bars = plt.bar(top_ratings.index,top_ratings.values,color="#4C72B0")
for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+10,str(int(bar.get_height())),ha="center",fontsize=10,fontweight="bold")
plt.title("Netflix Content by Rating" ,fontsize=15,fontweight="bold")
plt.xlabel("Rating",fontsize=12)
plt.ylabel("Number of Titles",fontsize=12)
plt.tight_layout()
plt.savefig("ratings.png",dpi=150)
plt.show()