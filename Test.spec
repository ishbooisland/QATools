# -*- mode: python -*-
a = Analysis(['Test.py'],
             pathex=['C:\\Users\\Darrin\\PycharmProjects\\untitled'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Test.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
