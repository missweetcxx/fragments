#!/usr/bin/env bash

method=$1
in_ip="99.99.99.99"
in_url="url"


switchToPreview()
{
inner_host=`cat /etc/hosts | grep ${in_url} | awk '{print $1}'`
if [[ ${inner_host} = ${in_ip} ]];then
	echo "${inner_host} ${in_url} added already"
elif [[ ${inner_host} != "" ]];then
    echo " configuration is not consistent with expectation, plz modify manually "
else
    inner_ip_map="${in_ip}	       ${in_url}"
    echo ${inner_ip_map} >> /etc/hosts
    if [ $? = 0 ]; then
        echo "${inner_ip_map} successfully added, host is `cat /etc/hosts`"
    fi
fi
}

switchToOnline()
{
inner_host=`cat /etc/hosts | grep ${in_url} | awk '{print $1}'`
if [[ ${inner_host} != "" ]];then
	sed -i "" "/${in_url}/d" /etc/hosts
    echo "${in_url} configuration has been deleted"
else
    echo "${in_url} configuration not exist"
fi
}

main()
{
if [[ ${method} == "online" ]]; then
    echo "you're about to switch to online";
    switchToOnline
elif [[ ${method} == "preview" ]]; then
    echo "you're about to switch to preview";
    switchToPreview
else
    echo "which environment do you want to switch to ? online/preview";
exit 0;
fi
}
main