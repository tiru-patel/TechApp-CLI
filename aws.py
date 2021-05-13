# *********************  AUTOMATE AWS FUNCTIONALITIES  *********************
import time
import subprocess

o = subprocess.run("aws --version &> /dev/null",shell=True)
if o.returncode != 0:
    print("Please wait, you don't have AWSCLI on your system. I am downloading it.")
    subprocess.run('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"',shell=True)
    subprocess.run("unzip awscliv2.zip",shell=True)
    subprocess.run("sudo ./aws/install",shell=True)
    x = subprocess.run("aws --version")
    if x.returncode == 0:
        print("AWSCLI version2 installed successfully.")
        print("Please configure AWS i.e provide ACCESS KEY and SECRET KEY, use command : aws configure")
        exit()
    else:
        print("Error in installing AWSCLI version2")
else:
    pass

kname = ""
qname = ""
savename = ""
gname = ""

def create_key():
    kname = input("Enter KeyPair name : ")
    qname = input("Enter name by which you want to query : ")
    savename = input("Enter the pem file name you want to save the key.")
    savename = "/root/menu/aws_keys/" + savename
    subprocess.run("aws ec2 create-key-pair --key-name {} --query '{}' > {}.pem".format(kname, qname, savename),
                   shell=True)
    print("Key Value pair is successfully created")
    i = input("Do you want to change permissions of key so that you can use for other configurations (y/n) : ")
    if i=="y":
        subprocess.run("chmod 400 {}.pem".format(savename),shell=True)

def create_securityGroup():
    des = input("Description for security group : ")
    gname = input("Enter security group name : ")
    subprocess.run('aws ec2 create-security-group --description "{}" --group-name "{}"'.format(des, gname), shell=True)
    subprocess.run(
        'aws ec2 authorize-security-group-ingress --group-name {} --protocol tcp --port 22 --cidr 0.0.0.0/0'.format(
            gname))

def provisionEC2():
    security_id = input("Enter Security Group ID : ")
    count = int(input("How many OS you want to provision : "))
    keyname = input("Enter Key Name : ")
    print("Instance Type will be t2.micro by default ...")
    time.sleep(1)
    print("By default Image AMI will be LinuxAMI ...")
    time.sleep(1)
    x = input("Do you want to enter Image ID and Instance type manually? (y/n) : ")
    if x == "y":
        instance_type = input("Enter Instance Type : ")
        Image_ID = input("Enter Image ID : ")
    else:
        instance_type = "t2.micro"
        Image_ID = "ami-052c08d70def0ac62"
    subprocess.run(
        "aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {}".format(Image_ID, count, instance_type, keyname, security_id), shell=True)

def createEBS():
    print("By Default Volume Type will be gp2, size of 1GB and Availability Zone, Mumbai, ap-south-1b")
    i = input("Do you want to enter EBS Block configuration manually? (y/n) : ")
    if i == "y":
        v_type = input("Enter Volume Type : ")
        size = int(input("Enter size (in GB) : "))
        zone = input("Enter Availability Zone : ")
    else:
        v_type = "gp2"
        size = 1
        zone = "ap-south-1b"
    subprocess.run("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(v_type, size, zone),
                   shell=True)
    print("\n EBS Block Volume Successfully Created ...")

def attachEBS():
    v_id = input("Enter EBS Volume ID : ")
    instance_id = ("Enter Instance ID : ")
    subprocess.run("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(v_id, instance_id),
                   shell=True)
    print("\n EBS Volume attached successfully ...")

def create_S3bucket():
    bucket_name = input("Please enter your bucket name : ")
    bucket_region = input("Enter region where you want your bucket to be placed : ")
    subprocess.run("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bucket_name,bucket_region,bucket_region),
                   shell=True)
    print("S3 Bucket has been successfully created")

def get_allBuckets():
    print("Below are all the S3 Buckets you have ...")
    subprocess.run("aws s3 ls",shell=True)

def putDataon_Bucket():
    print("Make sure you have your data file in the current directory.")
    file_name = input("Please provide the file you want to upload in S3 bucket : ")
    bucket_name = input("Which bucket you want to put your data : ")
    subprocess.run("aws s3 cp {} s3://{}".format(file_name, bucket_name),shell=True)
    print("Data has been uploaded to given S3 bucket successfully.")
    opt = input("Do you want to make your data public? (y/n) : ")
    if opt=="y" or opt=="Y":
        subprocess.run("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(bucket_name,file_name),shell=True)
        print("Data has been made public")
    else:
        pass

def setup_cloudFront():
    origin_domain=input("Please provide your Origin Domain Name(Eg: mybucket.s3.amazonaws.com) : ")
    subprocess.run("aws cloudfront create-distribution --origin-domain-name {}".format(origin_domain),shell=True)
    print("Cloud Front Distribution is successfully created")
