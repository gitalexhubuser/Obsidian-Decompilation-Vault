---
offset: "0x00926fd0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_codec.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00926fd0 — `DSPCodec_readCallback`

- **Адрес (Offset):** `0x00926fd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_codec.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00926fd0
FMOD_RESULT F_CALLBACK DSPCodec::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00926fd0 в IDA Pro / Ghidra
