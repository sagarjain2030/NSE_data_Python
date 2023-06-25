import pickle
company_name_symbol_dict = {}

def create_company_name_symbol_dict():
    print("creating company_name_symbol_dict")
    with open("Resources/company_name_symbol_faceVal.csv","r") as f:
        for line in f.readlines():
            line = line.strip().split(sep=",")
            if line[2] == "EQ":
                symb = line[0].lower()
                name = line[1].lower().replace(" ","_").strip()
                name = name.replace("-","_").strip()
                name = name.replace("__","_").strip()
                face_value = int(line[3])
                company_name_symbol_dict[symb] = {"name":name,"face_value":face_value}
    
    with open('Out/company_name_symbol_dict.pickle', 'wb') as handle:
        pickle.dump(company_name_symbol_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(len(company_name_symbol_dict))

def main():
    create_company_name_symbol_dict()

if __name__ == "__main__":
    main()