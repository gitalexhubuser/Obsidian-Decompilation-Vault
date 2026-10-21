---
offset: "0x00937d60"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00937d60 — `OutputWASAPI_initEx`

- **Адрес (Offset):** `0x00937d60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00937d60
FMOD_RESULT OutputWASAPI::initEx(int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, FMOD_SPEAKERMODE *speakermode, int dspbufferlength, int dspnumbuffers, int max2dchannels, int max3dchannels, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00937d60 в IDA Pro / Ghidra
