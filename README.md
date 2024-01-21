# Intro
this project was developed as an assignment for a DSS course. 
The dataset is from Kaggle :
https://www.kaggle.com/datasets/ruthgn/bank-marketing-data-set

## Note
- The AI model is trained by SKlearn Library. The model trained and tested on Google Colab (the ipynb file is coming from Colab). 
- The dss_api folder is a flask project. this project has only one endpoint ([POST] /api). this endpoint got 19 features of a potential audience of marketing campain (the request can come from a auatomatic system or a human agent) like object below:
```
{
    "age": null,
    "job": null,
    "marital": null,
    "education": "professional.course",
    "default": "no",
    "housing": "no",
    "loan": "no",
    "contact": "cellular",
    "month": "nov",
    "day_of_week": "fri",
    "campaign": 1,
    "pdays": 999,
    "previous": 0,
    "poutcome": "nonexistent",
    "emp.var.rate": -1.1,
    "cons.price.idx": 94.76700000000001,
    "cons.conf.idx": -50.8,
    "euribor3m": 1.028,
    "nr.employed": 4963.6
}
```
*Notice :* as it can be seen, there are some null value in the current object which is OK. the fill_missing_values.py module is going to fill the missing values by the most similar rows' data. 
- the agent call folder includes a html page which is design to be used by Human Agents.