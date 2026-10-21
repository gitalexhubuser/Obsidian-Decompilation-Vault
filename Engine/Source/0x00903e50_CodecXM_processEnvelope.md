---
offset: "0x00903e50"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_xm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00903e50 — `CodecXM_processEnvelope`

- **Адрес (Offset):** `0x00903e50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_xm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00903e50
FMOD_RESULT CodecXM::processEnvelope(MusicEnvelopeState *env, MusicVirtualChannel *vcptr, int Inumpoints, unsigned short *points, int type, int loopstart, int loopend, unsigned char ISustain, unsigned char control)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00903e50 в IDA Pro / Ghidra
