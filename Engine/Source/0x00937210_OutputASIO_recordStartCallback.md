---
offset: "0x00937210"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00937210 — `OutputASIO_recordStartCallback`

- **Адрес (Offset):** `0x00937210`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00937210
FMOD_RESULT F_CALLBACK OutputASIO::recordStartCallback(FMOD_OUTPUT_STATE *output, int id, FMOD_SOUND *sound, int loop)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00937210 в IDA Pro / Ghidra
