# -*- mode: python ; coding: utf-8 -*-
from kivymd import hooks_path as kivymd_hooks_path
other_files = [('login.kv', '.'), ('gallery.kv', '.'), ('calculator.kv', '.'), ('stopwatch.kv', '.'), ('info.kv', '.'), ('incorrect.kv', '.'), ('assets', 'assets')]
kv_imports = ['kivymd', 'pkg_resources.py2_warn']
block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/Rayhan/PycharmProjects/GUI_Kivy_Python_Revamp'],
             binaries=[],
             datas=other_files,
             hiddenimports=kv_imports,
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='GalleryApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='GalleryApp')
