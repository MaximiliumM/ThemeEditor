# coding: utf-8
import ui,colorsys

class ColorPicker(ui.View):
	def __init__(self, *args,**kwargs):
		ui.View.__init__(self,*args,**kwargs)
		self.history=[]  #future...keep track of recent colors
		self.current=(0.3,0.2,0.5) 
		self.rgb=colorsys.hsv_to_rgb(self.current[0], self.current[1], self.current[2])
		self.N=16
		self.Nb=18
		
	def set_rgb(self, r, g, b):
		self.current = colorsys.rgb_to_hsv(r, g, b)
		self.set_needs_display()
		
	def draw(self):
			self.y = 0
			square_size=max(self.width,self.height)
			N=self.N
			Nb=self.Nb
			dx=square_size*1.0/(N+3)
			dxb=N*dx/Nb
			h,s,v=self.current
			i0,j0,k0=(round(c*N) for c in self.current)
	
			k0=round(self.current[2]*Nb)
			#draw H/S grid
			for i in range(0,N+1):
				for j in range(0,N):			
					ui.set_color(colorsys.hsv_to_rgb(i*1.0/N,j*1.0/N,v))
					ui.set_blend_mode(ui.BLEND_NORMAL)
					ui.fill_rect(round(i*dx),round(j*self.height/Nb),round(dx),round(self.height+1/Nb))
	
			#draw V slider
			for k in range(0,Nb):
				ui.set_color(colorsys.hsv_to_rgb(h,s,k*1./Nb))
				ui.set_blend_mode(ui.BLEND_NORMAL)
				ui.fill_rect(round((N+1.5)*dx),round(k*self.height/Nb),round(dx),round(self.height/Nb+0.5))
				
			#highlight selection
			if all([c>=0 for c in self.current]):
				# h,s selection
				ui.set_color(colorsys.hsv_to_rgb(h-0.1,s,1-0.5*v))
				p=ui.Path.rect(i0*dx,j0*(self.height+10)/Nb,dx,self.height/Nb)
				p.line_width=4
				p.stroke()
				
				# v selection
				ui.set_color(colorsys.hsv_to_rgb(h,s,1-0.5*(0.2+v)))
				p=ui.Path.rect((N+1.5)*dx,k0*(self.height-10)/Nb,dx,self.height/Nb)
				p.line_width=4
				p.stroke()

			self.rgb=colorsys.hsv_to_rgb(self.current[0], self.current[1], self.current[2])			
			r, g, b = self.rgb

			self.superview.superview.set_colorView(r, g, b)
				

	def touch_began(self,touch):
		self.touch_moved(touch)
	def touch_moved(self,touch):
			#set color
			#  self dx=size/(N+2)
			square_size=max(self.width,self.height)
			N=self.N
			Nb=self.Nb
			dx=square_size*1.0/(N+2)
			dxb=N*dx*1.0/self.height+1
			h,s,v=self.current
			if touch.location[0]>=dx*(N+0.5) and touch.location[1]<=193:
				v=round(touch.location[1]/10)/Nb
			elif touch.location[1]<=self.height and touch.location[0]<=dx*(N+1):
				# Horizontal Position Relative to Finger
				h=round(touch.location[0]/(dx+0.1))/N
				# Vertical Position Relative to Finger
				s=round(touch.location[1]/10)/N 
			clip=lambda x:min(max(x,0),1)
			self.current=(clip(h),clip(s),clip(v))
			self.set_needs_display()

# DEBUG
#v = ColorPicker(frame=(0,0,360,576))
#v.present()
