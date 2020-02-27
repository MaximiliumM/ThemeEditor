#!python3

import ui
import os
import re
import editor
import objc_util
import ImageColor
import plistlib
import dialogs
from colorPicker import ColorPicker

TWITTERRIFIC_PATH = '/private/var/mobile/Library/Mobile Documents/iCloud~com~iconfactory~Blackbird/Documents/Themes/%s'

class MyTableViewDataSource(ui.ListDataSource):
	def __init__(self, data):
		super().__init__(data)
		self.data = data
		
	def tableview_delete(self,tableview, section,row):
		remove_theme(self.data[row])
		self.data.remove(self.data[row])
		return

class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		pass
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		isHexCode = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', replacement)
		
		if (range[0] == 0 and isHexCode):
			return True
		elif range[0] == 0:
			return False
		else:
			isHexCompliant = re.search(r'^[0-9a-fA-F]$', replacement)
		
			if (isHexCompliant or replacement == '' or replacement == '#') and not(len(textfield.text) + len(replacement)) > 7:
				return True
			else:
				return False
				
	def textfield_did_change(self, textfield):
		if textfield.text == '':
			textfield.text = '#'
		elif '##' in textfield.text:
			textfield.text = textfield.text.replace('##', '#')
		elif len(textfield.text) == 7:
			rgb = ImageColor.getrgb(textfield.text)
			r, g, b = rgb
			
			v = textfield.superview['groupView']
			
			v['slider1'].value = float(r) / 255
			v['slider2'].value = float(g) / 255
			v['slider3'].value = float(b) / 255
			
			v.superview.slider_action(v['slider1'])
			
		pass

class ThemeEditorView(ui.View):
	def save_changes(self):
		plistlib.writePlist(self.data, self.dir)
		
	def set_colorView(self, r, g, b):
		v = self
		v['view1'].background_color = (r, g, b)
		
		self.slider1.value = r
		self.slider2.value = g
		self.slider3.value = b
				
		self.textField.text = '#%.02X%.02X%.02X' % (int(r*255), int(g*255), int(b*255))
			
	def set_color(self, sender):
		# Get the root view:
		v = sender.superview.groupView
		# Get the sliders:
		r = int(255 * v['slider1'].value)
		g = int(255 * v['slider2'].value)
		b = int(255 * v['slider3'].value)
		
		self.data[self.tableView.data_source.items[self.tableView.data_source.selected_row]] = '%d:%d:%d' % (r, g, b)
		
		self.save_changes()
	
	def switch_action(self, sender):
		self.data[self.tableView.data_source.items[self.tableView.data_source.selected_row]] = sender.value
		self.save_changes()
	
	def slider_action(self, sender):
		# Get the root view:
		v = sender.superview
		# Get the sliders:
		r = v['slider1'].value
		g = v['slider2'].value
		b = v['slider3'].value
		
		self.pickerView.set_rgb(r, g, b)
		self.set_colorView(r, g, b)
		
		
	def cell_tapped(self, sender):
		v = self.groupView
		self.switch.hidden = True
		self.setColorButton.enabled = True
		
		selectedAttribute = sender.items[sender.selected_row]
		attrValue = self.data[selectedAttribute]
		
		if isinstance(attrValue, int):
			self.switch.hidden = False
			self.switch.value = attrValue
			self.setColorButton.enabled = False
		else:
			r, g, b = [float(x) / 255 for x in attrValue.split(':')]
			self.pickerView.set_rgb(r, g, b)
			self.set_colorView(r, g, b)
			
	def set_color_mode(self, sender):
		if sender.selected_index == 0:
			self.pickerView.hidden = True
			self.groupView['slider1'].hidden = False
			self.groupView['slider2'].hidden = False
			self.groupView['slider3'].hidden = False
		else:
			self.pickerView.hidden = False
			self.groupView['slider1'].hidden = True
			self.groupView['slider2'].hidden = True
			self.groupView['slider3'].hidden = True
		
		
	def setup(self, theme):
		self.dir = TWITTERRIFIC_PATH % theme
	
		with open(self.dir, 'rb') as f:
			self.data = plistlib.readPlist(f)
		
		dataSource = ui.ListDataSource(sorted(self.data.keys()))
		dataSource.action = self.cell_tapped
		dataSource.delete_enabled = False
		
		v = self
				
		self.tableView = v['tableview1']
		self.tableView.data_source = dataSource
		self.tableView.delegate = dataSource
		
		self.switch = v['switch1']
		self.switch.action = self.switch_action
		self.switch.hidden = True
		
		self.setColorButton = v['button1']
		self.setColorButton.action = self.set_color
		
		self.groupView = v['groupView']
		
		self.pickerView = ColorPicker(frame=(self.groupView.frame))
		self.pickerView.autoresizing = 'WH'
		self.groupView.add_subview(self.pickerView)
		
		self.slider1 = self.groupView['slider1']
		self.slider1.action = self.slider_action
		
		self.slider2 = self.groupView['slider2']
		self.slider2.action = self.slider_action
		
		self.slider3 = self.groupView['slider3']
		self.slider3.action = self.slider_action
		
		self.colorModeSegmentedControl = v['segmentedcontrol1']
		self.colorModeSegmentedControl.action = self.set_color_mode
		self.colorModeSegmentedControl.selected_index = 1
		self.set_color_mode(self.colorModeSegmentedControl)
		
		self.textField = v['textfield1']
		self.textField.delegate = MyTextFieldDelegate()
		
		self.tableView.data_source.tableview_did_select(self.tableView, 0, 0)
		
def loadTableView():
	currentTabDir = TWITTERRIFIC_PATH % segmentedControl.segments[segmentedControl.selected_index]

	dataSource = MyTableViewDataSource(os.listdir(currentTabDir))

	tableView.data_source = dataSource
	tableView.data_source.action = select_theme
	tableView.delegate = dataSource
	
	tableView.reload()
	
@ui.in_background 			
def new_theme(sender):
	path = editor.get_path()
	dir = os.path.dirname(path)
	
	with open(dir + '/Sample.twitterrifictheme', 'rb') as f:
		data = plistlib.readPlist(f)
		
	themeName = dialogs.input_alert('Theme Name')
	
	if len(themeName) != 0:
		currentTabDir = TWITTERRIFIC_PATH % segmentedControl.segments[segmentedControl.selected_index]
		
		writePath = currentTabDir + '/%s.twitterrifictheme' % themeName
		plistlib.writePlist(data, writePath)
	else:
		dialogs.alert('Invalid Name', button1='Ok', hide_cancel_button=True)
	
	loadTableView()
	
	
def select_theme(sender):
	v = ui.load_view('themeEditor')
	themeName = sender.items[sender.selected_row]
	v.setup(segmentedControl.segments[segmentedControl.selected_index] + '/' + themeName)
	v.name = themeName.replace('.twitterrifictheme', '')
	nav.push_view(v)
	

def change_folder(sender):
	loadTableView()
	
def remove_theme(file):
	currentTabDir = TWITTERRIFIC_PATH % segmentedControl.segments[segmentedControl.selected_index]
	os.remove(currentTabDir + '/' + file)
	loadTableView()
	

v = ui.load_view()
segmentedControl = v['segmentedcontrol1']
tableView = v['tableview1']

loadTableView()

nav = ui.NavigationView(v)
nav.name = "My Themes"
nav.title_color = '#636363'

nav.present("fullscreen")


