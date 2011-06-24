#! /usr/bin/env python
#My partions
#/dev/sda6 ->/mnt/others ->ntfs-3g
#/dev/sda2 ->/mnt/system ->ntfs -3g
#/dev/sda7 ->/mnt/ubuntu9.10 ->ext3
#/dev/sda3 ->/mnt/movies ->ext3
#/dev/sda9 ->/mnt/fedora14 ->ext3
import subprocess
source=('/dev/sda6','/dev/sda2','/dev/sda7','/dev/sda5','/dev/sda9')
dest=('/mnt/others','/mnt/system','/mnt/ubuntu9.10','/mnt/movies','/mnt/fedora14')
type_=('ntfs-3g','ntfs-3g','ext4','vfat','ext4')
for (x,y,z) in zip(source,dest,type_):
	subprocess.Popen(["mount","-t",z,x,y])
	print x,"is mounted in ",y
