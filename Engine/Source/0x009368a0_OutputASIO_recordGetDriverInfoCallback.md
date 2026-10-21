---
offset: "0x009368a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009368a0 — `OutputASIO_recordGetDriverInfoCallback`

- **Адрес (Offset):** `0x009368a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009368a0
FMOD_RESULT F_CALLBACK OutputASIO::recordGetDriverInfoCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009368a0 в IDA Pro / Ghidra
