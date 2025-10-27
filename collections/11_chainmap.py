# CHAINMAP

from collections import ChainMap

dict1 = {'a': 'value1', 'b': 'value2'}
dict2 = {'c': 'value3', 'a': 'value4'}
print("\n", ChainMap(dict1, dict2))

combined = dict1.copy()
combined.update(dict2)
print(combined) # pega uma unica de instancia de cada item.

# chainmap (alteracao seletiva em dicionario):

from collections import ChainMap

config_default = {"arch": "x64", "language": "en"}
config_user = {"language":"pt-br"}
config = ChainMap(config_user, config_default)
print(config["arch"], config["language"])

