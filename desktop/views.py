# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from django.conf import settings
from django.utils.translation import ugettext as _
from routines import default_renderer

#------------------------------------------------------------------------------ 
def view_index(request):
    ""
    content = {}
    return default_renderer(request, "index.html", content)

#------------------------------------------------------------------------------ 
def view_desktop(request):
    ""
    content = {}
    return default_renderer(request, "desktop.html", content)

#------------------------------------------------------------------------------ 
def system_folder(request):
    ""
    items = []
    path = request.GET.get("path", "")
    
    if path == "" or path == "":
        items = [
                 {'title': 'System Setup', 'icon': '/appmedia/imgs/system/system_setup.png', 'action': '/system_folder/?path=setup', 'app': 'yes'}, 
                 {'title': 'Command Prompts', 'icon': '/appmedia/imgs/system/command_prompts.png', 'action': '/system_folder/?path=cmd', 'app': 'yes'},
                 {'title': 'Productivity', 'icon': '/appmedia/imgs/system/folder.png', 'action': '/system_folder/?path=tools', 'app': 'yes'},
                 {'title': 'Minimized Window Viewer', 'icon': '/appmedia/imgs/system/minimized.png', 'action': '/system_folder/?path=minimized', 'app': 'yes'},
                 {'title': 'Shredder', 'icon': '/appmedia/imgs/system/shredder.png', 'action': '/system_folder/?path=shredder', 'app': 'yes'},
                 {'title': 'Drives', 'icon': '/appmedia/imgs/system/drives.png', 'action': '/system_folder/?path=drives', 'app': 'yes'},
                 {'title': 'Startup', 'icon': '/appmedia/imgs/system/startup.png', 'action': '/system_folder/?path=startup', 'app': 'yes'},
                 {'title': 'Games', 'icon': '/appmedia/imgs/system/folder.png', 'action': '/system_folder/?path=games', 'app': 'yes'},
                 ]
    elif path == "cmd":
        items = [
                 {'title': 'OS/2 Full Screen', 'icon': '/appmedia/imgs/cmd/os2fs.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'OS/2 Window', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'DOS Full Screen', 'icon': '/appmedia/imgs/cmd/dos_fs.png', 'action': '/cmd/?cmd=dos_wnd', 'app': 'yes'},
                 {'title': 'DOS Window', 'icon': '/appmedia/imgs/cmd/dos_wnd.png', 'action': '/cmd/?cmd=dos_wnd', 'app': 'yes'},
                 {'title': 'WIN-OS/2 Full Screen', 'icon': '/appmedia/imgs/cmd/win_fs.png', 'action': '/cmd/?cmd=win_wnd', 'app': 'yes'},
                 {'title': 'WIN-OS/2 Window', 'icon': '/appmedia/imgs/cmd/win_wnd.png', 'action': '/cmd/?cmd=win_wnd', 'app': 'yes'},
                 {'title': 'DOS from Drive A:', 'icon': '/appmedia/imgs/cmd/dos_a.png', 'action': '/cmd/?cmd=dos_wnd', 'app': 'yes'},
                 ]
    elif path == "drives":
        items = [
                 {'title': 'Drive A:', 'icon': '/appmedia/imgs/drives/a.png', 'action': 'error', 'dlg': 'yes'},
                 #{'title': 'Drive B:', 'icon': '/appmedia/imgs/drives/a.png', 'action': 'error', 'dlg': 'yes'},
                 {'title': 'Drive C:', 'icon': '/appmedia/imgs/drives/c.png', 'action': '/system_folder/?path=drive_c', 'app': 'yes'},
                 {'title': 'Drive D:', 'icon': '/appmedia/imgs/drives/c.png', 'action': '/system_folder/?path=drive_d', 'app': 'yes'},
                 {'title': 'Drive E:', 'icon': '/appmedia/imgs/drives/e.png', 'action': 'error', 'dlg': 'yes'},
                 ]
    elif path == "drive_c":
        items = [
                 {'title': 'OS/2', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_c_os2'},
                 {'title': 'PSFONTS', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_c_psfonts'},
                 {'title': 'NOWHERE', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_c_nowhere'},
                 {'title': 'SPOOL', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_c_spool'},
                 {'title': 'DESKTOP', 'icon': '/appmedia/imgs/system/desktop.png', 'action': '?path=drive_c_desktop'},
                 {'title': 'CONFIG.SYS', 'icon': '/appmedia/imgs/files/text_editor.png', 'action': '/app/text_editor/?path=config.sys', 'app': 'yes'},
                 ]
    elif path == "drive_c_os2":
        items = [
                 {'title': 'APPS', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'DLL', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'HELP', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'SYSTEM', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'ETC', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'INSTALL', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'BOOK', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'MDOS', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'DRIVERS', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'BOOT', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'POINTERS', 'icon': '/appmedia/imgs/system/folder.png'},
                 
                 {'title': 'KEYBOARD.DCP', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'INISYS.RC', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'HPFS.IFS', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'INI.RC', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'WIN_30.RC', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'VIDEO.CFG', 'icon': '/appmedia/imgs/files/default.gif'},
                 {'title': 'E.EXE', 'icon': '/appmedia/imgs/files/text_editor.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 
                 {'title': 'FORMAT.COM', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'HELP.CMD', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'CHKDSK.COM', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'FIND.EXE', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'CMD.EXE', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'BOOT.COM', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'PRINT.COM', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 {'title': 'MORE.COM', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 
                 ]
    elif path == "drive_c_desktop":
        items = [
                 {'title': 'OS/2 System', 'icon': '/appmedia/imgs/system_folder.png', 'action': '/system_folder/', 'app': 'yes'}, 
                 {'title': 'Information', 'icon': '/appmedia/imgs/help.png', 'action': '/appmedia/help/desktop.html', 'app': 'yes'},
                 {'title': 'Virtual PC', 'icon': '/appmedia/imgs/system/minimized.png', 'action': '/', 'app': 'yes'},
                 {'title': 'WebExplorer', 'icon': '/appmedia/imgs/web/explore.gif', 'action': '/webexplorer/', 'app': 'yes'},
                 {'title': 'WIN-OS/2 Window', 'icon': '/appmedia/imgs/cmd/win_wnd.png', 'action': '/cmd/?cmd=win_wnd', 'app': 'yes'},              
                 {'title': 'Solitaire', 'icon': '/appmedia/imgs/files/sol.jpg', 'action': 'http://www.webolog.com/online_games/solitaire/loaderwm.swf', 'app': 'yes'},
                 ]
    elif path == "drive_d":
        items = [
                 {'title': 'PROJECTS', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_d_projects'},
                 {'title': 'PYTHON', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_d_python'},
                 ]
    elif path == "drive_d_projects":
        items = [
                 {'title': 'OS2ONLINE', 'icon': '/appmedia/imgs/system/folder.png', 'action': '?path=drive_d_projects_os2online'},
                 ]
    elif path == "drive_d_projects_os2online":
        items = [
                 {'title': 'APPMEDIA', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': 'DESKTOP', 'icon': '/appmedia/imgs/system/folder.png'},
                 {'title': '__INIT__.PY', 'icon': '/appmedia/imgs/files/notepad.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 {'title': 'SETTINGS.PY', 'icon': '/appmedia/imgs/files/notepad.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 {'title': 'URLS.PY', 'icon': '/appmedia/imgs/files/notepad.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 ]
    elif path == "drive_d_python":
        items = [
                 {'title': 'DLLS', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'DOC', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'INCLUDE', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'LIB', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'LIBS', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'SCRIPTS', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'TCL', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'TOOLS', 'icon': '/appmedia/imgs/system/folder.png', 'action': ''},
                 {'title': 'LICENSE.TXT', 'icon': '/appmedia/imgs/files/text_editor.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 {'title': 'NEWS.TXT', 'icon': '/appmedia/imgs/files/text_editor.png', 'action': '/app/text_editor/', 'app': 'yes'},
                 {'title': 'PYTHON.EXE', 'icon': '/appmedia/imgs/cmd/os2wnd.png', 'action': '/cmd/?cmd=os2wnd', 'app': 'yes'},
                 ]
    elif path == "setup":
        items = [
                 {'title': 'System Clock', 'icon': '/appmedia/imgs/setup/clock.png', 'action': '?path=setup'},
                 {'title': 'Keyboard', 'icon': '/appmedia/imgs/setup/keyboard.png', 'action': '?path=setup'},
                 {'title': 'Selective Install', 'icon': '/appmedia/imgs/setup/install.png', 'action': '?path=setup'},
                 {'title': 'Mouse', 'icon': '/appmedia/imgs/setup/mouse.png', 'action': '?path=setup'},
                 {'title': 'Device Driver Install', 'icon': '/appmedia/imgs/setup/install.png', 'action': '?path=setup'},
                 {'title': 'System', 'icon': '/appmedia/imgs/setup/system.png', 'action': '?path=setup'},
                 {'title': 'Country', 'icon': '/appmedia/imgs/setup/country.png', 'action': '?path=setup'},
                 {'title': 'Sound', 'icon': '/appmedia/imgs/setup/sound.png', 'action': '?path=setup'},
                 {'title': 'Font Palette', 'icon': '/appmedia/imgs/setup/font.png', 'action': '?path=setup'},
                 {'title': 'Mixed Color Palette', 'icon': '/appmedia/imgs/setup/palette.png', 'action': '?path=setup'},
                 {'title': 'Solid Color Palette', 'icon': '/appmedia/imgs/setup/palette.png', 'action': '?path=setup'},
                 {'title': 'Power', 'icon': '/appmedia/imgs/setup/power.png', 'action': '?path=setup'},
                 {'title': 'WIN-OS/2 Setup', 'icon': '/appmedia/imgs/setup/win.png', 'action': '/cmd/?cmd=win_wnd', 'app': 'yes'},
                 
                 ]
    elif path == "shredder":
        items = [
                 {'title': 'Old documents', 'icon': '/appmedia/imgs/files/folder.png', 'action': ''},
                 {'title': 'Temp', 'icon': '/appmedia/imgs/files/notepad.png', 'action': ''},
                 ]
    elif path == "tools":
        items = [
                 {'title': 'OS/2 System Editor', 'icon': '/appmedia/imgs/files/text_editor.png', 'action': 'http://www.editpad.org/', 'app': 'yes'}, #/app/text_editor/
                 {'title': 'Enhanced Editor', 'icon': '/appmedia/imgs/files/notepad.png', 'action': 'http://shrib.com/', 'app': 'yes'},
                 {'title': 'Lotus Smart Suite', 'icon': '/appmedia/imgs/files/lotus.png', 'action': 'http://apps.live-documents.com/docs/', 'app': 'yes'},
                 {'title': 'Twitter', 'icon': '/appmedia/imgs/files/twitter.png', 'action': '/app/twitter/', 'app': 'yes'},
                 ]
    elif path == "games":
        items = [
                 {'title': 'Chess', 'icon': '/appmedia/imgs/files/chess.png', 'action': 'http://cdn.sparkchess.com/sparkchess.swf', 'app': 'yes'},
                 {'title': 'Solitaire', 'icon': '/appmedia/imgs/files/sol.jpg', 'action': 'http://www.webolog.com/online_games/solitaire/loaderwm.swf', 'app': 'yes'},
                 
                 ]

    content = {
               "items": items
               }
    return default_renderer(request, "folders/system_folder.html", content)

#------------------------------------------------------------------------------ 
def information(request):
    ""
    content = {}
    return default_renderer(request, "folders/information.html", content)

#------------------------------------------------------------------------------ 
def tutorial(request):
    ""
    content = {}
    return default_renderer(request, "programs/tutorial.html", content)

#------------------------------------------------------------------------------ 
def command_line(request):
    ""
    cmd = request.GET.get("cmd", "os2wnd")
    content = {}
    return default_renderer(request, "programs/cmd_%s.html" % cmd, content)

#------------------------------------------------------------------------------ 
def webexplorer(request):
    ""
    content = {}
    return default_renderer(request, "programs/webexplorer.html", content)

#------------------------------------------------------------------------------
def run_app(request, app_name):
    "Run application"
    text = ""
    path = request.GET.get("path", "")
    if path == "config.sys":
        text = """
IFS=C:\OS2\HPFS.IFS /CACHE:64 /CRECL:4
PROTSHELL=C:\OS2\PMSHELL.EXE
SET USER_INI=C:\OS2\OS2.INI
SET SYSTEM_INI=C:\OS2\OS2SYS.INI
SET OS2_SHELL=C:\OS2\CMD.EXE
SET AUTOSTART=PROGRAMS,TASKLIST,FOLDERS,CONNECTIONS,LANCHPAD
SET RUNWORKPLACE=C:\OS2\PMSHELL.EXE
SET COMSPEC=C:\OS2\CMD.EXE
LIBPATH=C:\OS2\DLL;C:\OS2\MDOS;
PATH=C:\OS2;C:\OS2\SYSTEM;C:\OS2\MDOS\WINOS2;C:\OS2\INSTALL;C:\;
"""
    content = {
               "text": text,
               }
    return default_renderer(request, "programs/%s.html" % app_name, content)

#------------------------------------------------------------------------------ 
def ajax_query(request, query_id):
    "AJAX requests dispatcher"
    from desktop_items import *
    return eval(query_id + '_data(request)')

#------------------------------------------------------------------------------ 
