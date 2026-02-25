import pcbnew
for v in pcbnew.GetBoard().GetTracks():
    if type(v) is pcbnew.PCB_VIA and v.GetWidth() == pcbnew.FromMM(0.6):
        v.SetSelected()
        
pcbnew.Refresh()