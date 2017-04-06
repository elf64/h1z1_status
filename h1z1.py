import lxml.html
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 

r = Render("https://www.daybreakgames.com/status")
result = r.frame.toHtml()
formatted_result = str(result.toAscii())
tree = lxml.html.fromstring(formatted_result)

for x in tree.xpath('//div[@id="h1z1xx"]//tbody//tr'):
    f = x.xpath(".//td/text()")
    print ' '.join(f)

