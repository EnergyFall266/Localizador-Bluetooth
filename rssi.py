import asyncio 

from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        if (d.address == '90:E2:02:91:62:09'): 
            print(d.address, d.rssi)

asyncio.run(main())