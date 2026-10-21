---
offset: "0x008f1780"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_highpass.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f1780 — `DSPHighPass_readCallback`

- **Адрес (Offset):** `0x008f1780`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_highpass.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008f1780
FMOD_RESULT F_CALLBACK DSPHighPass::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f1780 в IDA Pro / Ghidra
