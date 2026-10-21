---
offset: "0x00917100"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00917100 — `FMOD_CDDA_IssueScsiCmd_Internal`

- **Адрес (Offset):** `0x00917100`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00917100
int FMOD_CDDA_IssueScsiCmd_Internal(FMOD_CDDA_DEVICE *cdrom, int flags, unsigned char *cdb_data, int cdb_len, char *buf, int buflen, unsigned char adapter_id, unsigned char target_id, unsigned char lun_id)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00917100 в IDA Pro / Ghidra
