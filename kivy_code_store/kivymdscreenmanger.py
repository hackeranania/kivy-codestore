MDNavigationLayout:
	MDNavigationDrawer:
		MDRaisedButton:
			on_press:screen_manage.current = '2'
	ScreenManager:
		id : screen_manage
		Screen:
			name : '1'
			MDLabel:
				text:'number 1'
				pos_hint:{'center_y':.5,'center_x':.5}
		Screen:
			name : '2'
			MDLabel:
				text:'number 2'	
