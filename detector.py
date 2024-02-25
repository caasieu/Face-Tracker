import cv2
import filters 
from managers import WindowManager, CaptureManager

class Detector(object):
	def __init__(self):
		self._windowManager = WindowManager('Cameo', self.onKeypress)
		self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
		self._curveFilter = filters.BGRPortraCurveFilter()

	def run(self):
		""" Run the main loop. """
		self._windowManager.createWindow()
		while self._windowManager.isWindowCreated:
			self._captureManager.enterFrame()
			frame = self._captureManager.frame

			filters.strokeEdges(frame, frame)
			self._curveFilter.apply(frame, frame)

			self._captureManager.exitFrame()
			self._windowManager.processEvents()

	def onKeypress(self, keycode):
		""" 
			+ Handle a keypress + 
			space  -> Screenshot
			tab 	 -> Start/Stop recording 
			escape -> Quit 

		"""

		if keycode == 32: # space
			self._captureManager.writeImage('screenshot.png')
		elif keycode == 9: # tab 
			if not self._captureManager.isWritingVideo:
				self._captureManager.startWritingVideo('screencast.avi')
			else: 
				self._captureManager.stopWritingVideo()
		elif keycode == 27: # Esc
			self._windowManager.destroyWindow()

if __name__=='__main__':
	#filters.strokeEdges(cv2.imread('images/1.jpg'), '1_b.jpg')
	Detector().run()
