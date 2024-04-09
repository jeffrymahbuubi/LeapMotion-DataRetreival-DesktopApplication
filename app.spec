# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=['./leapc-cffi', './leapc-python-api'],
    binaries=[],
    datas=[('leapc-cffi/*', '.'), ('leapc-python-api/*', '.'), ('images/*', 'images')],
    hiddenimports=['leapmotion_ver3', 'data_management_ui', 'leapmotion_logic', 'PySide6.QtWidgets', 'PySide6.QtCore', 'PySide6.QtGui', 'PySide6'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Leap Motion Gemini V5.17.1',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Leap Motion Gemini V5.17.1',
)
