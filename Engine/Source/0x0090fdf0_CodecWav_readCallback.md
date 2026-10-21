---
offset: "0x0090fdf0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_wav.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090fdf0 — `CodecWav_readCallback`

- **Адрес (Offset):** `0x0090fdf0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_wav.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090fdf0
FMOD_RESULT F_CALLBACK CodecWav::readCallback(FMOD_CODEC_STATE *codec, void *buffer, unsigned int sizebytes, unsigned int *bytesread)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090fdf0 в IDA Pro / Ghidra
