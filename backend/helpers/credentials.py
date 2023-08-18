import os
import json


def get_credentials():
    env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(env_file_dir, "models_simulator/env.json"), "r") as f:
        s = f.read()
        s = s.replace('\t','')
        s = s.replace('\n','')
        s = s.replace(',}','}')
        s = s.replace(',]',']')
        data = json.loads(s)
        # print(data['dev_prod'])
    return data


credentials = get_credentials()

def dev_prod():
    if credentials['dev_prod'] == "local":
        # print('localllllllll')
        return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models_simulator.settingss.development')
    else:
        # print('ppppppppppppppppp')
        return os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models_simulator.settingss.production')


def dev_prod_email():
    if credentials['dev_prod'] == "local":
        return 'local'
    else:
        return 'prod'

