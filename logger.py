import os

os.system('sysdig -c spy_users && tail -f /var/log/secure')
