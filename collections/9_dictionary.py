person = {
    "id": 1,
    "name": "Anderson",
    "status": True,
    "salary": 61523.11,
    "gender": 'M',
    "address": {
        "street": "Street 01",
        "district": "bairro",
        "uf": "JR",
        "city": "cidade"
    },
}

for p, d in person.items():
    print(f"  - {p}: {d}")
    if isinstance(d, dict):
        for k, v in d.items():
            print(f"  - {k}: {v}")



users = {
    "name": "Anderson", "status":True,
    "name": "Fernanda", "status":False,
    "name": "Renata", "status":False,
    "name": "Cristiane", "status":True,
    "name": "Francine", "status":True,
    "name": "Joana", "status":False
}


# -------------


def fdict():
    dict = {1:'Anderson', 2:'Sarah', 3:'Anne', 4:'Lucy', 5:'Tiffany', 6:'Anne'}
    dict[7] = 'Ava'
    print(dict)

    print(len(dict))
    print(str(dict))
    print(type(dict))

    dict2 = dict.copy()
    print(dict2)

    dict3 = {8:'Will'}
    dict2.update(dict3)
    print(dict2)

    print('Registro 1: %s' %(dict.get(1)))

    # dict.setdefault(dict, default = None)
    # print(dict)

    # dict.fromkeys()

    # print(dict.has_key(1))
    print(dict.items())
    print(dict.keys())
    print(dict.values())

    dict.clear

    del dict

    try:
        print(dict)
    except Exception as e:
        print('Dicionário já não está mais referenciado.')
    return

# ---------------------

def fdict():
    dict = {1 : True, 2: 'A', 3:"Anderson", 4 : (3 + 3j), 5 : ["green", "yellow"],  6 : {'1':"Anderson"}, 7 : (1,2,3)}
    print (dict.keys())
    print (dict.values())
    print (dict[3])


# ---------------------

# dictionary:

person = {
    "id": 1,
    "name": "Anderson",
    "status": True,
    "salary": 61523.11,
    "gender": 'M',
    "address": {
        "street": "Street 01",
        "district": "Gávea",
        "uf": "RJ",
        "states": "Rio de Janeiro"
    },
}

for p, d in person.items():
    print(f"  - {p}: {d}")
    if isinstance(d, dict):
        for k, v in d.items():
            print(f"  - {k}: {v}")

# ---------------------

dict = {
        "id" : 123,
        "name": "Anderson",
        "gender": "M",
        "salary": 6172617.11,
        "status": True,
        "address": {
            "street": "street 01",
            "number": 59,
            "district": "MyDistrict",
            "city": "Rio de Janeiro",
            "State": "RJ",
            "Country": "Brazil",
            "complement": {
                "street": "Alameda",
                "number": 10
            }
        },
        "functions": ("Programmer", "Analyst"),
        "subject": ["database", "web", "IA", "Standalone"]
    }


print(dict["name"])

print(dict.get("address",{}).get("complement",{}).get("number"))

print(dict.get("address",{}).get("city"))

print(list(dict.keys()))
print(list(dict.values()))

print(dict.keys())
print(dict.values())

print(dict["address"]["complement"]["number"])






