# -*- mode: python -*-

block_cipher = None


a = Analysis(['typing_collection.py'],
             pathex=['/Users/baidu/Documents/\xe6\xaf\x95\xe4\xb8\x9a\xe8\xae\xbe\xe8\xae\xa1/typing_stroken'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='typing_collection',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='typing_collection')
