[app]
title = Lilit Pro
package.name = lilitpro
package.domain = org.isa
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 6.0
requirements = python3,kivy,pyjnius,requests,urllib3,charset-normalizer,idna,openssl,certifi
orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK, VIBRATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
fullscreen = 1
android.theme = @android:style/Theme.NoTitleBar.Fullscreen
[buildozer]
log_level = 2
warn_on_root = 1
