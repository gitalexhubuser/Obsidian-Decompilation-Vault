---
offset: "0x00886e90"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatSoundCODEC.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00886e90 — `CODECIPMR6000_DecompressEncodedData`

- **Адрес (Offset):** `0x00886e90`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatSoundCODEC.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00886e90
bool ComSat::Sound::CODECIPMR6000::DecompressEncodedData(uint8_t player, int32_t channel, const uint8_t* data, uint32_t bits, uint8_t* pcm, uint32_t* size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00886e90 в IDA Pro / Ghidra
