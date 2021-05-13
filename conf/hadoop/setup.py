import os 
import time 
os.system("clear && figlet -tc Setting Up AWS Cloud environment")
time.sleep(2)

os.system("ansible-playbook /root/menu/hadoop/setup_env.yml")

os.system("clear && figlet -tc Building HDFS-MAPREDUCE cluster on AWS")
time.sleep(2)

os.system("ansible-playbook /root/menu/hadoop/setup_mapred.yml -i /root/menu/inventory/hdfs-mapred.txt")
