---
offset: "0x0090cf60"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0090cf60 — `FMOD_FLAC_SeekCallback`

- **Адрес (Offset):** `0x0090cf60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_codec_flac.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0090cf60
static FLAC__StreamDecoderSeekStatus FMOD_FLAC_SeekCallback(const FLAC__StreamDecoder *decoder, FLAC__uint64 absolute_byte_offset, void *client_data)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0090cf60 в IDA Pro / Ghidra
