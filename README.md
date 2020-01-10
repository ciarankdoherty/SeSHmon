# SecureShellMonitoring

A simple monitoring program that shows active users on your linux system, and what they are up to. It displays running processes in a live view.

# **Linux Installation:**

`git clone https://github.com/60x/SecureShellMonitoring && cd SecureShellMonitoring`

`curl -s https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public | sudo apt-key add -  `

`sudo curl -s -o /etc/apt/sources.list.d/draios.list https://s3.amazonaws.com/download.draios.com/stable/deb/draios.list  `

sudo apt-get update

sudo apt-get -y install linux-headers-$(uname -r)

sudo apt-get -y install sysdig

python logger.py
```

# **Python Installation:**
```
sudo apt-get upgrade

sudo apt-get install python3

sudo apt-get install python3-pip

sudo apt-get update
```
