"""
schema.py for all AOS-S related scripts
Author: Miguel Balagot
Email: mbalagot@hpe.com
"""

import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

shared_secret = os.environ.get('SHARED_SECRET') or 'default'
cppm_api_username = os.environ.get('CPPM_API_ADMIN') or 'default'
cppm_api_password = os.environ.get('CPPM_API_ADMIN_PASSWORD') or 'default'

radius_uri = '/radius_servers'
radius_prof_uri = '/radius_profile'
radius_dyn_auth_uri = '/radius_dyn_authorization'
radius_auth_uri = '/radius_authentication'
radius_acct_uri = '/radius_accounting'
radius_data: {'radius_server_id': 1,
                   'address': {'version': 'IAV_IP_V4', 'octets': '15.129.80.136'},
                   'shared_secret': shared_secret,
                   'authentication_port': '1812',
                   'accounting_port': '1813',
                   'is_dyn_authorization_enabled': True,
                   'time_window_type': 'TW_POSITIVE_TIME_WINDOW',
                   'time_window': 300,
                   'is_oobm': False,
              }

radius_profile: {'retry_interval': 5,
                  'retransmit_attempts': 3,
                  'dead_time': Null,
                  'key': shared_secret,
                  'dyn_autz_port': 3799,
                  'tracking_name': 'radius-tracking-user',
                  'is_tracking_enabled': False,
                  'cppm_details': {'username': cppm_api_username, 'password': cppm_api_password},
                }
radius_server_group: {'server_group_name': 'radius_group1',
                      'server_ip': {'version': 'IAV_IP_V4', 'octets': '15.129.80.136'}
                      }