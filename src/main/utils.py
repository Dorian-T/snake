import os
import sys


def resource_path(relative_path) -> str:
	"""
	Get the absolute path to the resource, works for dev and for PyInstaller.
	
	Args:
		relative_path (str): The relative path.
		
	Returns:
		str: The absolute path.
	"""

	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except AttributeError:
		base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

	return os.path.join(base_path, relative_path)