import matplotlib.pyplot as plt
import pandas as pd

merged_df = pd.read_csv("~/playground/clinical-trials/Output/merged_df.csv")
print(merged_df["Continent_Name"].value_counts())

plt.style.use("fivethirtyeight")
slices = merged_df["Continent_Name"].value_counts()
labels = ['North America',"Europe","Asia","South America","Africa","Oceania"]
colors = ["#008fd5","#fc4f30","#e5ae37","#6d904f","#D02090","#308014"]
explode = [0.1, 0, 0, 0, 0.2, 0]

plt.pie(slices, labels = labels,explode = explode,
        startangle = -15,autopct = "%1.0f%%",
        colors = colors,
        wedgeprops = {"edgecolor":"black"})
plt.title("Clinical Trials on Skin Regeneration Across the World",fontsize = 15)
plt.legend(labels = labels, bbox_to_anchor=(1,0), loc="lower right",
                          bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.savefig("Pie Chart without Shadow.jpg")
plt.show()


