---
offset: "0x0090ce40"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090ce40 — `FMOD_FLAC_ReadCallback`

- **Адрес (Offset):** `0x0090ce40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090ce40
static FLAC__StreamDecoderReadStatus FMOD_FLAC_ReadCallback(const FLAC__StreamDecoder *decoder, FLAC__byte buffer[], size_t *bytes, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090ce40 в IDA Pro / Ghidra
