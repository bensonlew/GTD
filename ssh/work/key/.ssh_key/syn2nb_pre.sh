#!/bin/bash
FILE=${1}
PAR=${2}

export KEY=/mnt/lustre/users/sanger-dev/sg-users/shicaiping/script/.ssh_key
abspath() {
    cd "$(dirname "$1")"
    printf "%s/%s\n" "$(pwd)" "$(basename "$1")"
    cd "$OLDPWD"
}
# FILE=`readlink -f $FILE`
FILE=`abspath $FILE`
FILETO=$FILE
DIR=$FILE
echo $DIR
if [ -d "$FILE" ]; then
    FILETO=`echo $FILE | sed 's/\/$//g' |sed 's/[^\/]*$//'`
    DIR=$FILETO
else
    DIR=`echo $FILE | sed 's/[^\/]*$//'`
fi

# 旧框架同时传两个目录
FILETO_SG=`echo $FILETO|sed 's/sanger-dev/sanger/;s/sanger_bioinfo/test_sanger_bioinfo/'`
DIR_SG=`echo $DIR|sed 's/sanger-dev/sanger/;s/sanger_bioinfo/wpm2/test_sanger_bioinfo/'`


FILETO_ISG=`echo $FILETO|sed 's/lustre\/users\/sanger-dev/ilustre\/users\/isanger/;s/sanger_bioinfo/test_sanger_bioinfo/'`
DIR_ISG=`echo $DIR|sed 's/lustre\/users\/sanger-dev/ilustre\/users\/isanger/;s/sanger_bioinfo/test_sanger_bioinfo/'`

echo $DIR_SG
# echo $DIR
# create dir
ssh -i $KEY/sanger_id_rsa sanger@10.2.3.172 '
if [ -d '$DIR_SG' ];then
echo "sanger文件夹存在"
else
echo "sanger文件夹不存在, 创建"
mkdir -p '$DIR_SG'
fi
'
# echo $FILETO
scp $PAR -i $KEY/sanger_id_rsa $FILE sanger@10.2.3.172:$DIR_SG

# create dir
ssh -i $KEY/isanger_id_rsa isanger@10.2.0.115 '
if [ -d '$DIR_ISG' ];then
echo "isanger文件夹存在"
else
echo "isanger文件夹不存在, 创建"
mkdir -p '$DIR_ISG'
fi
'
# echo $DIR_ISG
# echo $FILETO
echo $DIR_ISG
scp $PAR -i $KEY/isanger_id_rsa $FILE isanger@10.2.0.115:$DIR_ISG


