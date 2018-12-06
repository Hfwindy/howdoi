import os
import sys
import logging
import logging.config

def config_logger(log_file, config_file):

    """Configure a logger based on a file

    """
    # set up logging
    assert os.path.exists(log_file), '{} file does not exist.'.format(log_file)
    assert os.path.exists(config_file), '{} file does not exist.'.format(config_file)

    logging.config.fileConfig(os.path.join(sys.path[0],config_file))

