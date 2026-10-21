---
offset: "0x00917aa0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00917aa0 — `FMOD_OS_CDDA_ReadSectors`

- **Адрес (Offset):** `0x00917aa0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00917aa0
FMOD_RESULT FMOD_OS_CDDA_ReadSectors(FMOD_CDDA_DEVICE *device, char *buf, unsigned int start_sector, unsigned int num_sectors)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00917aa0 в IDA Pro / Ghidra
