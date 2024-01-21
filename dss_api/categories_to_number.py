def categories_to_number(df):
  modified_df = df.copy(deep=True)

  mapping_dict_for_week_days = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5}
  modified_df["day_of_week"] = modified_df["day_of_week"].map(mapping_dict_for_week_days)

  mapping_dict_month_to_number = { "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12 }
  modified_df["month"] = modified_df["month"].map(mapping_dict_month_to_number)

  mapping_dict_contact = { "cellular": 1, "telephone": 2 }
  modified_df["contact"] = modified_df["contact"].map(mapping_dict_contact)

  mapping_dict_loan = { "yes": True, "no": False }
  modified_df["loan"] = modified_df["loan"].map(mapping_dict_loan)

  mapping_dict_housing = { "yes": True, "no": False }
  modified_df["housing"] = modified_df["housing"].map(mapping_dict_housing)

  mapping_dict_education = { "basic.4y": 1, "basic.6y": 2, "basic.9y": 3, "high.school": 4, "illiterate": 5, "professional.course": 6, "university.degree": 7 }
  modified_df["education"] = modified_df["education"].map(mapping_dict_education)

  mapping_dict_marital = { "married": 1, "single": 2, "divorced": 3 }
  modified_df["marital"] = modified_df["marital"].map(mapping_dict_marital)

  mapping_dict_job = { "admin.": 1, "blue-collar": 2, "entrepreneur": 3 , "housemaid": 4 , "management": 5 , "retired": 6 , "self-employed": 7, "services": 8 , "student": 9 , "technician": 10, "unemployed": 11 }
  modified_df["job"] = modified_df["job"].map(mapping_dict_job)

  mapping_dict_default = { "no": False, "yes": True }
  modified_df["default"] = modified_df["default"].map(mapping_dict_default)

  del modified_df['poutcome']
  del modified_df['pdays']

  return modified_df
