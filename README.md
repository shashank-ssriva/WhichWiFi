# WhichWiFi
A tiny Python3 script that tells you which WiFi network your Mac is connected to.

# Introduction
There are times when you have more than 1 WiFi routers and they all differ in their speed/tariff or data-limit. Sometimes you want to connect to router A because it is cheaper & has unlimited data. Sometimes you want to restrict your usage of router B because it has a data cap & also incurs a lot of money if that cap is crossed. Sometimes you want to connect to router B because you need fast speed. Situations may vary. Problem arises when your Mac switches to another router silently if connected router runs out of battery. Mac also tries to connect to other networks if certain settings (*remeber this network or auto-connect*) are enabled. You probably don't want to shop online when your Mac is connected to a free WiFi in a coffee shop, which is not that secure.

``WhichWiFi`` checks the network your Mac is connected to & displays it as a notification. You can put it inside a Cron job so that you continue to receive notifications about currently connected network without human intervention.

# Installation
You will need ``pync``(*Python Notification Center*) package to run this script. You can install it using..
```bash
pip3 install pync
```
Afterwards, clone/download my repository.
```bash
git clone https://github.com/shashank-ssriva/WhichWiFi.git
```
# Usage
You can run the script manually by executing...
```bash
admin@shashank-mbp ~/D/Python Scripts> python3 WhichWiFi.py
You are connected to : Airtel-WD670-EA3C
```
But the best way is to put the script in a Cron job & set a suitable duration. For example below Cron job sends a notification every minute. You can use any value as per your choice.

```bash
* * * * * /usr/local/bin/python3 "/Users/admin/Desktop/Python Scripts/WhichWiFi.py" >/Users/admin/Desktop/cronout.log 2>/Users/admin/Desktop/cronerror.log
```
## Screenshot

Here is the script in action!!

<img src="https://github.com/shashank-ssriva/WhichWiFi/blob/master/WhichWiFi.png" height="100" width="250">
