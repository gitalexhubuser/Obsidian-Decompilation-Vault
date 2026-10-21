---
offset: "0x00878960"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00878960 — `MonitorDSPCallback`

- **Адрес (Offset):** `0x00878960`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00878960
static FMOD_RESULT F_CALLBACK MonitorDSPCallback(FMOD_DSP_STATE* dspState, float* inBuffer, float* outBuffer, unsigned int length, int inChannels, int outChannels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00878960 в IDA Pro / Ghidra
