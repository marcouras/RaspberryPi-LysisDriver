__author__ = "Claudio Marche"

from HTTP.req import req
from Lib.xml.dom.minidom import getDOMImplementation
# "xml.dom.minidom" implementazione minima dell'interfaccia Document Object Model
# con una API simile a quella in altri linguaggi
from Lib.xml.dom.minidom import parseString

# smartplug

host = "192.168.1.1"
auth = ('admin', '1234')

class SmartPlug(object):


    def __init__(self):
        # crea una nuova istanza SmartPlug
        self.url = "http://%s:10000/smartplug.cgi" % host
        self.auth = auth
        self.domi = getDOMImplementation()



    def _xml_cmd_setget_state(self, cmdId, cmdStr):
        # crea una rappresentazione XML per il comando
        # type cmdId:  str     Usa 'setup' per cambiare lo stato
        # type cdcStr: str     Usa 'ON' o 'OFF'
        doc = self.domi.createDocument(None, "SMARTPLUG", None)
        doc.documentElement.setAttribute("id", "edimax")
        cmd = doc.createElement("CMD")
        cmd.setAttribute("id", cmdId)
        state = doc.createElement("Device.System.Power.State")
        cmd.appendChild(state)
        state.appendChild(doc.createTextNode(cmdStr))
        doc.documentElement.appendChild(cmd)
        xml = doc.toxml()
        return xml

        '''
        Esempio codice xml formatosi:
        <?xml version="1.0" ?><SMARTPLUG id="edimax"><CMD id="setup"><Device.System.Power.State>ON</Device.System.Power.State></CMD></SMARTPLUG>
        '''



    def _xml_cmd_get_pc(self, what):
        # rappresentazione xml per restituire potenza o corrente consumata
        # type what: str     usa 'NowPower' o 'Nowcurrent"
        doc = self.domi.createDocument(None, "SMARTPLUG", None)
        doc.documentElement.setAttribute("id", "edimax")
        cmd = doc.createElement("CMD")
        cmd.setAttribute("id", "get")
        pwr = doc.createElement("NOW_POWER")
        cmd.appendChild(pwr)
        state = doc.createElement("Device.System.Power.%s" % what)
        pwr.appendChild(state)
        doc.documentElement.appendChild(cmd)
        xml = doc.toxml()
        return xml

        '''
        Esempio codice xml formatosi:
        <?xml version="1.0" ?><SMARTPLUG id="edimax"><CMD id="get"><NOW_POWER><Device.System.Power.NowPower/></NOW_POWER></CMD></SMARTPLUG>
        '''



    def _post_xml(self, xml, code):
        # post comando xml
        files = {'file': xml}
        # creo un'istanza req
        call = req(self.url, None, self.auth, files)
        # uso il metodo post
        res = call.post()
        # se code vale 1, stiamo usando il metodo state, percio' non abbiamo bisogno di un valore di ritorno
        if (code):
            return None
        # se code vale 0, abbiamo bisogno del valore di ritorno
        return parseString(res.text)



    def state(self, value):
        # set stato SmartPlug
        # value prende valori 'ON' o 'OFF'
        if value == "ON":
            self._post_xml(self._xml_cmd_setget_state("setup", "ON"),1)
        else:
            self._post_xml(self._xml_cmd_setget_state("setup", "OFF"),1)


    def power(self):
        # ritorna la potenza consumata
        dom = self._post_xml(self._xml_cmd_get_pc("NowPower"),0)
        power = dom.getElementsByTagName("Device.System.Power.NowPower")[0].firstChild.nodeValue
        return round(float(power),1)        # cast a float e approssimazione a una cifra


    def current(self):
        # ritorna la potenza consumata
        dom = self._post_xml(self._xml_cmd_get_pc("NowCurrent"),0)
        current = dom.getElementsByTagName("Device.System.Power.NowCurrent")[0].firstChild.nodeValue
        return round(float(current),1)