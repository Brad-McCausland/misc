Bradley McCausland - W01053708
Cryptography assignment 4
12/7/2016

Contained are three files: a client, a server, and a file with methods that are imported
from the previous two. Running the two without arguments will set up a connection on
port 8001 on localhost by default. Next, the client will prompt the user to enter a
message, which will be encrypted, send to the server, and decrypted and displayed after
ket exchange takes place.

Invoking either program with the 's' flag will prompt the user to enter a custom
port and an ip address for the client. In addition, the 'd' flag will cause both
programs to display the data being sent. 

python client.py
python client.py d
python server.py s
python server.py sd


Note: In the process of testing I encountered a bug that sometimes causes the server to
crash on line 62 when trying to cast corrupted data to an int. The bug is fairly rare and
difficult to reproduce, and thus far I have not discovered the cause. I believe it has
something to do with messages arriving out of order, and so I've spaced out key network
operations with sleep commands. This seems to help, though it makes the programs a bit
sluggish. Hopefully it won't occur during grading, but if it does just go ahead and try
again, I promise it works most of the time :)
