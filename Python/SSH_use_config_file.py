from netmiko import ConnectHandler

iosv_l2_Switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.35.101',
    'username': 'patrick',
    'password': 'cisco'
}

iosv_l2_Switch3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.35.103',
    'username': 'patrick',
    'password': 'cisco'
}

iosv_l2_Switch4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.35.104',
    'username': 'patrick',
    'password': 'cisco'
}

with open ('switch_config_file') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_Switch, iosv_l2_Switch3, iosv_l2_Switch4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
