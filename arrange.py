import shutil, time

with open("block.txt", "r") as file:
	domains = file.readlines()

domains = [x.strip() for x in domains]

def change(str_: str) -> str:
	str_ = f"127.0.0.1\t{str_}\n127.0.0.1\twww.{str_}\n"
	return str_

domains = list(map(change, domains))

core = '''# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

'''

for x in domains:
	core += x
print(core)

def main() -> None:
	file = open("hosts", "w")
	file.writelines(core)
	file.close()

main()
time.sleep(3)

# replaces the hosts file in drivers/etc
def replace_hosts() -> None:
	shutil.copy('hosts', "C:\\Windows\\System32\\drivers\\etc")
replace_hosts()
