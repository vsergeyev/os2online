# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from routines import default_renderer
import time, random

#------------------------------------------------------------------------------ 
def get_desktop_items_data(request):
    """
    Returns items for Desktop in JSON array:
    title
    
    """
    items = [
             {'title': 'OS/2 System', 'icon': '/appmedia/imgs/system_folder.png', 'left': '0px', 'top': '40px', 'action': '/system_folder/'}, 
             {'title': 'Information', 'icon': '/appmedia/imgs/help.png', 'left': '0px', 'top': '120px', 'action': '/appmedia/help/desktop.html'},
             {'title': 'Virtual PC', 'icon': '/appmedia/imgs/system/minimized.png', 'left': '0px', 'top': '200px', 'action': '/'},
             {'title': 'WebExplorer', 'icon': '/appmedia/imgs/web/explore.gif', 'left': '0px', 'top': '280px', 'action': '/webexplorer/'},
             {'title': 'WIN-OS/2 Window', 'icon': '/appmedia/imgs/cmd/win_wnd.png', 'left': '0px', 'top': '360px', 'action': '/cmd/?cmd=win_wnd', 'app': 'yes'},              
             {'title': 'Solitaire', 'icon': '/appmedia/imgs/files/sol.jpg', 'left': '0px', 'top': '440px', 'action': 'http://www.webolog.com/online_games/solitaire/loaderwm.swf', 'app': 'yes'},
             ]
    
    content = simplejson.dumps(items)
    return HttpResponse(content)

#------------------------------------------------------------------------------ 
def get_lanchpad_data(request):
    ""
    content = {
               }
    return default_renderer(request, "lanchpad.html", content)

#------------------------------------------------------------------------------ 
def get_window_data(request):
    "Returns rendered window with iframe inside"
    title = request.GET.get("title", "")
    src = request.GET.get("src", "")
    width = request.GET.get("width", "634")
    height = request.GET.get("height", "450")
    win_id = int(time.time())
    
    template = "pm/base_window.html"
    if src.find("win_") != -1:
        template = "pm/win_window.html"
        #title = "Program Manager"
    
    content = {
               "title": title,
               "src": src,
               "win_id": win_id,
               "wnd_left": random.randint(120, 300),
               "wnd_top": random.randint(20, 100),
               "width": width,
               "height": height,
               }
    return default_renderer(request, template, content)

#------------------------------------------------------------------------------ 
def get_dialog_data(request):
    "Returns rendered dialog"
    dlg = request.GET.get("dlg", "")
    title = request.GET.get("title", "")
    win_id = int(time.time())
    
    template = "dialogs/%s.html" % dlg
    
    content = {
               "title": title,
               "dlg": dlg,
               "win_id": win_id,
               "wnd_left": 400,
               "wnd_top": 300,
               "width": 290,
               "height": 150,
               }
    return default_renderer(request, template, content)

#------------------------------------------------------------------------------ 
