---
offset: "0x008f5200"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_oscillator.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f5200 — `DSPOscillator_readCallback`

- **Адрес (Offset):** `0x008f5200`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_oscillator.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008f5200
FMOD_RESULT F_CALLBACK DSPOscillator::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f5200 в IDA Pro / Ghidra
