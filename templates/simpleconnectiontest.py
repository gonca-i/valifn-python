#!/usr/bin/env python

"""
    Test API connection to Valispace, holds for determined amount of time
    Returns run date.
"""

__author__ = "Gonçalo Ivo"
__copyright__ = "Copyright 2022, Valispace"
__credits__ = ["Gonçalo Ivo"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Valispace"
__email__ = "support@valispace.com"
__status__ = "Development"

# Standard modules
from valispace import API
from datetime import datetime, timedelta
import time
import site
site.addsitedir('script_code/') # Required to import other files in script
from .settings import Username, Password # Required to User Secrets defined at Settings

VALISPACE = {
    'domain': 'https://.valispace.com/',
    'username': Username,
    'password': Password
}

DEFAULT_VALUES = {
    "project": 24,
    "start_date": "",
    "today_date": ""    
}

def main(**kwargs):

    api = API(
            url = VALISPACE.get('domain'),
            username = VALISPACE.get('username'),
            password = VALISPACE.get('password')
        )
    DEFAULT_VALUES["start_date"] = api.get('project/'+str(DEFAULT_VALUES["project"]))['start_date']
    DEFAULT_VALUES["today_date"] = datetime.now().strftime("%Y-%m-%d")
    print (DEFAULT_VALUES["today_date"])
    print(kwargs)

    pass

if __name__=='__main__':
    main()
