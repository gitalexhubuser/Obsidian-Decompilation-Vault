---
offset: "0x0090cfc0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090cfc0 — `FMOD_FLAC_LengthCallback`

- **Адрес (Offset):** `0x0090cfc0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090cfc0
static FLAC__StreamDecoderLengthStatus FMOD_FLAC_LengthCallback(const FLAC__StreamDecoder *decoder, FLAC__uint64 *stream_length, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090cfc0 в IDA Pro / Ghidra
