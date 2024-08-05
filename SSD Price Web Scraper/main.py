import pypartpicker
from pypartpicker import Scraper
from time import sleep

pcpp = Scraper()
ssd_list = []
result = []
file = "ssd.txt" 
with open(file) as ssd:
    print("Searching PCPP...")
    for line in ssd:
        ssd_name = line.strip()
        print(f"Searching {ssd_name}...")
        ssd_object = pcpp.part_search(ssd_name, region = "ca") # Searches for ssds only in Canada
        one_tb_ssd_list = [ssd for ssd in ssd_object if ("1-tb" in ssd.url) and ssd.price != None]
        for one_tb_ssd in one_tb_ssd_list:
            price = float(one_tb_ssd.price.strip("$"))
            result.append((one_tb_ssd.url, price))
        sleep(2.5)

    result = sorted(result, key=lambda x: x[1])
    print("Sorted SSDs:")
    for url, price in result:
        print(f"{url} - ${price:.2f}")
   



