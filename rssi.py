import rssi

interface = 'wlp1s0'
rssi_scanner = rssi.RSSI_Scan(interface)
ap_info = rssi_scanner.getAPinfo(sudo=True)
print(ap_info)