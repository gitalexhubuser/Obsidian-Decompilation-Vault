---
offset: "0x00914ff0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00914ff0 — `OutputNoSound_initCallback`

- **Адрес (Offset):** `0x00914ff0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00914ff0
FMOD_RESULT F_CALLBACK OutputNoSound::initCallback(FMOD_OUTPUT_STATE *output, int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00914ff0 в IDA Pro / Ghidra
