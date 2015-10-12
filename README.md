# Description

Extended MSP(MultiWii Serial Protocol) connector that you can use to connect and communicate with [Cleanflight](https://github.com/cleanflight/cleanflight). We will use it to handle the extended MultiWii Serial Protocol to send/receive data from Naze32 board.

# Test

- Connect your Naze32 board with USB
- Config serial port

```
board = EMSP("/dev/cu.SLAB_USBtoUART",115200)
``` 

- Run test

```shell
python test.py ATTITUDE  
python test.py RC  
python test.py RAW_IMU  

```

 
# Author

- [Innoecho](Innoecho@outlook.com)
- [CCharlieLi](ccharlieli@live.com)

# License

GPLv3




