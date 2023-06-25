import pickle

company_details_dict = {}

name_industry_dict = {}
with open('Out/name_industry_dict.pickle', 'rb') as handle:
        name_industry_dict = pickle.load(handle)

domain_industry_dict = {}
with open('Out/domain_industry_dict.pickle', 'rb') as handle:
        domain_industry_dict = pickle.load(handle)

company_name_symbol_dict = {}
with open('Out/company_name_symbol_dict.pickle', 'rb') as handle:
        company_name_symbol_dict = pickle.load(handle)

temp = set()
for key,value in company_name_symbol_dict.items():
        temp.add(value["name"])

print(len(temp))
print(temp)

print(len(name_industry_dict))
print(len(domain_industry_dict))
print(len(company_name_symbol_dict))