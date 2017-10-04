#!/bin/bash

cd ..
rm certificate-traffic-simulator.zip
zip -r -X certificate-traffic-simulator.zip certificate-traffic-simulator

for i in $(seq 1 2); do
    scp certificate-traffic-simulator.zip pc$i.r:.
done

ssh -f pc1.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./lifetime-sim.sh"

ssh -f pc2.r "chmod +x certificate-traffic-simulator.zip;
rm -rf certificate-traffic-simulator/
unzip certificate-traffic-simulator.zip;
rm certificate-traffic-simulator.zip;
cd certificate-traffic-simulator;
./node-sim.sh"
