import pickle
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

def create_domain_industry_dict():
    domain_names = ["Agri","Alcohol","Automobile-Ancillaries","Aviation","Banks",
                  "Capital-Goods","Chemicals","Construction-Materials","Consumer-Durables","Containers-Packaging","Diamond-Jewellery","Diversified",
                  "Electricals","ETF","Finance","FMCG","Footwear","Healthcare","Hospitality","Industrial-Gases-Fuels","Infrastructure","Insurance","Logistics",
                  "Manufacturing","Media-Entertainment","Metals-Mining","Miscellaneous","Oil-Gas","Paper","Photographic-Products","Plastic-Products","Power",
                  "Real-Estate","Retailing","Ship-Building","Software-IT-Services","Telecom","Textiles","Trading"]
    
    domain_industry_dict = {}
    name_industry_dict = {}

    for domain in tqdm(domain_names):
        temp_set = set()
        domain = domain.lower()
        URL = "https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/" + domain + ".html"
        print(URL)
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        temp_data = soup.find_all("td", attrs = {"class":"brdrgtgry"})
        i = 0 
        if(len(temp_data) == 0):
            continue
        company_name = ""
        for count,t in enumerate(temp_data):
            print(str(i) + " : " + t.text.lower())
            if(i == 0):
                company_name = t.text.lower().replace(" ","_").replace("-","_").strip()
                company_name = company_name.replace("__","_")
                print(company_name)
            if(i == 1):
                temp_set.add(t.text.lower())
                industry = t.text.lower().replace(" ","_").replace("-","_").strip()
                industry = industry.replace("__","_")
                name_industry_dict[company_name] = industry
            i += 1
            if(i > 5):
                i = 0
        for ind in temp_set:
            domain  = domain.lower().replace("-","_")
            domain = domain.replace("__","_").strip()
            domain_industry_dict[ind] = domain

    with open('Out/name_industry_dict.pickle', 'wb') as handle:
        pickle.dump(name_industry_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('Out/domain_industry_dict.pickle', 'wb') as handle:
        pickle.dump(domain_industry_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def main():
    create_domain_industry_dict()

if __name__ == "__main__":
    main()