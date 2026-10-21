---
offset: "0x0090ce80"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090ce80 — `FMOD_FLAC_WriteCallback`

- **Адрес (Offset):** `0x0090ce80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090ce80
static FLAC__StreamDecoderWriteStatus FMOD_FLAC_WriteCallback(const FLAC__StreamDecoder *decoder, const FLAC__Frame *frame, const FLAC__int32 * const buffer[], void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090ce80 в IDA Pro / Ghidra
