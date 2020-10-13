from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

Router = nr.filter(F(groups__contains="CSR_Routers"))

description = "Description set with Nornir Netmiko"

description_config = [
    "interface GigabitEthernet3",
    f"description {description}",
]
   
result = nr.run(netmiko_send_config, config_commands=description_config)
print_result(result)
