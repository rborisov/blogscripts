#! /usr/bin/env python
#sudo fdisk -l =>Output
"""kracekumar@python-lover:~$ sudo fdisk -l

Disk /dev/sda: 320.1 GB, 320072933376 bytes
255 heads, 63 sectors/track, 38913 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0xf897e57b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1               1         192     1536000   27  Unknown
Partition 1 does not end on cylinder boundary.
/dev/sda2             192       10786    85097782    7  HPFS/NTFS
/dev/sda3           10787       37572   215153680+   f  W95 Ext'd (LBA)
/dev/sda4           37572       38914    10778624   17  Hidden HPFS/NTFS
/dev/sda5           18954       22993    32442349   83  Linux
/dev/sda6           27878       37572    77869056    7  HPFS/NTFS
/dev/sda7           10787       15916    41199605   83  Linux
/dev/sda8           18615       18953     2722986   82  Linux swap / Solaris
/dev/sda9   *       15916       18497    20731904   83  Linux
/dev/sda10          18497       18614      945152   82  Linux swap / Solaris
/dev/sda11          22993       27671    37580800   83  Linux
/dev/sda12          27671       27878     1655808   82  Linux swap / Solaris

Partition table entries are not in disk order
"""
#df -T
"""
kracekumar@python-lover:~$ df -T
Filesystem    Type   1K-blocks      Used Available Use% Mounted on
/dev/sda11    ext4    36990536  15201872  19909624  44% /
none      devtmpfs     1474632       740   1473892   1% /dev
none         tmpfs     1481240      3844   1477396   1% /dev/shm
none         tmpfs     1481240       240   1481000   1% /var/run
none         tmpfs     1481240         0   1481240   0% /var/lock
/dev/sda7     ext4    40551772  36086304   2405492  94% /mnt/ubuntu9.10
/dev/sda9     ext4    20406140   6774300  12595248  35% /mnt/fedora14
/dev/sda5     vfat    32426480  29893680   2532800  93% /mnt/movies
/dev/sda2  fuseblk    85097776  69094072  16003704  82% /mnt/system
/dev/sda6  fuseblk    77869052  64031512  13837540  83% /mnt/others

"""
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
