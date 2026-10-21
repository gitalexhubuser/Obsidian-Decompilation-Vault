---
offset: "0x008ef440"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_dsp_distortion.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008ef440 — `DSPDistortion_readCallback`

- **Адрес (Offset):** `0x008ef440`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_dsp_distortion.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008ef440
FMOD_RESULT F_CALLBACK DSPDistortion::readCallback(FMOD_DSP_STATE *dsp, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008ef440 в IDA Pro / Ghidra
