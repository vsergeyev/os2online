# -*- coding: utf-8 -*-
import json

from flask import jsonify
from flask import render_template, request, url_for, redirect
import time, random

#------------------------------------------------------------------------------ 
def get_desktop_items_data():
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
    #return jsonify(items=items)
    return json.dumps(items)

#------------------------------------------------------------------------------ 
def get_lanchpad_data():
    return render_template("lanchpad.html")

#------------------------------------------------------------------------------ 
def get_window_data():
    "Returns rendered window with iframe inside"
    title = request.args.get("title", "")
    src = request.args.get("src", "")
    width = request.args.get("width", "634")
    height = request.args.get("height", "450")
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
    return render_template(template, **content)

#------------------------------------------------------------------------------ 
def get_dialog_data():
    "Returns rendered dialog"
    dlg = request.args.get("dlg", "")
    title = request.args.get("title", "")
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
    return render_template(template, **content)

#------------------------------------------------------------------------------ 
