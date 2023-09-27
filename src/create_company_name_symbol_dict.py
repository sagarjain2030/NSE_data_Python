import pickle
from TrieSearch import Trie
company_name_symbol_dict = {}
symb_trie = Trie()
new_name_modified_name_dict = {}


def create_company_name_symbol_dict():
    
    print("creating company_name_symbol_dict")
    with open("Resources/company_name_symbol_faceVal.csv","r") as f:
        for line in f.readlines():
            line = line.strip().split(sep=",")
            if line[2] == "EQ":
                symb = line[0].lower()
                ori_name = line[1]
                name = line[1].lower().replace(" ","_").strip()
                name = name.replace("-","_").strip()
                name = name.replace("__","_").strip()
                face_value = int(line[3])
                company_name_symbol_dict[symb] = {"name":name,"face_value":face_value}
                new_name_modified_name_dict[name] = ori_name
                symb_trie.insert(symb)
    
    with open('Out/company_name_symbol_dict.pickle', 'wb') as handle:
        pickle.dump(company_name_symbol_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    with open('Out/symb_trie.pickle','wb') as handle:
        pickle.dump(symb_trie,handle,protocol=pickle.HIGHEST_PROTOCOL)

    with open('Out/new_name_modified_name_dict.pickle','wb') as handle:
        pickle.dump(new_name_modified_name_dict,handle,protocol=pickle.HIGHEST_PROTOCOL)

    print(len(company_name_symbol_dict))

def main():
    create_company_name_symbol_dict()

if __name__ == "__main__":
    main()