import pickle
company_name_symbol_dict = {}

with open("company_name_symbol_faceVal.csv","r") as f:
    for line in f.readlines():
        line = line.strip().split(sep=",")
        if line[2] == "EQ":
            symb = line[0].lower()
            name = line[1].lower().replace(" ","_").strip()
            face_value = int(line[3])
            company_name_symbol_dict[symb] = {"name":name,"face_value":face_value}

with open('company_name_symbol_dict.pickle', 'wb') as handle:
    pickle.dump(company_name_symbol_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(len(company_name_symbol_dict),"companies in company_name_symbol_dict.pickle (created)")

print(company_name_symbol_dict["infy"])

print(company_name_symbol_dict["wockpharma"])

print(company_name_symbol_dict["chamblfert"])

print(company_name_symbol_dict["dalbharat"])
