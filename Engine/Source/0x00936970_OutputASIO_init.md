---
offset: "0x00936970"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00936970 — `OutputASIO_init`

- **Адрес (Offset):** `0x00936970`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_asio.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00936970
FMOD_RESULT OutputASIO::init(int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00936970 в IDA Pro / Ghidra
