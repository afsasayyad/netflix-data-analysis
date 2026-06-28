import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\THINK PAD\Downloads\archive (3)\netflix_titles.csv")
top = df["country"].dropna().str.split(",").explode().str.strip().value_counts().head(10)
plt.figure(figsize=(10,6))
bars = plt.bar(top.index,top.values,color=["#4C72B0","#DD5143","#2CA02C","#FF7F0E","#9467BD","#8C564B","#E377C2","#7F7F7F","#BCBD22","#17BECF"])
for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2,bar.get_height()+20,str(int(bar.get_height())),ha="center",fontsize=9,fontweight="bold")
plt.title("Top 10 Countries on Netflix",fontsize=12,fontweight="bold")
plt.xlabel("Country",fontsize=12)
plt.ylabel("Number of titles",fontsize=12)
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top",dpi=300)
plt.show()