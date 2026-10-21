---
offset: "0x0092b2c0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092b2c0 — `OutputOpenAL_getFreeChannel`

- **Адрес (Offset):** `0x0092b2c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0092b2c0
FMOD_RESULT OutputOpenAL::getFreeChannel(FMOD_MODE mode, ChannelReal **realchannel, int numchannels, int numsoundchannels, int *found)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092b2c0 в IDA Pro / Ghidra
