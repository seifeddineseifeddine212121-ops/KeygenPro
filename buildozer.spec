[app]
title = KeygenPro
package.name = keygenpro
package.domain = org.keygenpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.0
requirements = python3,kivy
icon.filename = apk_icon2.png
orientation = portrait
fullscreen = 0
android.permissions =
android.api = 34
android.minapi = 21
android.enable_androidx = True
android.gradle_dependencies = androidx.core:core:1.10.1
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
android.archs = arm64-v8a
android.allow_backup = True
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
