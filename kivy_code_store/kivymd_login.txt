from kivymd.app import MDApp
from kivy.lang import Builder


	

class java(MDApp):
	def build(self):
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.theme_style = "Dark"
		return Builder.load_file('java.kv')
	def login(self):
		self.root.ids.user.text = ''
		self.root.ids.password.text = ''
		self.root.ids.label.text = 'to many request login after 2 min'
		self.root.ids.label.font_size = 15
	def clear(self):
		self.root.ids.user.text = ''
		self.root.ids.password.text = ''

java().run()




Screen : 
	MDCard:
		size_hint: None , None
		size : 300,400
		pos_hint : {"center_x": .5 , "center_y": .5}
		elevation : 10
		padding : 25
		spacing : 25
		orientation : 'vertical'
		MDLabel: 
			id : label 
			text : 'WELCOME '
			font_size : 40
			halign : 'center'
			size_hint_y : None
			height : self.texture_size [1]
			padding_y : 20
		MDTextFieldRound :
			id : user
			hint_text : 'username'
			size_hint_x : None
			width : 200
			font_size : 19
			pos_hint :  {'center_x':.5}	
			password: False
		MDTextFieldRound :
			id : password
			hint_text : 'password'
			size_hint_x : None
			width : 200
			font_size : 19
			pos_hint :  {'center_x':.5}	
			password: True	
		MDRectangleFlatButton :
			
			text : 'signin'
			font_size : 19
			pos_hint :  {'center_x':.5}	
			on_press : app.login ()	
		MDRectangleFlatButton :
			text : 'clear'
			font_size : 19
			pos_hint :  {'center_x':.5}	
			on_press : app.clear()	
				