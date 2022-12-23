import configparser, os

config_file = '.\\src\\config\\config.ini'

def config_generation()-> configparser.ConfigParser:
    # make config file
    config = configparser.ConfigParser()

    # make mongodb object
    config['mongodb'] = {}
    config['mongodb']['host'] = 'localhost'
    config['mongodb']['port'] = '27017'
    config['mongodb']['database'] = 'test'
    config['mongodb']['collection'] = 'urlitem'

    # make hash object
    config['hash'] = {}
    config['hash']['map'] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    config['hash']['max-id'] = '916132831'
    config['hash']['padding-width'] = '2048'
    config['hash']['split-sep'] = '4'
    config['hash']['base-num'] = '62'

    # make cache object
    config['cache'] = {}
    config['cache']['capacity'] = "100"
    config['cache']['size'] = "0"
    
    return config

def check_config():
    if not os.path.isfile(config_file):
        with open(config_file, 'w', encoding='utf-8') as configfile:
            config_generation().write(configfile)

def get_config(key:str)-> configparser.ConfigParser():
    config_data = configparser.ConfigParser()
    config_data.read(config_file, encoding='utf-8')
    return config_data[key]