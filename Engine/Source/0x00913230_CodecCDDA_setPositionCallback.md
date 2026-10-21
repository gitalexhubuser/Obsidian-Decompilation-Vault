---
offset: "0x00913230"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_codec_cdda.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00913230 — `CodecCDDA_setPositionCallback`

- **Адрес (Offset):** `0x00913230`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_codec_cdda.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00913230
FMOD_RESULT F_CALLBACK CodecCDDA::setPositionCallback(FMOD_CODEC_STATE *codec, int subsound, unsigned int position, FMOD_TIMEUNIT postype)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00913230 в IDA Pro / Ghidra
