# OpenADR_NodeRed
1) Setup the VTN virtual machine using provided Virtual HDD
2) Use script_comed_vtn_update.py to update real time data from ComEd website to VTN
3) Install Node-RED
4) Install the OpenADR library from "https://github.com/MTU-IMES-LAB/OpenADR"
5) Copy to Node-RED the flow provided in the file named "flow.txt"
6) Use Model.m to simulate the vehicle battery

Note: If you want to see console based message exchange between VEN and VTN please replace the installed openADR file with one provided in folder named Diagnostic Node. Installed file must be present in "C:/users/<computer name>/.node-red/nodes/OpenADR/"


File Structure:
|-Virtual Machine HDD
|-->nebland-oadr-vtn-appliance-v0.9.4-4(ubuntu 14.04)-disk1
|-Diagnostic Node
|-->OpenADR.js
|-flow.txt
|-Readme.txt
|-script_comed_vtn_update.py
