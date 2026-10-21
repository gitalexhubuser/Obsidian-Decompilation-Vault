---
offset: "0x009160b0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009160b0 — `Output_getFreeChannel`

- **Адрес (Offset):** `0x009160b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009160b0
FMOD_RESULT Output::getFreeChannel(FMOD_MODE mode, ChannelReal **realchannel, int numchannels, int numsoundchannels, int *found)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009160b0 в IDA Pro / Ghidra
