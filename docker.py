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


def pull_image(): # Method for pulling/downloading the docker image form the docker hub
    os.system("clear && figlet -f script -tc Pulling Image")

    image = input("\n\n\n\t\t\t\t Please enter the image name [also specify the version if you want] : ")
    o = subprocess.run("docker pull {} &> /dev/null".format(image), shell=True)
    if o.returncode == 0:
        green("Image download succesfully")
    else:
        red("Error in downloading image, please specify correct image name with version.")

def launch_container():  # Method for launching the docker container
    os.system("clear && figlet -f script -tc Launching Container")

    image_name = input("\n\n\n\t\t\t\t Please enter the image name : ")
    os_name = input("\n\t\t\t\t Enter the name you want to give to container [else just press enter] : ")
    if len(os_name) != 0:
        o = subprocess.run(
            "docker run -dit --name {} {} &> /dev/null".format(os_name, image_name), shell=True)
    else:
        o = subprocess.run("docker run {} &> /dev/null".format(image_name), shell=True)
    if o.returncode == 0:
        green("Container launched successfully")
    else:
        red("Error in launching container, please specify correct image name with version.")


def remove_image():  # Method for removing the image
    os.system("clear && figlet -f script -tc Deleting Image")
    image_name = input("\n\n\n\t\t\t\t Enter the image name you want to delete : ")
    o = subprocess.run("docker rmi -f {} &> /dev/null".format(image_name), shell=True)
    if o.returncode == 0:
        green("Image deleted Successfully")
    else:
        red("Error in removing image, please give correct Image name with it's version. ")


def remove_container():  # method for removing the container
    os.system("clear && figlet -f script -tc Deleting Image")
    name_or_id_of_os = input("\n\n\n\t\t\t\t Enter the name or id of the container/os you want to delete :")
    o = subprocess.run("docker rm {} &> /dev/null".format(name_or_id_of_os), shell=True)
    if o.returncode == 0:
        green("Conatiner deleted successfully")
    else:
        red("Error in deleting container, please make sure the name is correct & container is stopped ")

def cp_base_to_cont():  # Method for copying the content from the base os to the conatiner
    os.system("clear && figlet -f script -tc Copying Content from Base System to the Container")
    content = input("\n\n\n\t\t\t\t Enter the path of the content you want to copy from base os to container : ")
    bos = input("\n\t\t\t\t Enter the container name or container id : ")
    path_in_os = input("\n\t\t\t\tEnter the location in the conatiner where you want to store the content : ")
    o = subprocess.run("docker cp {} {}:{} &> /dev/null".format(content, bos, path_in_os), shell=True)
    if o.returncode == 0:
        green("The file conetent has been copied to the respective docker conatiner successfully")
    else:
        red("Error in copying content, please make sure path is correct. ")


def cp_cont_to_base():  # Method for copying the content  from container to the base os
    os.system("clear && figlet -f script -tc Copying Content from the Container to Base System")
    content = input("\n\n\n\t\t\t\t Enter the path of the content you want to copy from container to base os :")
    bos = input("\n\t\t\t\t Enter the os name or id : ")
    path_in_base = input("\n\t\t\t\t Enter the loaction where you want to copy the content in the base os : ")
    o = subprocess.run("docker cp {}:{}  {} &> /dev/null".format(bos, content, path_in_base), shell=True)
    if o.returncode == 0:
        green("The file conetent has been copied to the respective docker conatiner successfully")
    else:
        red("Error in copying content, please make sure path is correct. ")


def see_the_running_cont():  # Method for seeing the currently running container
    os.system("clear && figlet -f script -tc Running Containers")
    green("All running containers")
    subprocess.run("docker ps ", shell=True)


def see_all_cont():  # Method for seeing the all [active+inactive] containers
    os.system("clear && figlet -f script -tc All Containers")
    green("Below is the list of all containers")
    subprocess.run("docker ps -a", shell=True)


def start_exist_cont():  # Method for starting the existing container..
    os.system("clear && figlet -f script -tc Start Existing Container")
    name_id_os = input("\n\n\n\t\t\t\tEnter the name/id of the conatiner/os : ")
    o = subprocess.run("docker start {} &> /dev/null".format(name_id_os), shell=True)
    if o.returncode == 0:
        green("Container started successfully")
    else:
        red("Error in starting container, please check name is correct or not.")


def start_docker_service():  # Method for starting the docker service
    subprocess.run('ansible-playbook conf/docker/setupdoc.yml --extra-vars "hostname=localhost" &> /dev/null',shell=True)
    subprocess.run("systemctl start docker", shell=True)


def stop_running_docker():  # method for stopping the running container
    os.system("clear && figlet -f script -tc Stopping Container")
    os_name = input("\n\n\n\t\t\t\t Enter the os/container name/id : ")
    o = subprocess.run("docker stop {} &> /dev/null".format(os_name), shell=True)
    if o.returncode == 0:
        green("Container stopped successfully")
    else:
        red("Error in stopping container, please check whether container is up or not. ")


def get_images():
    os.system("clear && figlet -f script -tc Docker Images")
    green("Below is the list of all your docker images")
    subprocess.run("docker images",shell=True)


def inspect_docker():
    os.system("clear && figlet -f script -tc Inspecting Container")
    c = input("Enter Name or ID of container : ")
    subprocess.run("docker inspect {}".format(c),shell=True)


def remove_allcont():
    os.system("clear && figlet -f script -tc Deleting all containers")
    i = input("\n\n\n\t\t\t\t Do you want to delete all containers? (y/n) : ")
    if i=="y" or i=="Y":
        o = subprocess.run("docker rm -f $(docker container ls -aq) &> /dev/null",shell=True)
    if o.returncode == 0:
        green("All containers are deleted successfully ")
    else:
        red("Some error in deleting all containers ")


def docker_ip():
    os.system("clear && figlet -f script -tc Container IP ")
    n = input("\n\n\n\t\t\t\t Enter container name/id : ")
    o = subprocess.run('docker inspect -f "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}" {} '.format(n), shell=True)

    if o.returncode != 0:
        red("Some error in retrieving IP Address, please check with the name is correct or not.")

def build_apacheServer_image_dockerfile():
    os.system("clear && figlet -f script -tc Apache Image")
    print()
    print()
    green("This will create a Apache Webserver with the html page inside /root/menu/httpd folder.However you can put your own webpage there with name index.html.")
    img = input("\n\n\t\t\t\t Please provide image name with version(myimage:v1) : ")
    o = subprocess.run("docker build -t {} /root/menu/dockerimages/httpd/.  &> /dev/null".format(img),shell=True)
    if o.returncode == 0:
        green("Apache Image build successfully")
    else:
        red("Error in building image")

def runWebServer():
    os.system("clear && figlet -f script -tc Running WebServer")
    os_name = input("\n\n\n\t\t\t\t Please provide container name : ")
    #image = input("\n\n\n\t\t\t\t Please provide Containerized Image : ")
    port = input("\n\t\t\t\t Enter Port number where you want to expose webserver : ")
    subprocess.run("docker build -t defaultweb /root/menu/dockerimages/httpd/.  &> /dev/null",shell=True)
    o = subprocess.run("docker run -dit --name {} -p {}:80 defaultweb &> /dev/null".format(os_name,port),shell=True)
    if o.returncode == 0:
        green("WebServer running successfully")
    else:
        red("Error in launching Webserver")
