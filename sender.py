import socket
try:
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #dgram -- datagram
    print ("socket successfuly created")
    ip_add="172.20.10.2"
    port=8888                                      #00-65535
    target_add= (ip_add,port)
    message= input("enter the message :😊")
    encoded_msg=message .encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent successfully")
    s.close()

except Exception as e:
    print("an error occurred",e)