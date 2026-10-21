---
offset: "0x008f3760"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_lowpass.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f3760 — `DSPLowPass_readCallback`

- **Адрес (Offset):** `0x008f3760`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_lowpass.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008f3760
FMOD_RESULT F_CALLBACK DSPLowPass::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f3760 в IDA Pro / Ghidra
