import sys
from turtle import title
import wx
import wx.xrc
path=''#初始化地址
class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = '制作by-Tby落雨|QQ:2086097937|博客地址：tby-luoyu.github.io|制作不易，请勿用于商业用途！', pos = wx.DefaultPosition, size = wx.Size( 618,416 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.biaoti = wx.StaticText( self, wx.ID_ANY, u"博客（md)文章编辑器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.biaoti.Wrap( -1 )

		self.biaoti.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.biaoti, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.biaoti_wenzhang = wx.StaticText( self, wx.ID_ANY, u" 标题：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.biaoti_wenzhang.Wrap( -1 )

		gSizer2.Add( self.biaoti_wenzhang, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.tage = wx.StaticText( self, wx.ID_ANY, u"标签：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tage.Wrap( -1 )

		gSizer4.Add( self.tage, 0, wx.ALL, 5 )

		self.text_tage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.text_tage, 0, wx.ALL, 5 )


		gSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.wenzhangwenjian = wx.StaticText( self, wx.ID_ANY, u"导入文章文件（目前仅支持.txt文件）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wenzhangwenjian.Wrap( -1 )

		gSizer10.Add( self.wenzhangwenjian, 0, wx.ALL, 5 )


		gSizer1.Add( gSizer10, 1, wx.EXPAND, 5 )

		self.wenjianmulidizhi = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.Point( 600,600 ), wx.Size( 300,-1 ), wx.FLP_DEFAULT_STYLE )
		gSizer1.Add( self.wenjianmulidizhi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.zhushi1 = wx.StaticText( self, wx.ID_ANY, u" 文章内容：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zhushi1.Wrap( -1 )

		gSizer7.Add( self.zhushi1, 0, wx.ALL, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"导入hexo博客根目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer9.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.genmulu = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 142,-1 ), wx.DIRP_DEFAULT_STYLE )
		gSizer9.Add( self.genmulu, 0, wx.ALL, 5 )


		gSizer7.Add( gSizer9, 1, wx.EXPAND, 5 )

		self.zhushi = wx.StaticText( self, wx.ID_ANY, u" 注释：详细语法请前往：https://tby-luoyu.github.io", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zhushi.Wrap( -1 )

		gSizer7.Add( self.zhushi, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer7, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.tijiao = wx.Button( self, wx.ID_ANY, u"提交", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tijiao.Bind(wx.EVT_BUTTON,self.updatetext)
		gSizer5.Add( self.tijiao, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.chongxie = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chongxie.Bind(wx.EVT_BUTTON,self.restart)
		gSizer5.Add( self.chongxie, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
	def updatetext(self,event):
		global path
		path=self.wenjianmulidizhi.Path
		genpath=self.genmulu.Path
		tage=self.text_tage.GetValue()
		titles=self.m_textCtrl2.GetValue()
		import work
		work.fpath(path,genpath,titles,tage)
	def restart(self,event):
		sys.exit()



	def __del__( self ):
		pass


