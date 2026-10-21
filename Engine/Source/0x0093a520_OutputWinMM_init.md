---
offset: "0x0093a520"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093a520 — `OutputWinMM_init`

- **Адрес (Offset):** `0x0093a520`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_winmm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093a520
FMOD_RESULT OutputWinMM::init(int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093a520 в IDA Pro / Ghidra
