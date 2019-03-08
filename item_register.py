import ui
import barcode
import time

def getCode():
    code = barcode.main()
    return code
    
def button_tapped(sender):
    code = getCode()
    if code:
        v['textfield1'].text = code
        v['textfield2'].begin_editing()
        
def next_field(sender):
    next = int(sender.name[-1]) + 1
    v[f'textfield{next}'].begin_editing()

class myDelegate(object):
    def textfield_should_return(self, tf):
        next_field(tf)

v = ui.load_view()
for i in range(1,4):
    v[f'textfield{i}'].delegate = myDelegate()
v.present(orientations=['portrait'])
