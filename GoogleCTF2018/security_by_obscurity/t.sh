#! /bin/bash

unzip -o -qq obscurity.ZIP

# remember to ctl+c and name the file to new again
# for each round of while True below






# while [ 1 ];
# do 
# 	ls | grep -v "zip" | grep -v "ZIP$" | grep -v "t.sh" | while read line;
#	do
#		mv $line $line.zip
#		unzip $line.zip
#	done
# done

# while [ 1 ];
# do
#	mv new new.xz
#	unxz new.xz
# done

# while [ 1 ];
# do 
#	mv new new.bz2
#	bunzip2 new.bz2
# done

while [ 1 ];
do
	mv new new.gz
	gunzip new.gz	
done




