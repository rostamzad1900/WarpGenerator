import csv
import json
import os

def zero_packet_loss(row):
    loss = row[1]
    if type(loss) == str:
        loss = loss.replace("%", "")
        try:
            l = float(loss)
            if l < 1.0:
                return True
        except:
            return False
    return False

misaka_results = "./CFscanners/misaka/result-ipv4-21.08.2024.csv"
peyman_results = "./CFscanners/peyman/result-ipv4-21.08.2024.csv"
misaturo_results = "./CFscanners/misaturo/result-ipv4-21.08.2024.csv"

if os.path.isfile(peyman_results):
    with open(peyman_results, "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
num = 1
config_list_1 = []
config_list_2 = []
for i , row in enumerate(data):
    if i % 2 == 0 or i == len(data) - 1:
        continue
    if zero_packet_loss(data[i]) and zero_packet_loss(data[i+1]):
        ip1 = data[i][0]
        ip2 = data[i+1][0]
        warp_config_1 = f"warp://p1@:{ip1}?ifp=40-80&ifps=40-100&ifpd=4-8&ifpm=m4#m4&&detour=warp://p2@{ip2}#WoW_Peyman_{num}"
        warp_config_2 = f"warp://{ip1}/?ifp=1-3&ifpm=m4&&detour=warp://@{ip2}/?ifp=1-3&ifpm=m4#WoW_Peyman_{num}"
        config_list_1.append(warp_config_1)
        config_list_2.append(warp_config_2)
        num += 1
with open ("peyman_warp_config_1.txt", "w") as file:
	for item in config_list_1:
		file.write(f"{item}\n")

with open ("peyman_warp_config_2.txt", "w") as file:
	for item in config_list_2:
		file.write(f"{item}\n")




