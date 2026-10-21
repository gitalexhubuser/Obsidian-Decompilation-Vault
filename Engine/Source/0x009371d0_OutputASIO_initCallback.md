---
offset: "0x009371d0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009371d0 — `OutputASIO_initCallback`

- **Адрес (Offset):** `0x009371d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009371d0
FMOD_RESULT F_CALLBACK OutputASIO::initCallback(FMOD_OUTPUT_STATE *output, int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009371d0 в IDA Pro / Ghidra
