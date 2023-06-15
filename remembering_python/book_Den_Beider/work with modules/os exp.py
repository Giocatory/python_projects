import os


# os name
print(os.name)  # posix
os_info = os.uname()
print(os_info)
# posix.uname_result(
    # sysname='Linux', 
    # nodename='giocatory', 
    # release='5.15.0-73-generic', 
    # version='#80-Ubuntu SMP Mon May 15 15:18:26 UTC 2023', 
    # machine='x86_64'
    # )
print(os_info[0])  # Linux

# env
env_list = os.environ
for i in env_list:
    print(i)
