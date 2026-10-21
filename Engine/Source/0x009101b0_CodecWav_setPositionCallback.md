---
offset: "0x009101b0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_wav.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009101b0 — `CodecWav_setPositionCallback`

- **Адрес (Offset):** `0x009101b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_wav.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009101b0
FMOD_RESULT F_CALLBACK CodecWav::setPositionCallback(FMOD_CODEC_STATE *codec, int subsound, unsigned int position, FMOD_TIMEUNIT postype)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009101b0 в IDA Pro / Ghidra
