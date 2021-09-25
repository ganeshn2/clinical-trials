from pytrials.client import ClinicalTrials
import pandas as pd
import matplotlib.pyplot as plt

ct = ClinicalTrials()

# importing country to continent data
country_continent_df = pd.read_csv("clinical-trials/Input/country-and-continent-codes-list.csv")
country_continent_df = country_continent_df.drop(
        ["Three_Letter_Country_Code","Country_Number","Two_Letter_Country_Code"],axis = 1)

def impute_pipe(ctr):
    string_split = ctr.split("|")
    string_imputed = string_split[0]
    return string_imputed

# Generic function for search criteria:
# for example, the following search criteria will be performed:
# Skin Healing+Diabetes
# Skin+Hydrogel
# Wound Heal+Hydrogel
# wound+hydrogel
# skin+fibers
# wound heal+fibers
# skin heal+gels
# wound heal+gels
# skin healing+foams
# wound healing+foams

def search_criteria (search_string):
    study_list = ct.get_study_fields (
    search_expr = search_string,
    fields=["NCTId", "Condition", "BriefTitle", "InterventionType", "LocationCountry", "StartDate",
                "CompletionDate"],
    max_studies = 1000,
    fmt = 'csv')
    ct.get_study_count(search_expr = search_string)
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

def create_dataframe():
    shd = search_criteria("Skin Healing + Diabetes")
    sh = search_criteria("Skin + Hydrogel")
    whh = search_criteria("Wound Heal + Hydrogel")
    wh = search_criteria("wound + hydrogel")
    sf = search_criteria("skin + fibers")
    whf = search_criteria("wound heal + fibers")
    whg = search_criteria("wound heal + gels")
    shg = search_criteria("skin heal + gels")
    shf = search_criteria("skin healing + foams")
    whfs = search_criteria("wound healing + foams")
    frames = [shd,sh,whh,wh,sf,whf,whg,shg,shf,whfs]
    clinical_trials_data_df = pd.concat(frames)
    clinical_trials_data_df["Country_Name"] = clinical_trials_data_df["LocationCountry"].apply(lambda x: impute_pipe(x))
    clinical_trials_data_df["InterventionType"] = clinical_trials_data_df["InterventionType"].apply(lambda x: impute_pipe(x))
    clinical_trials_data_df.to_csv("./clinical-trials/Output/clinical_trials_data_df.csv")
    return clinical_trials_data_df


def merge_clean_dataframe (df1, df2):
    df1 = df1.drop(["LocationCountry", "Rank"], axis=1)
    df1.drop_duplicates(keep=False, inplace=True)
    merged_df = df1.merge(df2, how="inner", on="Country_Name")
    merged_df.to_csv("./clinical-trials/Output/merged_df.csv")
    return merged_df


def interventionDF(df3):
    intervention_df = df3[(df3["InterventionType"] == "Device") |
                          (df3["InterventionType"] == "Drug") | (df3["InterventionType"] == "Other") |
                          (df3["InterventionType"] == "Procedure") | (df3["InterventionType"] == "Biological")]
    intervention_df.to_csv("./clinical-trials/Output/intervention_df.csv")
    return intervention_df


# Code for matplotlib pie plots
colors_1 = ["#008fd5","#fc4f30","#e5ae37","#6d904f","#D02090","#308014"]
colors_2 = ["#008fd5","#fc4f30","#e5ae37","#6d904f","#D02090"]
labels_1 = ['North America',"Europe","Asia","South America","Africa","Oceania"]
labels_2 = ['Device',"Drug","Other","Procedure","Biological"]
explode_1 = [0.1, 0, 0, 0, 0.2, 0]
explode_2 = [0.1, 0, 0, 0, 0.1]


def pie_chart(slices,labels, colors, explode,title):
    plt.style.use("fivethirtyeight")
    plt.pie(slices, labels=labels, explode=explode,
            startangle=-15, autopct="%1.0f%%",
            colors=colors,
            wedgeprops={"edgecolor": "black"})
    plt.title(title, fontsize=18)
    plt.tight_layout()
    plt.savefig(title+".jpg")
    plt.show()


if __name__ == "__main__":
    main_df = create_dataframe()
    merged_df = merge_clean_dataframe(main_df,country_continent_df)
    piechart_plot2_df = interventionDF(merged_df)
    pie_chart(merged_df["Continent_Name"].value_counts(),labels_1,colors_1,explode_1,
              "Skin Regeneration Clinical Trials Across the World")
    pie_chart(piechart_plot2_df["InterventionType"].value_counts(), labels_2, colors_2, explode_2,
              "Type of Skin Regeneration Clinical Trials")