dict_FQDN_IP = {}
#only thing that changes between the two variables is number in server
#and the that last byte in the IP address
#can loop to add all 6 entries to the dictionary
#use the dictionary["key"] = value formate in my loop
for i in range(1,7):
    offsetIP = i + 9
    dict_FQDN_IP[f"server{i}.testlab.com"] = f"192.16.1.{offsetIP}"


for key in dict_FQDN_IP:
    print(key)

for key in dict_FQDN_IP:
    print(dict_FQDN_IP[key])

for i in range(7,9):
    offsetIP = i + 9
    dict_FQDN_IP[f"server{i}.testlab.com"] = f"192.168.1.{offsetIP}"

def testKey(dict, key):
    if key in dict.keys():
        print(f"{key} is in the dictionary and has the IP address {dict[key]}" )
    else:
        print(f"{key} is not in the dictionary")

testKey(dict_FQDN_IP,"server2.testlab.com")
testKey(dict_FQDN_IP,"server10.testlab.com")


