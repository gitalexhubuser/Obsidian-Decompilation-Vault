---
offset: "0x008da550"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_dspi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008da550 — `DSPI_calculateSpeakerLevels`

- **Адрес (Offset):** `0x008da550`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_dspi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008da550
FMOD_RESULT DSPI::calculateSpeakerLevels(float frontleft, float frontright, float center, float lfe, float backleft, float backright, float sideleft, float sideright, FMOD_SPEAKERMODE speakermode, int channels, FMOD_SPEAKERMAPTYPE speakermap, float *outlevels, int *numinputlevels)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008da550 в IDA Pro / Ghidra
