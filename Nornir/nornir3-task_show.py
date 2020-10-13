from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

Router = nr.filter(F(groups__contains="CSR_Routers"))

result = Router.run(netmiko_send_command, command_string="show ip int brief")

print_result(result)