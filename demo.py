import unittest
from fishrob import fishrob


debian_package_file = """
Package: abs-guide
Version: 6.6-1
Installed-Size: 4121
Maintainer: Sandro Tosi <morph@debian.org>
Architecture: all
Recommends: lynx | www-browser
Description: The Advanced Bash-Scripting Guide
Homepage: http://www.tldp.org/LDP/abs/html/
Description-md5: c70e528b8b624e5738bdbd1b89e8b349
Tag: devel::doc, devel::examples, made-of::html, role::documentation
Section: non-free/doc
Priority: optional
Filename: pool/non-free/a/abs-guide/abs-guide_6.6-1_all.deb
Size: 1109664
MD5sum: d132e879652e3bd16542f3bcb5cfd51f
SHA1: 1d8d29e3d91203184691cc1a06d15e5d82b4a98a
SHA256: d688486a1661ff1f32b5a8b17246150b200564ed90de3f102ec022b98077e079

Package: album
Version: 4.12-3
Installed-Size: 313
Maintainer: Joao Eriberto Mota Filho <eriberto@debian.org>
Architecture: all
Depends: perl, imagemagick
Recommends: album-data
Suggests: httpd, jhead, libav-tools
Description: HTML photo album generator with theme support
Homepage: http://marginalhacks.com/Hacks/album
Description-md5: 3eaaefa453087570fb45ac51eeccbe7c
Tag: implemented-in::perl, interface::commandline, role::program,
 scope::application, use::browsing, use::organizing, web::application,
 works-with-format::html, works-with::image, works-with::image:raster,
 works-with::text
Section: non-free/web
Priority: extra
Filename: pool/non-free/a/album/album_4.12-3_all.deb
Size: 89616
MD5sum: d99598b731d80b388fd25e90403d1dd0
SHA1: 85c58e53bc50513d372010fcf8062a9155e71a7e
SHA256: 328a6a5ef392372c51e5f60370277e74f21662cf7a9069cd64f62fb65651fda8

Package: album-data
Version: 4.05-5
Installed-Size: 7643
Maintainer: Joao Eriberto Mota Filho <eriberto@debian.org>
Architecture: all
Depends: album, libjs-swfobject
Description: themes, plugins and translations for album
Homepage: http://marginalhacks.com/Hacks/album
Description-md5: 34adea76df6b2c02712e3838461edbb2
Tag: role::app-data
Section: non-free/web
Priority: extra
Filename: pool/non-free/a/album-data/album-data_4.05-5_all.deb
Size: 5473382
MD5sum: 2154aeb5885ff823c29f729ac6adf90c
SHA1: f3655e6ba284da04a17bdd642a6ce41be9b869f6
SHA256: 91f5edbfa9d183d7807ec602b47825dae2f23a39db63773fff3344a43f10804c
"""


# Extract groups of non-blank lines,
# Where the Section is 'non-free/web',
# Split into individual lines,
# Take the one that's the package name,
# And print it.
fishrob(debian_package_file) \
    .x(r'(.+\n)+') \
    .g(r'Section: non-free/web') \
    .x(r'.+\n') \
    .g(r'^Package:') \
    .p()
# Should print album-data and album.
