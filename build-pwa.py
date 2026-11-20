#!/usr/bin/env python3
"""Genera docs/index.html (la app instalable) a partir de taller-excel.html.
Uso: python3 build-pwa.py"""
import re
src = open('taller-excel.html', encoding='utf8').read()
src = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', '', src)
src = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', '', src)
src = src.replace('https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js', 'vendor/xlsx.full.min.js')
src = src.replace('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js', 'vendor/chart.umd.min.js')
head = '''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1a7f4b">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Taller Excel">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);-webkit-text-size-adjust:100%}body{margin:0}[hidden]{display:none!important}button,.btn{-webkit-tap-highlight-color:transparent}</style>
</head><body>
'''
tail = '''
<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>
</body></html>
'''
open('docs/index.html', 'w', encoding='utf8').write(head + src + tail)
print('docs/index.html listo')
