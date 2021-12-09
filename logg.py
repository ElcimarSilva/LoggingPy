import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s') # para passar data e hora + level do log + mensagem do log
# logging.basicConfig(level=logging.DEBUG, filename='log.log') # Para mandar para um arquivo

""" logging.debug("Debug!!")

logging.info("Info!!")

logging.warning("Warning!!")

logging.error("Error!!") """



variavel = 'cloudwatch'
logging.info({"é assim que se faz logs para mandar para cloudwatch":variavel})