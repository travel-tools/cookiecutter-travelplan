# pip imports
import logging
import os
import sys


# Package dirpath
DIRPATH_package = os.path.join(os.path.dirname(os.path.realpath(__file__)))

# Package resources
DIRPATH_resources = os.path.join(DIRPATH_package, 'resources')

# Package sub-resources
DIRPATH_config = os.path.join(DIRPATH_resources, 'config')


def _init_logger():
    """
    Set the format of the Python root logger.
    """
    formatter = logging.Formatter('%(asctime)s '
                                  '[%(process)d] '
                                  '%(levelname)-5s '
                                  '[%(name)-48s] '
                                  '%(message)s')

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger()  # Python root logger

    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)


_init_logger()
