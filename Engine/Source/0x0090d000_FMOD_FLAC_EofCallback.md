---
offset: "0x0090d000"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090d000 — `FMOD_FLAC_EofCallback`

- **Адрес (Offset):** `0x0090d000`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090d000
static FLAC__bool FMOD_FLAC_EofCallback(const FLAC__StreamDecoder *decoder, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090d000 в IDA Pro / Ghidra
