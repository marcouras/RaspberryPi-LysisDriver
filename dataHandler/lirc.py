import os
import time

class Lirc():

    def __init__(self):
        self.num_lines = 0

    # metodo decodifica
    # a partire dal codice di comando, crea il file lirc ed invia il comando
    def send(self, mode, fan, vane):

        codes = self.compose(mode, fan, vane)

        file = open("/home/pi/lircd.conf", "w")

        file.write("begin remote\n\n\t")
        file.write(" name MY_REMOTE\n\t flags RAW_CODES\n\t eps\t 30\n\t aeps\t 100\n")
        file.write("\n\t frequency   38000\n\n")
        file.write("\tbegin raw_codes\n\n")
        file.write("\tname MY_TEST\n")

        file.write("\t\t 3500\t 1600")

        if (codes[0] == '0'):
            file.write("\t470\t 400")
        else:
            file.write("\t470\t 1200")

        if codes[1] == '0':
            file.write("\t470\t 400")
        else:
            file.write("\t470\t 1200")

        file.write("\n\t")

        newcodes = codes[2:]

        i = 0

        while i < len(newcodes):
            if i == 0:
                file.write("\t")
            if newcodes[i] == '0':
                file.write("\t470\t 400")
            else:
                file.write("\t470\t 1200")
            if ((i + 1) % 3 == 0):
                file.write("\n\t")
            i = i + 1

        file.write("\t470")
        file.write("\n\n\t end raw_codes\n")
        file.write("end remote\n")
        file.close()

        os.system("sudo /etc/init.d/lirc stop")

        os.system("sudo cp ~/lircd.conf /etc/lirc/lircd.conf")
        os.system("sudo /etc/init.d/lirc start")
        os.system("irsend SEND_ONCE MY_REMOTE MY_TEST")
        time.sleep(1)
        os.system("sudo /etc/init.d/lirc stop")



    # metodo per comporre codice
    def compose(self, mode, fan, vane):

        b0  =  [1,1,0,0,0,1,0,0]
        b1  =  [1,1,0,1,0,0,1,1]
        b2  =  [0,1,1,0,0,1,0,0]
        b3  =  [1,0,0,0,0,0,0,0]
        b4  =  [0,0,0,0,0,0,0,0]

        if mode == "COOL":
            b5 = [0,0,1,0,0,1,0,0]      # byte ON/OFF
            b6 = [1,1,0,0,0,0,0,0]      # byte mode
        elif mode == "HEAT":
            b5 = [0,0,1,0,0,1,0,0]
            b6 = [1,0,0,0,0,0,0,0]
        elif mode == "OFF":
            b5 = [0,0,0,0,0,1,0,0]
            b6 = [1,0,0,0,0,0,0,0]


        if mode == "COOL":
            b7 = [1,1,1,1,0,0,0,0]      # byte temperatura  #cool = 16
        elif mode == "HEAT":
            b7 = [0,0,0,0,0,0,0,0]      # heat = 31
        elif mode == "OFF":
            b7 = [0,0,0,0,0,0,0,0]


        if fan == 1:                    # byte fan e vane
            b8a = [0,1,0]
        elif fan == 2:
            b8a = [1,1,0]
        elif fan == 3:
            b8a = [1,0,1]

        if vane == 1:       # vane 1 = alto
            b8b = [1,0,0,0,0]
        elif vane == 2:
            b8b = [0,1,0,0,0]
        elif vane == 3:
            b8b = [1,1,0,0,0]
        elif vane == 4:
            b8b = [0,0,1,0,0]
        elif vane == 5:     # vane 5 = basso
            b8b = [1,0,1,0,0]
        b8  =  b8a + b8b


        b9  =  [0,0,0,0,0,0,0,0]
        b10 =  [0,0,0,0,0,0,0,0]
        b11 =  [0,0,0,0,0,0,0,0]
        b12 =  [0,0,0,0,0,0,0,0]

        sum = b0 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12

        sum.reverse()

        nb0 = sum[0:8]
        nb0 = ''.join(str(e) for e in nb0)
        nb0 = int(nb0, 2)

        nb1 = sum[8:16]
        nb1 = ''.join(str(e) for e in nb1)
        nb1 = int(nb1, 2)

        nb2 = sum[16:24]
        nb2 = ''.join(str(e) for e in nb2)
        nb2 = int(nb2, 2)

        nb3 = sum[24:32]
        nb3 = ''.join(str(e) for e in nb3)
        nb3 = int(nb3, 2)

        nb4 = sum[32:40]
        nb4 = ''.join(str(e) for e in nb4)
        nb4 = int(nb4, 2)

        nb5 = sum[40:48]
        nb5 = ''.join(str(e) for e in nb5)
        nb5 = int(nb5, 2)

        nb6 = sum[48:56]
        nb6 = ''.join(str(e) for e in nb6)
        nb6 = int(nb6, 2)

        nb7 = sum[56:64]
        nb7 = ''.join(str(e) for e in nb7)
        nb7 = int(nb7, 2)

        nb8 = sum[64:72]
        nb8 = ''.join(str(e) for e in nb8)
        nb8 = int(nb8, 2)

        nb9 = sum[72:80]
        nb9 = ''.join(str(e) for e in nb9)
        nb9 = int(nb9, 2)

        nb10 = sum[80:88]
        nb10 = ''.join(str(e) for e in nb10)
        nb10 = int(nb10, 2)

        nb11 = sum[88:96]
        nb11 = ''.join(str(e) for e in nb11)
        nb11 = int(nb11, 2)

        nb12 = sum[96:104]
        nb12 = ''.join(str(e) for e in nb12)
        nb12 = int(nb12, 2)

        sum = nb0 + nb1 + nb2 + nb3 + nb4 + nb5 + nb6 + nb7 + nb8 + nb9 + nb10 + nb11 + nb12

        convert = bin(sum)

        new = convert[::-1]

        b13 = new[0:8]

        vect = list(b13)

        b13 = map(int, vect)

        complete = b0 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13

        cod = ''.join(str(e) for e in complete)

        return cod

