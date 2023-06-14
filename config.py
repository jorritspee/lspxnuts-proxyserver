import os
from typing import List


def envget_str(key: str, dflt: str = '') -> str:
    """
    Gets a value from the os.environ, and defaults to the value of dflt if not set in the environment.
    :param key: environment variable name
    :param dflt: default value, if not present in the environment
    :return: either the value of the environment variable or the default value (dflt)
    """
    return os.environ[key] if key in os.environ else dflt


def envget_strs(key: str, dflt=None) -> List[str]:
    """
    Gets a value from the os.environ, and defaults to the value of dflt if not set in the environment.
    :param key: environment variable name
    :param dflt: default value, if not present in the environment
    :return: either the value of the environment variable or the default value (dflt)
    """
    if dflt is None:
        dflt = []
    val = os.environ[key] if key in os.environ else None
    if val:
        return [v.strip() for v in val.split(',')]
    return dflt


def envget_str_required(key: str) -> str:
    """
    Gets a value from the os.environ, and defaults to the value of dflt if not set in the environment.
    :param key: environment variable name
    :return: either the value of the environment variable ora ValueError
    """
    if key in os.environ:
        return os.environ[key]
    else:
        raise ValueError(f'Missing environment variable {key}')


def envget_bool(key, dflt: bool = False) -> bool:
    """
    Gets a value from the os.environ, and defaults to the value of dflt if not set in the environment.
    :param key: environment variable name
    :param dflt: default value, if not present in the environment
    :return: either the value of the environment variable or the default value (dflt)
    """
    val = envget_str(key, 'True' if dflt else 'False')
    return val.lower() in ['true', 'yes', '1', 'y']


def envget_int(key, dflt: int = 0) -> int:
    """
    Gets a value from the os.environ, and defaults to the value of dflt if not set in the environment.
    :param key: environment variable name
    :param dflt: default value, if not present in the environment
    :return: either the value of the environment variable or the default value (dflt)
    """
    return int(os.environ[key]) if key in os.environ else dflt


DEBUG = envget_bool('DEBUG', False)
BASE_URL_NUTS_NODE = envget_str('BASE_URL_NUTS_NODE', 'http://nuts-node:1323')
BASE_URL_LSP = envget_str('BASE_URL_LSP', 'https://zim.prf001.aorta-zorg.nl')
LSP_APPLICATION_ID = envget_str('LSP_APPLICATION_ID', '80000002')
FILENAME_TRANSACTION_TOKEN = envget_str('FILENAME_TRANSACTION_TOKEN', '/token/transactietoken.txt')
URA_LSP_DEELNEMER = envget_str('URA_LSP_DEELNEMER', '90019288')
VENDOR_DID = envget_str('VENDOR_DID', 'did:nuts:E5VztsdgrvgtwhZGwg7mdrgRJ7UK4qmLF4txUveADBFW')
SENDER_AORTA_APPLICATION_ID = envget_str('SENDER_AORTA_APPLICATION_ID', '110')
