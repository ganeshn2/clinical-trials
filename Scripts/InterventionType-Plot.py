import matplotlib.pyplot as plt
import pandas as pd

merged_df = pd.read_csv("~/playground/clinical-trials/Output/merged_df.csv")
split_df = merged_df[(merged_df["InterventionType"] == "Device") |
     (merged_df["InterventionType"] == "Drug") |
      (merged_df["InterventionType"] == "Other") |
      (merged_df["InterventionType"] == "Procedure") |
      (merged_df["InterventionType"] == "Biological")]


plt.style.use("fivethirtyeight")
slices = split_df[["InterventionType"]].value_counts()
labels = ['Device',"Drug","Other","Procedure","Biological"]
colors = ["#008fd5","#fc4f30","#e5ae37","#6d904f","#D02090"]
explode = [0.1, 0, 0, 0, 0.1]

plt.pie(slices, labels = labels,explode = explode,shadow = True,
        startangle = -15,autopct = "%1.0f%%",
        colors = colors,
        wedgeprops = {"edgecolor":"black"})
plt.title("Clinical Trials on Skin Regeneration Based on Intervention Types",fontsize = 10)
plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right",
                          bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()
plt.savefig("Pie Chart2 with shadow.png")


