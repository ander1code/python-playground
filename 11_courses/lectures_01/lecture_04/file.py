# DICTIONARY

def dictStudy():
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

    print(dict)
    print(dict["name"])
    dict["name"] = "Anderson C."
    print(dict["name"])
    print(dict["address"]["city"])
    print(dict["address"]["complement"]["number"])

    def showDictNull():
        dict = {}
        print(dict)
        dict["name"] = "Anderson"
        print(dict)

    showDictNull()

    print(dict.values())
    print(dict.keys())
    print(dict.get("address"))


    # saber quantas chaves têm
    print(len(list(dict.keys())))

    # saber quantas values têm
    print(len(list(dict.values())))

    print(dict.items())
    print(len(list(dict.items())))

    # dict.update("id") = 432
    # rint(dict)

    print(dict["name"]) # error!!!
    print(dict.get("name"))

    dict.update({"salary":999999.99})
    print(dict.get("salary"))

# SET
def SetStudy():
    nums = {5,4,3,2,1}
    print(nums)

    empty_set = set()
    print(empty_set)

    print(type(nums))

    print(len(nums))

    nums.add(999)
    print(nums)

    nums.remove(5)
    print(nums)

    nums.pop()
    print(nums)

    nums.clear()
    print(nums)


    set1 = {1,2,3,4,5}
    set2 = {1,1,7,8,0}
    print(set1.union(set2))
    print(set1.intersection(set2))


    values = {9,9.0}
    print(values)

    values = {9,9.5}
    print(values)


dictStudy()
SetStudy()