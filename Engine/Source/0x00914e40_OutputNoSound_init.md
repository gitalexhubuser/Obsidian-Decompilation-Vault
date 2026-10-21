---
offset: "0x00914e40"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00914e40 — `OutputNoSound_init`

- **Адрес (Offset):** `0x00914e40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00914e40
FMOD_RESULT OutputNoSound::init(int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00914e40 в IDA Pro / Ghidra
