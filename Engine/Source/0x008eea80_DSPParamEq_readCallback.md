---
offset: "0x008eea80"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_parameq.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008eea80 — `DSPParamEq_readCallback`

- **Адрес (Offset):** `0x008eea80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_parameq.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008eea80
FMOD_RESULT F_CALLBACK DSPParamEq::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008eea80 в IDA Pro / Ghidra
