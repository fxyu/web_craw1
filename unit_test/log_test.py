import logging

FORMAT = '[%(filename)s:%(lineno)d] %(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    handlers=[
        logging.FileHandler("myLog.log",mode='a'),
        logging.StreamHandler()       
    ]
)

def main():
    logging.info('ABC')
    logging.warning('This is a warning')


main()
