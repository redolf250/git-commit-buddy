# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Include the resources directory and other files
datas = [
    ('D:/commit-buddy/app/icon.ico', '.'),
    ('D:/commit-buddy/app/resources/assert/', 'resources/assert/'),
    ('./views/*.ui', 'views'),
    ('D:/commit-buddy/app/database/*.json', 'database'),
    ('D:/commit-buddy/app/database/*.txt', 'database')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['pydantic', 'pydantic-core', 'pydantic.deprecated.decorator'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GitCommitBuddy',
    debug=True,
    console=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    onefile=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:/commit-buddy/app/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GitCommitBuddy',
)