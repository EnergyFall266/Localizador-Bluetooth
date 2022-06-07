import asyncio
import time 

from bleak import BleakScanner

async def main():
    # start=time.time()
    devices = await BleakScanner.discover(timeout=3)
    for d in devices:
        if (d.address == '90:E2:02:91:62:09' or d.address == '3C:A3:08:96:68:60' or d.address == '4C:24:98:5D:05:A3'): 
            print(d.rssi)
    # print(time.time()-start)
for i in range(0,50):
    
    asyncio.run(main())
    


    
    