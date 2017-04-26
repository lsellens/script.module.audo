#
import xbmc
import xbmcaddon

__scriptname__ = "audo"
__author__     = "lsellens"
__url__        = "https://github.com/lsellens/xbmc.addons"
__icon__   = xbmcaddon.Addon(id='script.module.audo').getAddonInfo('icon')

#try to get service addon info or send notification to install it.
try:
    __addon__      = xbmcaddon.Addon(id='script.service.audo')
    __addonpath__  = __addon__.getAddonInfo('path')
except:
    xbmc.executebuiltin("XBMC.Notification(audo, Install audo service!, 15000, %s)" % __icon__)
    xbmc.log('AUDO: Could not detect service addon:', level=xbmc.LOGERROR)
    exit()

if __name__ == '__main__':
    
    # Shutdown audo
    __addon__.setSetting(id='SHUTDOWN', value='true')
    
    # Open settings dialog
    __addon__.openSettings()
    
    # Restart audo
    __addon__.setSetting(id='SHUTDOWN', value='false')
