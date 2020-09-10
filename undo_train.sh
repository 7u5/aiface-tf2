# cmd :
if [ $# -gt 0 ]; then
name=$1
model="inception_resnet_v2"
rm -rf ../data/$name/${name}_train*
rm -rf ../data/$name/${name}_valid*
rm -rf ../data/$name/labels.txt
rm -rf my_models/$model/${name}

else
    echo "please give name of class"
    exit

fi

