import urllib3
from virl2_client import ClientLibrary

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
client = ClientLibrary("https://10.10.20.161", "developer", "C1sco12345", ssl_verify=False)
lab = client.create_lab()
print(lab.id)
s1 = lab.create_node("s1", "server", 50, 100)
s2 = lab.create_node("s2", "server", 50, 200)
print(s1, s2)
lab.connect_two_nodes(s1, s2)