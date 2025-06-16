import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")

## sender ke ander ip add receiver ka he aayega 
## hamesha and reciver ka he aayega khud ka 

    ip_add="172.20.10.2"
    port =8888
    complete_add=(ip_add,port)
    s.bind(complete_add)

    while True:
        message,sender_address=s.recvfrom(1024)

        print("raw message", message)
        print("sender address", sender_address)

        decoded_msg =message.decode("ascii")
        print("message",decoded_msg)

except Exception as e:
    print("an error occured",e)
    