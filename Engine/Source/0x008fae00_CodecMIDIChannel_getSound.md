---
offset: "0x008fae00"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_midi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008fae00 — `CodecMIDIChannel_getSound`

- **Адрес (Offset):** `0x008fae00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_midi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008fae00
FMOD_RESULT CodecMIDIChannel::getSound(int key, SoundI **sound, CodecDLSInstrument **instrument, int *unitynote, int *finetune, int *sampleattenuation, bool *duplicateallowed, int *keygroup, int *numarticulators, DLS_CONNECTIONBLOCK **articulators)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008fae00 в IDA Pro / Ghidra
