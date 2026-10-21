---
offset: "0x008efd60"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_flange.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008efd60 — `DSPFlange_readCallback`

- **Адрес (Offset):** `0x008efd60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_flange.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008efd60
FMOD_RESULT F_CALLBACK DSPFlange::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008efd60 в IDA Pro / Ghidra
