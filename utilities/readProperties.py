import configparser

config = configparser.RawConfigParser()
config.read("/Users/vijaydudhiyan/PycharmProjects/nopcommerceselenium/Configurations/config.ini")
print(config.sections())


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('DEFAULT', 'baseUrl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('DEFAULT', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('DEFAULT', 'password')
        return password
