---
offset: "0x00421f50"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/SFile2-Core.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00421f50 — `SFileAuthenticateArchiveEx`

- **Адрес (Offset):** `0x00421f50`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/SFile2-Core.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00421f50
int32_t STORMAPI SFileAuthenticateArchiveEx(SArchive* archive, uint32_t* result, const uint8_t* modulus, uint32_t modulusSize, const uint8_t* exponent, uint32_t exponentSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00421f50 в IDA Pro / Ghidra
