# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/gns3/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gns3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
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
    name='gns3',
)
app = BUNDLE(
    coll,
    name='GNS3.app',
    icon='icon.icns',
    bundle_identifier='net.gns3',
    version='VER',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHumanReadableCopyright': 'GNU General Public License (GPL), GNS3 Technologies Inc.',
        'NSAppleScriptEnabled': False,
        'CFBundleGetInfoString': 'GNS3, Graphical Network Simulator',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'GNS3 Project',
                'CFBundleTypeExtensions': ['gns3'],
                'CFBundleTypeRole': 'Editor'
            },
            {
                'CFBundleTypeName': 'GNS3 Portable Project',
                'CFBundleTypeExtensions': ['gns3project', 'gns3p'],
                'CFBundleTypeRole': 'Editor'
            },
            {
                'CFBundleTypeName': 'GNS3 Appliance',
                'CFBundleTypeExtensions': ['gns3appliance', 'gns3a'],
                'CFBundleTypeRole': 'Viewer'
            }
        ]
    },
)
