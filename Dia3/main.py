from tabulate import tabulate
import requests

#json-server Dia3/data/datos.json -b 5502

a = requests.get("http://localhost:5502")
a = a.json()

print(tabulate(a, headers="keys", tablefmt="html"))