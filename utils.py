import pandas as pd
from pandas import Series
import pickle

def read_data():
    data = pd.read_csv("data/companylist.csv")
    useful_data = data[["Symbol", "Name", "Sector", "Industry"]]
    return useful_data


def create_sets(data,fieldname):
    domain_unique = data[fieldname].unique()
    #industries = data["Industry"].unique()
    # print(industry)

    domain_dict ={}
    #industry_set = {}
    for individual_domain in domain_unique:
        domain_dict[individual_domain] = set()

        series = data[data[fieldname] == individual_domain]["Symbol"]
        for i, sec in series.items():
            domain_dict[individual_domain].add(sec.strip())

    return domain_dict

def ticker_to_name(ticker_set,data):
    name_list=[]
    for ticker in ticker_set:
        for name in data[data["Symbol"]==ticker]["Name"]:
            name_list.append(name+"("+ticker+")")
            print(name_list)
            #print(name+"("+ticker+")")
    return name_list

def ticker_to_name_dict(data):
    #ticker2name={ticker,name for i,ticker in data["Symbol"] for j,name in }
    return Series(data.Name.values,index=data.Symbol.str.strip().values).to_dict()


def get_intersection(set_list):
    return set.intersection(*set_list)

def get_union(set_list):
    return set.union(*set_list)




"""""
for industry in industries:
    industry_set[industry] = set()

    series = data1[data1["Industry"] == industry]["Symbol"]
    for j, sec in series.items():
        industry_set[industry].add(sec.strip())

print(industry_set)
"""""
data=read_data()
sector_dict=create_sets(data,"Sector")
industry_dict=create_sets(data,"Industry")
#ticker_to_name(industry_set["Books"],data)
ticker2name_dict=(ticker_to_name_dict(data))
pickle.dump([sector_dict,industry_dict,ticker2name_dict],open("conclusions/info.p","wb"))
#print(ticker2name_dict)