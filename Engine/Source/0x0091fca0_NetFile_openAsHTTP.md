---
offset: "0x0091fca0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_file_net.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0091fca0 — `NetFile_openAsHTTP`

- **Адрес (Offset):** `0x0091fca0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_file_net.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0091fca0
FMOD_RESULT NetFile::openAsHTTP(const char *name_or_data, char *host, char *file, char *auth, unsigned short port, unsigned int *filesize)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0091fca0 в IDA Pro / Ghidra
