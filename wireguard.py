import json

sample_outband ={
  "type": "wireguard",
  "tag": "W1",
  "local_address":       [
    "172.16.0.2/24",
    "2606:4700:110:8056:6ec9:563a:d8e7:5097/128"
  ],
  "private_key": "AN/vE11+V8r25aGti20+ZPv3LfWckXfzGJlDQuxpCkc=",
  "server": "162.159.192.171",
  "server_port": 864,
  "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
  "mtu": 1306,
  "fake_packets": "40-80",
  "fake_packets_size": "40-100",
  "fake_packets_delay": "4-8",
  "fake_packets_mode": "m4"
}
outbounds = {"outbounds": []}

num = 1
with open("wgcf-profile.conf", "r") as file:
    f = file.readlines()
    sample_outband["private_key"] = f[1].split(" ")[2].strip()
    sample_outband["peer_public_key"] = f[7].split(" ")[2].strip()
    sample_outband["server"] = f[10].split("=")[1].strip().split(":")[0].strip()
    sample_outband["server_port"] = int(f[10].split("=")[1].strip().split(":")[1].strip())

    sample_outband["tag"] = f"W{num}"
    addressV4 = f[2].split("=")[1].strip()
    addressV6 = f[3].split("=")[1].strip()
    sample_outband["local_address"] = [addressV4, addressV6]

    outbounds["outbounds"].append(sample_outband)

    json_object = json.dumps(outbounds, indent = 2)
    print(json_object)
    with open("sample.json", "w") as js:
        json.dump(json_object, js)

