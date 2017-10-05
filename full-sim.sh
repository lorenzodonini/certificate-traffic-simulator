#!/bin/bash

cd ..
rm certificate-traffic-simulator.zip
zip -r -X certificate-traffic-simulator.zip certificate-traffic-simulator

for i in $(seq 2 6); do
    scp certificate-traffic-simulator.zip pc$i.r:.
done

#ssh -f pc1.r "chmod +x certificate-traffic-simulator.zip;
#rm -rf certificate-traffic-simulator/
#unzip certificate-traffic-simulator.zip;
#rm certificate-traffic-simulator.zip;
#cd certificate-traffic-simulator;
#./node-sim.sh 1 3"

ssh -f pc2.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 4 7"

ssh -f pc3.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 8 10"

ssh -f pc4.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 11 13"

ssh -f pc5.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 14 16"

ssh -f pc6.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 17 20"

