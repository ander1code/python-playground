import .sample_01.c_client as c_client
import .sample_02.b_server as b_server

def execution_unique():
   b_server.server__unique()
   c_client.client__unique()     

def execution_lopping():
    b_server.server_looping()
    c_client.client_looping()     

print("********************************************")
print("SOCKETS")
print("********************************************")
print("1 - Unique ")
print("2 - Looping")
print("********************************************")
opc = input("Enter option: ")
if opc == 1:
   execution_unique()
else:
   execution_lopping()
