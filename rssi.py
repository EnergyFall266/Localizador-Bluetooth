import asyncio

from bleak import BleakScanner

# with open('coleta.csv', 'a') as f:
#     f.write('Address,RSSI\n')    

async def main():
    global a,b,c    
    devices = await BleakScanner.discover(timeout=4)
    for d in devices:
        if (d.address == '90:E2:02:91:62:09' and a<1000): 
            with open('coleta.csv', 'a') as f:
                f.write(f'{d.address},{d.rssi},{coordx},{coordy}\n')
            
            # print(d.address ,d.rssi)
            # print(a)
            a+=1
        if (d.address == '3C:A3:08:96:68:60' and b<1000):
            with open('coleta.csv', 'a') as f:
                f.write(f'{d.address},{d.rssi},{coordx},{coordy}\n')
            # print(d.address ,d.rssi)
            # print(b)
            b+=1
        if (d.address == '4C:24:98:5D:05:A3' and c<1000):
            with open('coleta.csv', 'a') as f:
                f.write(f'{d.address},{d.rssi},{coordx},{coordy}\n')
            # print(d.address ,d.rssi)
            # print(c)
            c+=1
a=0
b=0
c=0
coordx=9
coordy=6
for i in range(0,2050):
    
    asyncio.run(main())
    if(a==1000 and b==1000 and c==1000):
        break


    
    