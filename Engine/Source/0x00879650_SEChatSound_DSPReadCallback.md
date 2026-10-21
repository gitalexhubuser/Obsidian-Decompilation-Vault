---
offset: "0x00879650"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00879650 — `SEChatSound_DSPReadCallback`

- **Адрес (Offset):** `0x00879650`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00879650
FMOD_RESULT F_CALLBACK SEChatSound::DSPReadCallback(FMOD_DSP_STATE* dspState, float* inBuffer, float* outBuffer, unsigned int length, int inChannels, int outChannels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00879650 в IDA Pro / Ghidra
