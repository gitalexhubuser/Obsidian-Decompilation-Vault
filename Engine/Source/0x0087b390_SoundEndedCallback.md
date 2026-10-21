---
offset: "0x0087b390"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087b390 — `SoundEndedCallback`

- **Адрес (Offset):** `0x0087b390`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087b390
static FMOD_RESULT F_CALLBACK SoundEndedCallback(FMOD_CHANNEL* channel, FMOD_CHANNEL_CALLBACKTYPE type, int command, unsigned int commanddata1, unsigned int commanddata2) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087b390 в IDA Pro / Ghidra
