# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['boardz.py', 'chuli.py', 'data_eeg.py', 'feature.py', 'game_GUI.py', 'model_GUI.py', 'platform.ico', 'press1.py', 'processing.py', 'tezhengtiqu.py'],
             pathex=['F:\\Vscode\\PyProject\\YHA\\ssvep'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='boardz',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='1.py')
