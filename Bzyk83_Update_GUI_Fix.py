#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Repair only the updater modal UI, preserving the currently configured update source."""
import os,sys,tempfile,base64,zlib
from pathlib import Path
DATA='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'

def atomic(path,data,mode):
 fd,tmp=tempfile.mkstemp(prefix='.bzyk83-modal-fix-',dir=str(path.parent))
 try:
  with os.fdopen(fd,'wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
  os.chmod(tmp,mode);os.replace(tmp,path)
 finally:
  if os.path.exists(tmp):os.unlink(tmp)

def main():
 plugin=Path('/usr/lib/enigma2/python/Plugins/Extensions/Bzyk83Downloader/plugin.py');helper=plugin.with_name('safe_update_ui.py')
 if not plugin.is_file():raise ValueError('Nie znaleziono wtyczki Bzyk83Downloader.')
 if os.geteuid()!=0:raise ValueError('Uruchom jako root.')
 old=plugin.read_bytes();text=old.decode('utf-8-sig')
 if 'Bzyk83PluginUpdater' not in text and '_bz_core' not in text:raise ValueError('Nie rozpoznano obslugi aktualizacji w tej wersji wtyczki.')
 marker='# BZYK83_MODAL_SAFE_UPDATE_HOTFIX'
 if marker not in text:text+='\n'+marker+'\nfrom . import safe_update_ui as _bzyk83_modal_fix\n_bzyk83_modal_fix.install(globals())\n'
 source=zlib.decompress(base64.b64decode(DATA));compile(text,str(plugin),'exec');compile(source,str(helper),'exec')
 saved=helper.read_bytes() if helper.exists() else None;mode=plugin.stat().st_mode&0o777
 try:atomic(helper,source,0o644);atomic(plugin,text.encode('utf-8'),mode)
 except Exception:
  atomic(plugin,old,mode)
  if saved is not None:atomic(helper,saved,0o644)
  elif helper.exists():helper.unlink()
  raise
 cache=plugin.parent/'__pycache__'
 if cache.is_dir():
  for p in cache.glob('*.pyc'):
   if p.name.startswith(('plugin.','safe_update_ui.')):p.unlink()
 print('GOTOWE: poprawiono kolejnosc otwierania okien aktualizacji.')
 print('Zrodlo aktualizacji, numer wersji, skrypty i bukiety nie zostaly zmienione.')
 print('Zrestartuj GUI, a nastepnie uruchom aktualizacje wtyczki z GitHuba.')
if __name__=='__main__':
 try:main()
 except Exception as error:print('BLAD poprawki GUI: '+str(error));raise SystemExit(1)
