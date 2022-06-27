import wx

import backend


# Create a button event
def press_button(event):
    meters = float(input_box.GetValue())
    result_out.SetLabel(str(backend.converter(meters)))


# Start the application
app = wx.App()
frame = wx.Frame(parent=None, title='Meters to Feet Converter')
panel = wx.Panel(frame)
sizer = wx.GridBagSizer()

# Create inputs and outputs fields
input_box = wx.TextCtrl(panel)
input_meters = wx.StaticText(panel, label='Meters : ')  # create panel and add input widget
result_box = wx.StaticText(panel, label='Feet : ')
result_out = wx.StaticText(panel, label='')
button = wx.Button(panel, label='Converter')
button.Bind(wx.EVT_BUTTON, press_button)
# Adjust the inputs and outputs
sizer.Add(input_meters, (0, 0))
sizer.Add(input_box, (0, 1))
sizer.Add(result_box, (1, 0))
sizer.Add(result_out, (1, 1))
sizer.Add(button, (2, 0))

# fit the panel and frame
panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)

# Show the application
frame.Show()
app.MainLoop()
