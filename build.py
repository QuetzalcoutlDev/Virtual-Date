import PyInstaller.__main__

PyInstaller.__main__.run([
	'--noconfirm',
	'settings.spec',
	'main.py'
])
