from pytrials.client import ClinicalTrials
import pandas as pd

ct = ClinicalTrials()

# importing country to continent data
country_continent = pd.read_csv("clinical-trials/Input/country-and-continent-codes-list.csv")

def impute_pipe(ctr):
    string_split = ctr.split("|")
    string_imputed = string_split[0]
    return string_imputed

fields = ["NCTId", "Condition", "BriefTitle","InterventionType","LocationCountry","StartDate","CompletionDate"]
max_studies = 1000
fmt = "csv"

# Search criteria - Skin Healing AND Diabetes

def skhealing_diabetes ():
    study_list = ct.get_study_fields (
    search_expr = "Skin Healing+Diabetes",
    fields = fields,
    max_studies = max_studies,
    fmt = fmt )
    ct.get_study_count(search_expr="Skin Healing+Diabetes")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - Skin AND Hydrogel

def skin_hydrogel():
    study_list = ct.get_study_fields(
        search_expr="Skin+Hydrogel",
        fields=fields,
        max_studies=max_studies,
        fmt=fmt)
    ct.get_study_count(search_expr="Skin+Hydrogel")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - wound heal AND hydrogel

def wound_heal_hydrogel():
    study_list = ct.get_study_fields(
    search_expr="Wound Heal+Hydrogel",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="Wound Heal+Hydrogel")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - wound AND hydrogel

def wound_hydrogel():
    study_list = ct.get_study_fields(
    search_expr="wound+hydrogel",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="wound+hydrogel")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - skin AND fibers

def skin_fibers():
    study_list = ct.get_study_fields(
    search_expr="skin+fibers",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="skin+fibers")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - wound heal AND fibers

def wound_heal_fibers():
    study_list = ct.get_study_fields(
    search_expr="wound heal+fibers",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="wound heal+fibers")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - skin healing AND gels
def skin_heal_gels():
    study_list = ct.get_study_fields(
    search_expr="skin heal+gels",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="skin heal+gels")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - skin healing AND gels
def wound_heal_gels():
    study_list = ct.get_study_fields(
    search_expr="wound heal+gels",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="wound heal+gels")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - skin healing AND gels
def skin_foams():
    study_list = ct.get_study_fields(
    search_expr="skin healing+foams",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="skin healing+foams")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

# Search criteria - wound healing AND gels
def wound_foams():
    study_list = ct.get_study_fields(
    search_expr="wound healing+foams",
    fields=fields,
    max_studies=max_studies,
    fmt=fmt)
    ct.get_study_count(search_expr="wound healing+foams")
    return pd.DataFrame.from_records(study_list[1:], columns=study_list[0])

if __name__ == "__main__":
    frames = [skhealing_diabetes(),skin_hydrogel(),wound_heal_hydrogel(),wound_hydrogel(),skin_fibers(),
                          wound_heal_fibers(),skin_heal_gels(),wound_heal_gels(),skin_foams(),wound_foams()]

    clinical_trials_data_df = pd.concat(frames)
    clinical_trials_data_df["Country_Name"] = clinical_trials_data_df["LocationCountry"].apply(lambda x : impute_pipe(x))
    clinical_trials_data_df["InterventionType"] = clinical_trials_data_df["InterventionType"].apply(lambda x : impute_pipe(x))
    clinical_trials_data_df = clinical_trials_data_df.drop(["LocationCountry","Rank"],axis=1)
    clinical_trials_data_df.drop_duplicates(keep=False, inplace=True)

    merged_df = clinical_trials_data_df.merge(country_continent, how="inner", on="Country_Name").drop(
        ["Three_Letter_Country_Code","Country_Number","Two_Letter_Country_Code"], axis = 1)

    merged_df.to_csv("~/playground/clinical-trials/Output/merged_df.csv")
    print(merged_df["InterventionType"].value_counts())
    print('success')