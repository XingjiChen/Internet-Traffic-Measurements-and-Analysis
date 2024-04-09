#!/bin/bash

function command_usage_help {
    echo "Usage $0 server nameaddr [-t type] [-c class] [-x] [-o opt]"
    echo "  If nameaddr is an ip address, -x switch must be supplied"
    echo "  Multiple options can be provided space separated but then it must"
    echo "  be quoted, e.g. ... -o '+norec +multiline' ."
    echo "  See 'man dig' for options"
    echo
    echo "Additional output contains ';CURL:' line providing following times:"
    echo " - time_starttransfer: when dig has completed"
    echo " - time_pretransfer: https request sent"
    echo " - time_connect: TCP connection established"
}

if [ $# -lt 2 ]
then
    command_usage_help
    exit 1
fi

function make_url {
    echo -n "server=$server"
    if [ ${reverse:-none} != none ]
    then
	echo -n "&addr=$name"
    else
	echo -n "&name=$name"
    fi
    if [ "${type:-none}" != none ]
    then
	echo -n "&type=$type"
    fi
    if [ "${class:-none}" != none ]
    then
	echo -n "&class=$class"
    fi
    if [ "${opts:-none}" != none ]
    then
	echo -n "&opt="
	echo -n "$opts" | sed 's/%/%37/g;s/[+]/%2b/g;s/ /+/g'
    fi
}
server=$1
shift
name=$1
shift
while [ $# -gt 0 ]
do
    case $1 in
	-t) type=$2
	    shift
	    ;;
	-c) class=$2
	    shift
	    ;;
	-x) reverse=1
	    ;;
	-o) opts=$2
	    shift
	    ;;
	*) echo "Invalid argument: $1"
	   command_usage_help
	   exit 2
	   ;;
    esac
    shift
done
url=https://tools.dice.aalto.fi/dig?$(make_url)
echo $url
curl -s -w ';CURL: %{time_starttransfer} %{time_pretransfer} %{time_connect}\n'  $url
