#!/bin/bash

cd ..
rm certificate-traffic-simulator.zip
zip -r -X certificate-traffic-simulator.zip certificate-traffic-simulator -x *.csv

for i in $(seq 1 6); do
    scp certificate-traffic-simulator.zip pc$i.r:.
done

ssh -f pc1.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 1 4"

ssh -f pc2.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 5 8"

ssh -f pc3.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 9 11"

ssh -f pc4.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 12 14"

ssh -f pc5.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 15 17"

ssh -f pc6.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh 18 20"

