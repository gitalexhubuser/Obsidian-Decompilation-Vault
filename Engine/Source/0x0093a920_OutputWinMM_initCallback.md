---
offset: "0x0093a920"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093a920 — `OutputWinMM_initCallback`

- **Адрес (Offset):** `0x0093a920`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093a920
FMOD_RESULT F_CALLBACK OutputWinMM::initCallback(FMOD_OUTPUT_STATE *output, int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093a920 в IDA Pro / Ghidra
