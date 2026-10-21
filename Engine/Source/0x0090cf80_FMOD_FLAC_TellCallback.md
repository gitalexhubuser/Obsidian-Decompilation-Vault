---
offset: "0x0090cf80"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090cf80 — `FMOD_FLAC_TellCallback`

- **Адрес (Offset):** `0x0090cf80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090cf80
static FLAC__StreamDecoderTellStatus FMOD_FLAC_TellCallback(const FLAC__StreamDecoder *decoder, FLAC__uint64 *absolute_byte_offset, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090cf80 в IDA Pro / Ghidra
