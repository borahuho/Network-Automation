from nornir import InitNornir
from nornir_scrapli.tasks import (
    get_prompt,
    send_command,
    send_configs
)
from nornir_utils.plugins.functions import print_result

nr = InitNornir("config.yaml")

command_results = nr.run(task=send_command, command="show ip int brief")
print("Result for CSR1:")
print(command_results["CSR1"].result)

print("Result for CSR2:")
print(command_results["CSR2"].result)
