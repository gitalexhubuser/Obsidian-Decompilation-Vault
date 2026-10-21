---
offset: "0x0090d040"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090d040 — `FMOD_FLAC_MetadataCallback`

- **Адрес (Offset):** `0x0090d040`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090d040
static void FMOD_FLAC_MetadataCallback(const FLAC__StreamDecoder *decoder, const FLAC__StreamMetadata *metadata, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090d040 в IDA Pro / Ghidra
