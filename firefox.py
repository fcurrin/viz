# An example app module.
# Play tone when Notepad is opened

import appModuleHandler
import tones
import api
import treeInterceptorHandler
import browseMode
import textInfos

class AppModule(appModuleHandler.AppModule):
	
	def event_gainFocus(self, obj, nextHandler):
		log_file = open("C:\\Users\\Flannery\\AppData\\Roaming\\nvda\\appModules\\log.txt", "w")
		log_file.write("")
		log_file.close()
		log_file = open("C:\\Users\\Flannery\\AppData\\Roaming\\nvda\\appModules\\log.txt", "a")
		nav = api.getNavigatorObject()
		navs = []
		focus = api.getFocusObject()
		buffer = focus.treeInterceptor
		#log_file.write(str(buffer) + "\n")
		#log_file.write(str(type(buffer)) + "\n")
		
		if (isinstance(buffer, treeInterceptorHandler.TreeInterceptor)):
			info = buffer.makeTextInfo(textInfos.POSITION_ALL)
			chunks = info.getTextInChunks(textInfos.UNIT_WORD)
			for chunk in chunks:
				log_file.write(str(chunk) + ",10\n")
			log_file.close()
        '''
        while (nav != None):
			log_file.write(str(nav.basicText) + "\n")
			for item in nav.children:
				log_file.write(str(item.basicText) + "\n")
			nav = nav.next
        '''