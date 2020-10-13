from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_utils.plugins.functions import print_result

nr = InitNornir("config.yaml")

r2 = nr.filter(name="CSR2")

result = r2.run(napalm_cli, commands=["show version", "show ip interface brief"])
print_result(result)