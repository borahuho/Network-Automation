## For Nornis 2.nogwat

from nornir import InitNornir

nr = InitNornir("config.yaml")

from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

result = nr.run(netmiko_send_command, command_string="sh ip int br")

print_result(result)