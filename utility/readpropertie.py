
import configparser
config = configparser.RawConfigParser()
config.read('./configuration/config.ini')


class ReadConifig:

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getusername():
        username = config.read('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
