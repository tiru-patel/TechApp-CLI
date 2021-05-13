import subprocess
import os
import shutil
from TextFormatter import TextFormatter
import time 
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

def setup_k8s_aws():
    print()
    print_centre("SETTING UP MULTINODE KUBERNETES CLUSTER")
    opt = input("Have you configured variables in roles(y/n) : ")
    if opt=="y" or opt == "Y":
        print()
        subprocess.run("> /root/menu/inventory/k8s-cluster.txt",shell=True)
        os.system("clear && figlet -tc Setting Up AWS Cloud environment")
        time.sleep(2)

        os.system("ansible-playbook /root/menu/conf/k8s_aws/setupec2.yml")

        os.system("clear && figlet -tc Building KUBERNETES  cluster on AWS")
        time.sleep(2)

        os.system("ansible-playbook /root/menu/conf/k8s_aws/setup_cluster.yml -i /root/menu/inventory/k8s-cluster.txt")
        green("Wordpress site is hosted with MySQL Database connected on top of Multinode Kubernetes Cluster on AWS...")
    else:
        red("Please provide appropriate variables in roles.")


