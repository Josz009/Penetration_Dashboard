
import msfrpc
from app.config import Config

def run_metasploit_exploit(module, target, payload):
    client = msfrpc.Msfrpc({})
    client.login(Config.METASPLOIT_USER, Config.METASPLOIT_PASS)

    exploit = client.call('module.execute', ['exploit', module, {
        'RHOSTS': target,
        'PAYLOAD': payload
    }])

    return exploit
