from configparser import ConfigParser
import os

def readConfig(section,key):
    config = ConfigParser()
    config.read(os.getcwd()+"/../ConfigurationData/config.ini")
    print(config)
    return config.get(section,key)




