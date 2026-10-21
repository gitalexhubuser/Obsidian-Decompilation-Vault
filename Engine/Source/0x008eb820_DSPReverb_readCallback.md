---
offset: "0x008eb820"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_reverb.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008eb820 — `DSPReverb_readCallback`

- **Адрес (Offset):** `0x008eb820`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_reverb.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008eb820
FMOD_RESULT F_CALLBACK DSPReverb::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008eb820 в IDA Pro / Ghidra
