#from threading import Thread
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def show_logo(filename, device):
    logoImage = Image.new('RGB', (device.width, device.height))
    img_path = os.path.dirname(os.path.realpath(__file__)) + '/../img/'
    try:
        logoImage = Image.open(img_path + filename) #.resize((device.width, device.height), Image.ANTIALIAS)
    except IOError:
        print("Cannot open file %s" % filename)
        pass
    device.display(logoImage)

def load_font(filename, font_size):
    font_path = os.path.dirname(os.path.realpath(__file__)) + '/../fonts/'
    try:
        font = ImageFont.truetype(font_path + filename, font_size)
    except IOError:
        print('font file not found -> using default font')
        font = ImageFont.load_default()
    return font

class Screen(object): # screen base class
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.image = Image.new('RGB', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        self.draw.rectangle((0, 0, self.width - 1, self.height - 1), outline="white", fill="black")

    def Image(self):
        return self.image

class StaticText(Screen):
    def __init__(self, height, width, textlabel, font, center=False, fill="white", bgcolor="black"):
        super(StaticText, self).__init__(height, width)

        self.textlabel = textlabel
        self.textwidth, self.textheight = self.draw.textsize(textlabel, font=font)
        self.center = center
        self.image = Image.new('RGB', (self.textwidth+2, self.textheight+2), bgcolor)   #Need to investigate what are the result of +2 is
        self.draw = ImageDraw.Draw(self.image)
        #self.draw.fontmode = "1"  #no antialiasing
        self.draw.text((0, 0), textlabel, font=font, fill=fill)

    def DrawOn(self, image, position):
        if self.center:
            width, height = image.size
            if self.textwidth < width:
                position = (int(42), position[1])   #original -> "position = (int((width-self.textwidth)/2 + 42), position[1])  "
        image.paste(self.image, position)

class ScrollText(Screen):
    def __init__(self, height, width, textlabel, font):
        super(ScrollText, self).__init__(height, width)

        self.startScrollDelay = 80             #time value
        self.endScrollDelay = 50               #time value
        self.offset = -self.startScrollDelay
        self.scrollSpeed = 1
        self.endScrollMargin = 2               #could not see a difference when set to 4. Maybe a higher number?

        self.textlabel = textlabel
        self.textwidth, self.textheight = self.draw.textsize(textlabel, font=font)
        self.stopPosition =  self.textwidth - width + self.endScrollMargin

        self.image = Image.new('RGB', (self.textwidth + 4, self.textheight + 4))    #Need to investigate what are the result of +4 is
        self.draw = ImageDraw.Draw(self.image)
        self.draw.text((0, 0), textlabel, font=font, fill="white")

    def DrawOn(self, image, position):
        """ Draw the label on (x,y) position of an image with starting at <offset> """
        width, height = image.size

        self.offset += self.scrollSpeed
        if self.offset > self.stopPosition + self.endScrollDelay:
            self.offset = -self.startScrollDelay     #scrolling start is delayed 

        i = 0
        if self.textwidth <= width:                  # center text
            position = (int(42), position[1])     #original-> "position = (int((width-self.textwidth)/2), position[1])"
        elif self.offset <= 0:                       # start position before scrolling
            i = 0
        elif self.offset < self.stopPosition:        # scroll text by offset
            i = int(self.offset)
        else:                                        # stop position when scrolling ended
            i = self.stopPosition

        temp = self.image.crop((i, 0, width+i, self.textheight))
        image.paste(temp, position)

class Bar(Screen):
    def __init__(self, height, width, barHeight, barWidth):
        super(Bar, self).__init__(height, width)

        self.barHeight = barHeight
        self.barWidth = barWidth
        self.filledPixels = 0

        self.image = Image.new('RGB', (self.barWidth, self.barHeight))
        self.draw = ImageDraw.Draw(self.image)

    def SetFilledPercentage(self, percent):
        self.filledPixels = int(self.barWidth*percent/100)

    def DrawOn(self, image, position):
        self.draw.rectangle((0, 0, self.barWidth-1 , self.barHeight-1), outline="white", fill="#2f2f2f")
        self.draw.rectangle((1, 1, self.filledPixels-2 , self.barHeight-2), fill="white")
        image.paste(self.image, position)

