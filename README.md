# SimpleMan
"I am a simple man. I see different IP, I update things!" [**](http://knowyourmeme.com/memes/i-m-a-simple-man) SimpleMan is a tiny tool to help users connect their networks over dynamic 
IPs. Computer using SimpleMan will let you know about new IP, when IP is changed.
#### Properties
  - Mail sending
  - Updating DYNDNS hostname
#### Installation
  - Download all files
  - Put _php_ files to a server
  - Put _simpleMan.py_ to node in network with dynamic IP
  - Edit _.conf_ file with required information
  - Rename it to _config.conf_
  - Run _simpleMan.py_
#### Scheduling
You can add the line below to your crontab file.
> 00 * * * * [USER] [SIMPLE_MAN_PATH]/SimpleMan/simpleMan.py
#### Roadmap
_No other feature is planned yet. To suggest new features, or report bugs please use [Github Issues](https://github.com/GarageGroup/SimpleMan/issues)_
