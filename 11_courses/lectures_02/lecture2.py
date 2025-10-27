
#                              Observação: Todos os exemplos devem conter 
#                              tratamento dos dados que estão entrando. 
# Lecture 02 

#     1. Criar uma string contendo um “Lorem Ipsum”, e imprima essa string,  
#        bem como o tamanho desta mesma string. 

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

#    2.  Criar um código que exemplifique a utilização de caracteres especiais 
#        como estes: \n, \t, \\, \', \", \r, \b, \f, \v e \0. 

phrase = """Lorem ipsum \ndolor sit amet, \0consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(phrase)


#    3. Criar um código que exemplifique a utilização de caracteres na 
#        impressão de uma string a partir de um início e fim dessa mesma string 
#        utilizando slicing [início:fim]. 

print(lorem[0:11])
print(lorem[6:11])

#    4.  Criar um código que exemplifique a utilização de funções específicas 
#        para strings, como: 

#        •find(), endswith(), replace(), count(), capitalize(), upper(), lower(). 

name = "anderson"
print("find: ", name.find("d"))
print("endswith: ", name.endswith("son"))
print("replace: ", name.replace("son", "father"))
print("count(n): ", name.count("n"))
print("capitalize: ", name.capitalize())
print("upper: ", name.upper())
print("lower: ", name.lower())
print("len: ", len(name))

#    5. Criar um código que exemplifique a utilização do if…, elif e else. 

age = 24
if age >= 18:
    print("Adulto")
elif age >= 14 and age < 18:
    print("Adolescente")
else:
    print("Criança")