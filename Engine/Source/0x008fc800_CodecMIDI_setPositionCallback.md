---
offset: "0x008fc800"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_midi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008fc800 — `CodecMIDI_setPositionCallback`

- **Адрес (Offset):** `0x008fc800`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_midi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008fc800
FMOD_RESULT F_CALLBACK CodecMIDI::setPositionCallback(FMOD_CODEC_STATE *codec, int subsound, unsigned int position, FMOD_TIMEUNIT postype)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008fc800 в IDA Pro / Ghidra
