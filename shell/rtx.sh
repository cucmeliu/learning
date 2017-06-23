#!/bin/bash

function alarm(){
    user="$1"
    content="$2"
    stat=$(curl --connect-timeout 60 -s "http://yw.test.com:8082/alarmServer/bus?user_name="${user}"&sendType=2,3&title=【服务器IP信息】&systemId=5&password=I6rXbaO****&content="${content}"")
    echo ${stat}
}

#site = web_guanwangtest_0001 | web_4399_0001

function setconf(){
    site=$1
    number=$(echo ${site##*_})
    echo $site $number ${site%_*}
    case ${site%_*} in
        web_duowan)
            title="多玩${number}区";;
        web_4399)
            title="4399${number}区";;
        web_guanwangtest)
            title="测试服${number}区";;
        *)
            echo "没有这个代理的信息，请更新脚本!"
    esac
}

function getconf(){
    ip_config=($(ifconfig eth0|awk -F'[ :]+' '/inet/{print $4}') $(ifconfig eth0:1|awk -F'[ :]+' '/inet/{print $4}'))
    setconf "$(hostname)"
    content="${title}%0Aip地址：${ip_config[0]}%20${ip_config[1]}"
}

function main(){
    getconf
    alarm "jerry.huang,Shelly.yu" "${content}"
    #echo ${content}
}
main