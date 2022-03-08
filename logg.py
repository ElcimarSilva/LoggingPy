import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s') # para passar data e hora + level do log + mensagem do log
# logging.basicConfig(level=logging.DEBUG, filename='log.log') # Para mandar para um arquivo

variavel = 'cloudwatch'
logging.debug({"é assim que se faz logs para mandar para cloudwatch":variavel}) # este não aparece a menos que coloque lvl debug
logging.info({"é assim que se faz logs para mandar para cloudwatch":variavel})
logging.warning({"é assim que se faz logs para mandar para cloudwatch":variavel})
logging.error({"é assim que se faz logs para mandar para cloudwatch":variavel})
logging.critical({"é assim que se faz logs para mandar para cloudwatch":variavel})