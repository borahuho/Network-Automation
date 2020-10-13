from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_utils.plugins.functions import print_result

nr = InitNornir("config.yaml")

result = nr.run(task=napalm_get, getters=["interfaces"])
print_result(result)