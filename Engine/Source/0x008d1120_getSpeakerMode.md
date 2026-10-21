---
offset: "0x008d1120"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_systemi.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008d1120 — `getSpeakerMode`

- **Адрес (Offset):** `0x008d1120`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_systemi.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008d1120
FMOD_RESULT       getSpeakerMode         (FMOD_SPEAKERMODE *speakermode) { if (!speakermode) { return FMOD_ERR_INVALID_PARAM; } *speakermode = mSpeakerMode; return FMOD_OK; }
```

## Исследование и заметки
- [ ] Открыть адрес 0x008d1120 в IDA Pro / Ghidra
