from pypresence import Presence
import time

id = input("Client ID : ")
RPC = Presence(id)
RPC.connect()

RPC.update(
    state="Lamp Handsome",
    large_image="",
    details="Lamp Pro",
    start=time.time()
)
try:
    print("[ STATUS: Connected! ]")
    while True:
        time.sleep(200)
        
except Exception as e:
    print(e)
