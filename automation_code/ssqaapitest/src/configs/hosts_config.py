
API_HOSTS = {
    "test": "http://192.168.1.100:11002/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}
WOO_API_HOSTS = {
    "test": "http://192.168.1.100:11002/shop/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "172.17.0.1",
                       "database": "wordpress",
                       "table_prefix": "wp_",
                       "socket": "/var/run/mysqld/mysqld.sock",
                       "port": 33002
                       },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'docker': {
              "test": {
                  "host": "host.docker.internal",
                  "database": "wp398",
                  "table_prefix": "wp2p_",
                  "socket": None,
                  "port": 3306
              },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/akinfu/Library/Application Support/Local/run/d84nqkpSm/mysql/mysqld.sock",
                 "port": 3306
                 },
        "dev": {
                  "host": "host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
        "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
    }
}
