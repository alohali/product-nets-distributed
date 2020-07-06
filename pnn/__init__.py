import socket

config = {}

host = socket.gethostname()
config['host'] = host.lower()
config['location'] = 'apex'

# only data_path is required
if config['host'] == 'altria':
    config['data_path'] = '/home/alohali/code/Ads-RecSys-Datasets/'
    config['env'] = 'cpu'
else:
    if config['location'] == 'apex':
        config['data_path'] = '/home/alohali/code/Ads-RecSys-Datasets/'
    else:
        config['data_path'] = '/home/alohali/code/Ads-RecSys-Datasets/'
    config['env'] = 'gpu'
