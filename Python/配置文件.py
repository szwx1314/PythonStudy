import configparser

config = configparser.ConfigParser()
# config["server"]={'server_ip':'172.16.1.71',
#                   'port':'10000'}
#
# config["program"]={'version':'1.1.1.0',
#                    'updatetime':'2017-04-01 10:10:00'}
#
# with open('config.ini','w') as configfile:
#     config.write(configfile)

config.read('config.ini')
print(config.sections())
print(config.defaults())

print(config['server']['server_ip'])