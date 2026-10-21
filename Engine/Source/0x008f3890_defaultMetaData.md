---
offset: "0x008f3890"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008f3890 — `defaultMetaData`

- **Адрес (Offset):** `0x008f3890`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codeci.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008f3890
static FMOD_INLINE FMOD_RESULT F_CALLBACK defaultMetaData     (FMOD_CODEC_STATE *codec, FMOD_TAGTYPE type, char *name, void *data, unsigned int datalen, FMOD_TAGDATATYPE datatype, int unique) { return ((Codec *)codec)->metaData(type, name, data, datalen, datatype, unique == 1 ? true : false); }
```

## Исследование и заметки
- [ ] Открыть адрес 0x008f3890 в IDA Pro / Ghidra
