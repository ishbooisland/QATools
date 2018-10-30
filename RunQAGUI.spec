# -*- mode: python -*-
a = Analysis(['RunQAGUI.py'],
             pathex=['C:\\Users\\Darrin\\PycharmProjects\\QATools'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RunQAGUI.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
