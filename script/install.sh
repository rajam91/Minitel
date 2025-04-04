#!/bin/bash

password = ""
password_confirmation = " "
invalid=1

clear
echo "Create user"
#create a new user
while [ $invalid -eq 1 ]
do
    read -p "Enter username : " username
    egrep "^$username" /etc/passwd >/dev/null
    if [ $? -eq 0 ]; then
        clear
        echo "$username already exists!"
        read
        clear
        echo "Enter another username."
    else
        invalid=0
    fi
done

while [ $password != $password_confirmation ]
do
    clear
    read -s -p "Enter password : " password
    echo
    read -s -p "Confirm password : " password_confirmation
    if [ $password != $password_confirmation ]
    then
        echo
        echo "The passwords are different."
        read
    fi
done

clear
pass=$(perl -e 'print crypt($ARGV[0], "pswd")' $password)
#useradd -m -p "$pass" "$username"

python3 /Users/marwah/Desktop/group-1040572-marwah/minitel-2/minitel/menu.py --username"$username" --password"$password"
