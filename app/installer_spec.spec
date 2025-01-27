# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Adjust paths to be Unix-compatible
datas = [
    ('icon.ico', '.'),  # Fixed the syntax error here, use .ico or convert to .png if needed
    ('./resources/assert/', 'resources/assert/'),
    ('./views/*.ui', 'views'),
    ('./database/*.json', 'database'),
    ('./database/*.txt', 'database'),
]

a = Analysis(
    ['main.py'],
    pathex=['.'],  # Add the current directory to the path
    binaries=[],
    datas=datas,
    hiddenimports=['pydantic', 'pydantic-core', 'pydantic.deprecated.decorator'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],  # If not using PySide6
    win_no_prefer_redirects=False,  # Windows-specific, safe to leave as is
    win_private_assemblies=False,  # Windows-specific, safe to leave as is
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
    debug=False,  # Set to False unless debugging
    console=False,  # Set to False if a GUI application
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    onefile=False,  # Set to True if a single executable is desired
    disable_windowed_traceback=False,
    target_arch='ppc64',
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'  # Use Unix-compatible icon format, or change to .png if needed
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

