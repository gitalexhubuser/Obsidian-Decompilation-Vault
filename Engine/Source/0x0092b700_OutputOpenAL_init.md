---
offset: "0x0092b700"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092b700 — `OutputOpenAL_init`

- **Адрес (Offset):** `0x0092b700`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0092b700
FMOD_RESULT OutputOpenAL::init(int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092b700 в IDA Pro / Ghidra
