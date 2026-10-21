---
offset: "0x009156c0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter_nrt.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009156c0 — `OutputWavWriter_NRT_initCallback`

- **Адрес (Offset):** `0x009156c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter_nrt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009156c0
FMOD_RESULT F_CALLBACK OutputWavWriter_NRT::initCallback(FMOD_OUTPUT_STATE *output, int selecteddriver, FMOD_INITFLAGS flags, int *outputrate, int outputchannels, FMOD_SOUND_FORMAT *outputformat, int dspbufferlength, int dspnumbuffers, void *extradriverdata)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009156c0 в IDA Pro / Ghidra
