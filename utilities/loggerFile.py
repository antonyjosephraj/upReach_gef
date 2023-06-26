import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\AntonyJosephRaj\\OneDrive - JMAN Group Ltd\\PROJECTS\\UPREACH\\Automation\\20230613_automation_v3\\logs\\automation.log",
                                format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger