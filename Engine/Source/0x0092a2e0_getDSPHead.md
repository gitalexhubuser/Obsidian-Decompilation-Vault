---
offset: "0x0092a2e0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_channel_openal.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092a2e0 — `getDSPHead`

- **Адрес (Offset):** `0x0092a2e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_channel_openal.h`

## Сигнатура C++
```cpp
// OFFSET: 0x0092a2e0
FMOD_RESULT  getDSPHead           (DSPI **dsp)      { *dsp = mDSPHead; return FMOD_OK; }
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092a2e0 в IDA Pro / Ghidra
