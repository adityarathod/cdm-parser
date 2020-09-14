import configparser

config = configparser.ConfigParser()


def main():
    config.read('datasource.ini')
    print(config['chargemasters']['location'])

if __name__ == '__main__':
    main()