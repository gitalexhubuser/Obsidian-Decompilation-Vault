---
offset: "0x0093cd10"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dsp_convert.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0093cd10 — `DSPI_convert`

- **Адрес (Offset):** `0x0093cd10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dsp_convert.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0093cd10
FMOD_RESULT DSPI::convert(void *outbuffer, void *inbuffer, FMOD_SOUND_FORMAT outformat, FMOD_SOUND_FORMAT informat, unsigned int length, int destchannelstep, int srcchannelstep, float volume)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0093cd10 в IDA Pro / Ghidra
