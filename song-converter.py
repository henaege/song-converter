import boto3
import wx

# import the newly created GUI file
import form

session = boto3.Session(profile_name='converter')

filePath = ""

class FileFrame(form.MyFrame1):
    def __init__(self, parent):
        form.MyFrame1.__init__(self, parent)




app = wx.App(False)
frame = form.MyFrame1(None)
frame.Show(True)
# start the applications
app.MainLoop()
