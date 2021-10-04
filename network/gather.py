import netmiko

connection = netmiko.ConnectHandler(ip='10.10.20.175', device_type="cisco_ios", username='cisco', password="cisco")
connection.enable()
serial = connection.send_command('sh version')
print(serial)
print(connection.send_command('ping 10.10.20.175'))
