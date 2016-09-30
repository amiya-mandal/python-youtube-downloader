import wx
import wx.xrc
import pafy
import sys



'''class MyDialog(wx.Dialog):
   def __init__(self, parent, title):
      super(MyDialog, self).__init__(parent, title = title, size = (250,150))
      panel = wx.Panel(self)
      self.btn = wx.Button(panel, wx.ID_OK, label = "ok", size = (50,20), pos = (75,50))
      #self.btn.Bind()
'''






#frame code
class Myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(536, 354), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        #this is temp lable 0
        self.urllable = wx.StaticText(self, 101, "enter the url of the youtube:", wx.DefaultPosition, wx.DefaultSize,
                                      wx.ALIGN_CENTRE)
        self.urllable.Wrap(-1)
        bSizer1.Add(self.urllable, 0, wx.ALL | wx.EXPAND, 5)

        #this is the conatainor for the url enter
        self.urlcontainer = wx.TextCtrl(self, 102, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.urlcontainer, 0, wx.ALL | wx.EXPAND, 5)

        #this will show the options
        self.show = wx.Button(self, 103, "options", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.show, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.show.Bind(wx.EVT_BUTTON,self.urlsender)

        #this will hold options
        opcontainerChoices = []
        self.opcontainer = wx.ListBox(self, 104, wx.DefaultPosition, wx.DefaultSize, opcontainerChoices, 0)
        bSizer1.Add(self.opcontainer, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)
        #self.opcontainer.SetSelection(0)
        self.Bind(wx.EVT_LISTBOX_DCLICK,self.doubleClick,self.opcontainer)

        #update bar
        self.updator = wx.Gauge(self, 105, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.updator.SetValue(0)
        bSizer1.Add(self.updator, 0, wx.ALL | wx.EXPAND, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #this is temp lable
        self.speed0 = wx.StaticText(self, 106, "speed:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.speed0.Wrap(-1)
        gbSizer1.Add(self.speed0, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        #this will display the speed
        self.speed = wx.StaticText(self, 107, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.speed.Wrap(-1)
        gbSizer1.Add(self.speed, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        #this is temp lable
        self.templable2 = wx.StaticText(self, wx.ID_ANY, "time:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.templable2.Wrap(-1)
        gbSizer1.Add(self.templable2, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        #this will show the time left
        self.time = wx.StaticText(self, 108, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.time.Wrap(-1)
        gbSizer1.Add(self.time, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer1, 1, wx.EXPAND, 5)

        #this button will download the file
        self.download = wx.Button(self, 109, "download", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.download, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        def mi():
            self.download.Bind(wx.EVT_BUTTON, self.adown)

        try:
            mi()

        except:
            a=wx.MessageBox((sys.exc_info()[1]),"error", wx.OK | wx.ICON_INFORMATION)
            if a is None:
                self.opcontainer.Clear()
                mi()

        self.SetSizer(bSizer1)
        self.Layout()
        self.index=0

        self.Centre(wx.BOTH)

    #return url
    def urlsender(self,e):
        #self.opcontainer.Clear()
        url=self.urlcontainer.GetValue()
        self.m=second(first(url))
        #update gause and lable
    def updategause(self,ratio,speed,time):
        self.updator.SetValue(ratio)
        self.speed.SetLabelText(str(speed))
        self.time.SetLabelText(str(time))

    def doubleClick(self,e):
        #self.opcontainer.Clear()
        self.index=self.opcontainer.GetSelection()
        wx.MessageBox( str(self.index),"Selected", wx.OK | wx.ICON_INFORMATION)

    def adown(self,e):
        third(self.index, self.m)
        wx.MessageBox("Download completed", "Download", wx.OK | wx.ICON_INFORMATION)
        self.opcontainer.Clear()



    def __del__(self):
        pass

#class finished here


def first(url):
    av=pafy.new(url)
    data = av.allstreams
    return data


def second(data):
    i=0
    for a in data:
        frame.opcontainer.Append(str(a))

    return data

def third(index,data):
    data[index].download(quiet=True, callback=updag)
    #data[index].download()
    print 'complete'


def updag(self,rec,ratio,rate,time):
    frame.updategause(ratio*100,rate,time)

def intiilzer():
    frame.Show()
    app.MainLoop()






if __name__=='__main__':
    try:
        app = wx.App()
        frame = Myframe()
        intiilzer()
        #first()



    except:
        wx.MessageBox( (sys.exc_info()[1]),"error", wx.OK | wx.ICON_INFORMATION)
        #print "error:",sys.exc_info()[1]
        #frame.opcontainer.Clear()
        #intiilzer()
        #app.MainLoop()