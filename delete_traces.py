import pcbnew
b = pcbnew.GetBoard()
tracks = b.Tracks()
for t in tracks:
    if t.GetWidth() == pcbnew.FromMM(0.20):
        t.SetSelected()
        
pcbnew.Refresh()