import pickle

import sys
sys.path.append('src')


def test_create_name_industry_dict():
    with open('Out/name_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b)

def test_name_industry_dict_len():
    with open('Out/name_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(len(b) == 1936)

def test_name_industry_dict_aviation():
    with open('Out/name_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b['mazagon_dock'] == "ship_building")

def test_name_industry_dict_finance():
    with open('Out/name_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["kirloskar_ind"] == "power_generation/distribution")


def test_create_domain_industry_dict():
    with open('Out/domain_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b)

def test_domain_industry_dict_len():
    with open('Out/domain_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(len(b) == 176)

def test_domain_industry_dict_aviation():
    with open('Out/domain_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b['aerospace_&_defence'] == "aviation")

def test_domain_industry_dict_finance():
    with open('Out/domain_industry_dict.pickle', 'rb') as handle:
        b = pickle.load(handle)
    assert(b["finance__nbfc"] == "finance")