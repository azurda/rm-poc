rm-poc
=========
When deleting a file using *del* or *rm* (Windows, Linux) the file is actually not removed. If you do that, the file is likely to be recovered. 

In reality, what _rm_ does is unlinking the file, in other words: The file is still in the system, waiting for other memory space to fill it; it only removes the filename association to the file. 

To avoid this, this script will NOP (x90) every byte of the file and then afterwards delete it, which in case of being recovered afterwards it will be filled with NOP.

This will prevent at a minimum recover the data simply by reading the media again using standard system functions.

Unreliable fileystems
---------
* btrfs
* ssd's
* reiserfs
* COW

    $ alias del="python rm.py"

    $ del file

