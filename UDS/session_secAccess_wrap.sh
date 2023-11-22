echo "Opening Extended Diagnostic Session"
echo "10 03"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0

echo "Unlocking Security Access Level 3"
python3 level3.py

echo "Opening Programming Session"
echo "10 02"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0

echo "Requesting Level 1 Seed"
echo "27 01"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0 

echo "Reading Memory"
#echo "23 14 00 01 A0 00 FF"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0
#echo "23 24 00 01 A8 00 04 44"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0

#while [ true ]
#do
    echo "3E 80"  | isotpsend -p 00 -s 7E0 -d 7E8 vcan0
#    sleep 1
#done

echo "Unlocking Security Access Level 1"
python3 level1.py