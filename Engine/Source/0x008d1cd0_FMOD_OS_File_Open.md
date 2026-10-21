---
offset: "0x008d1cd0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_misc.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d1cd0 — `FMOD_OS_File_Open`

- **Адрес (Offset):** `0x008d1cd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_misc.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008d1cd0
FMOD_RESULT FMOD_OS_File_Open(const char *name, char *mode, int unicode, unsigned int *filesize, void **handle)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d1cd0 в IDA Pro / Ghidra
