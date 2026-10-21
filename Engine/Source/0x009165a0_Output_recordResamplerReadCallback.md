---
offset: "0x009165a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009165a0 — `Output_recordResamplerReadCallback`

- **Адрес (Offset):** `0x009165a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009165a0
FMOD_RESULT F_CALLBACK Output::recordResamplerReadCallback(FMOD_DSP_STATE *dsp_state, float *inbuffer, float *outbuffer, unsigned int length, int inchannels, int outchannels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009165a0 в IDA Pro / Ghidra
