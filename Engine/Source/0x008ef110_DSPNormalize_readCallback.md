---
offset: "0x008ef110"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_normalize.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008ef110 — `DSPNormalize_readCallback`

- **Адрес (Offset):** `0x008ef110`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_normalize.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008ef110
FMOD_RESULT F_CALLBACK DSPNormalize::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008ef110 в IDA Pro / Ghidra
