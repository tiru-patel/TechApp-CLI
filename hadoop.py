import getpass
import time
import subprocess
import os
import shutil
from TextFormatter import TextFormatter
def green(text):
    cprint = TextFormatter()
    cprint.cfg("g","k","b")
    print("\n\n")
    cprint.center(text)
    print("\n\n")
    cprint.reset()


def red(text):
    cprint = TextFormatter()
    cprint.cfg("r","k","b")
    print("\n\n")
    cprint.center(text)
    print("\n\n")
    cprint.reset()

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


def create_cluster():
    print()
    print_centre("SETTING UP HADOOP CLUSTER")
    opt = input("Have you configured variables in roles(y/n) : ")
    if opt=="y" or opt == "Y": 
        print()
        subprocess.run("> /root/menu/inventory/hdfs-mapred.txt",shell=True)
        os.system("clear && figlet -tc Setting Up AWS Cloud environment")
        time.sleep(2)

        os.system("ansible-playbook /root/menu/conf/hadoop/setup_env.yml")

        os.system("clear && figlet -tc Building HDFS-MAPREDUCE cluster on AWS")
        time.sleep(2)

        os.system("ansible-playbook /root/menu/conf/hadoop/setup_hdfsmapred.yml -i /root/menu/inventory/hdfs-mapred.txt")
        green("Hadoop-MapReduce Cluster Setup on AWS is done!")
    else: 
        red("Please provide appropriate variables in roles.")
