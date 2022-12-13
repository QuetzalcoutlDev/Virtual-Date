import platform

windows = False
mac = False
linux = False

if platform.system() == "Windows":
    windows = True

elif platform.mac_ver()[0]:
    mac = True

elif platform.system() == "Linux":
    linux = True

icon=None

if windows == True:

    icon="./icon.ico"

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=None,
    datas=[],
    hiddenimports=[],
    hookspath=None,
    hooksconfig={},
    runtime_hooks=None,
    excludes=None,
    cipher=block_cipher
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    icon=icon,
    name='date',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
