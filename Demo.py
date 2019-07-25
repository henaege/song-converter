# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

class MyFileDropTarget(wx.FileDropTarget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window

    #----------------------------------------------------------------------
    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """
        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))
        print(filenames)
        for filepath in filenames:
            self.window.updateText(filepath + '\n')

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 252,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter a number", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 5,1 ), wx.DefaultSize, wx.TE_CENTER )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Find the square", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
									   wx.Point(5, 1), wx.DefaultSize,
									   wx.TE_CENTER)
		bSizer1.Add(self.m_textCtrl2, 0,
					wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.FindSquare )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def FindSquare( self, event ):
		event.Skip()


