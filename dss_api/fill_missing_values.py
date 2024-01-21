import pandas as pd

df = pd.read_csv('https://ali.dasmeh.ir/bank-direct-marketing-campaigns.csv')

def create_combined_condition(conditions_arr):
  combined_condition = conditions_arr[0] & conditions_arr[1]
  for condition in conditions_arr[2:] :
    combined_condition = combined_condition & condition

  return combined_condition

def search_for_the_most_similar_row(current_row, key_with_none_value):
  conditions = []
  for key, value in current_row.items():
    if value is not None:
      conditions.append((df[key] == value))
    else:
      conditions.append((df[key].notna()))

  combined_condition = create_combined_condition(conditions)
  similar_rows = df[combined_condition]
  conditions.pop()

  while similar_rows.shape[0]== 0 and len(conditions) > 3:
    combined_condition = create_combined_condition(conditions)
    similar_rows = df[combined_condition]
    conditions.pop()


  if similar_rows.shape[0] == 0:
    return False

  else:
    return similar_rows.iloc[0, :][key_with_none_value]
  
def fill_missing_values(df):
    for index, row in df[df.isna().any(axis=1)].iterrows():
        for key, value in row.items():
            # if key == "housing" and value is None:
            if value is None:
                new_value = search_for_the_most_similar_row(row, key)
                if new_value == False:
                    return {"status": False, "dataframe": df}
                else:
                    df.at[index, key] = new_value

    return {"status": True, "dataframe": df}