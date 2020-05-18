# IP RECON TOOL

A python tool which uses web APIs to gather informaation about a an IP Address.

## Langauge Used : Python

## Prerequisits :

Python 3.x and Python IDLE/Shell

## Libraries Used :

Requests<br/>
Sys<br/>
Json<br/>
Argsparse<br/>
Make sure the the required Libraries are installed correctly.

## Installation :

Clone the repository into your system by typing :

```
git clone https://github.com/whokilleddb/iprecon

```

Once cloned , cd into the directory and install the requirements as follows :

```
cd iprecon
pip3 install -r requirements.txt

```
 
Now type run the script using :

```
python3 iprecon.py

```

The following should give a similar output as :

![](https://github.com/whokilleddb/iprecon/blob/master/Images/1.png)

To get help about the operations , type in :

```
python3 iprecon.py -h

```

It will give an output as such :

![](https://github.com/whokilleddb/iprecon/blob/master/Images/2.png)

To get the information about any IP Address or Website type in :


```
python3 iprecon.py -i example.com #You can put in any IP or domain name. I have used google.com

```
If your input is valid , you will get an output as such :

![](https://github.com/whokilleddb/iprecon/blob/master/Images/3.png)

If it is not valid or otherwise , the output screen will be as such :

![](https://github.com/whokilleddb/iprecon/blob/master/Images/4.png)

## API Source :

The application get's it's information from (https://ip-api.com/)


