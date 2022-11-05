import yaml

with open("fileconfig.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    
print("cfg: ", cfg)
for section in cfg:
    print('section: ', section)
    print('data: ', cfg[section])
    