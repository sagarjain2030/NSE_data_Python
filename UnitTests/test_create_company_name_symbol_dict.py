import pickle

def test_create_company_name_symbol_dict():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b)

def test_company_name_symbol_dict_len():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(len(b) == 1769)

def test_company_name_symbol_dict_infy():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["infy"]["name"] == "infosys_limited")
    assert(b["infy"]["face_value"] == 5)

def test_company_name_symbol_dict_wockpharma():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["wockpharma"]["name"] == "wockhardt_limited")
    assert(b["wockpharma"]["face_value"] == 5)

def test_company_name_symbol_dict_chamblfert():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["chamblfert"]["name"] == "chambal_fertilizers_&_chemicals_limited")
    assert(b["chamblfert"]["face_value"] == 10)

def test_company_name_symbol_dict_dalbharat():
    with open('company_name_symbol_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["dalbharat"]["name"] == "dalmia_bharat_limited")
    assert(b["dalbharat"]["face_value"] == 2)