---
offset: "0x008eaad0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_compressor.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008eaad0 — `DSPCompressor_readCallback`

- **Адрес (Offset):** `0x008eaad0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_compressor.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008eaad0
FMOD_RESULT F_CALLBACK DSPCompressor::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008eaad0 в IDA Pro / Ghidra
