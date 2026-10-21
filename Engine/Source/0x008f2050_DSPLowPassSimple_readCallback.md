---
offset: "0x008f2050"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_lowpass_simple.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f2050 — `DSPLowPassSimple_readCallback`

- **Адрес (Offset):** `0x008f2050`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_lowpass_simple.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008f2050
FMOD_RESULT F_CALLBACK DSPLowPassSimple::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f2050 в IDA Pro / Ghidra
