import subprocess
import shutil

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def automate_lvm():
    print_centre("*  PLEASE ATTACH TWO HARDDISK  *")
    print()
    print_centre("DISPLAYING ALL HARDDISK ATTACHED")
    print()
    print(subprocess.getoutput("fdisk -l"))
    print()
    hd1 = input("Choose the FIRST harddisk, please enter the correct harddisk name : ")
    print_centre("Creating Physical Volume")
    print(subprocess.getoutput("pvcreate {}".format(hd1)))
    print()
    print_centre("PV created")
    opt = input("Do you want to display created Physical Volume(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("pvdisplay {}".format(hd1)))
    print()
    hd2 = input("Choose the SECOND harddisk, please enter the correct harddisk name : ")
    print_centre("Creating Physical Volume")
    print(subprocess.getoutput("pvcreate {}".format(hd2)))
    print_centre("PV created")
    opt = input("Do you want to display created Physical Volume(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("pvdisplay {}".format(hd2)))
    print()
    print_centre("Creating VG")
    vg = input("Please enter your VG name : ")
    print(subprocess.getoutput("vgcreate {} {} {}".format(vg, hd1, hd2)))

    opt = input("Do you want to display created VG(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("vgdisplay {}".format(vg)))
    print()
    print_centre("Now creating Logical Volume from created VG")
    size = input("Please enter size of Logical Volume(LV): ")
    name = input("Please enter name of LV: ")
    print(subprocess.getoutput("lvcreate --size {}G --name {} {}".format(size,name,vg)))
    print("Logical Volume Created")
    opt = input("Do you want to display created LV(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("lvdisplay {}/{}".format(vg,name)))
    print()
    print_centre("LVM JOB DONE")
    print()
