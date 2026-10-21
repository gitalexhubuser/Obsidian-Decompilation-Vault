---
offset: "0x00888ec0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/ProtocolMeta.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00888ec0 — `String_IsValid`

- **Адрес (Offset):** `0x00888ec0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/ProtocolMeta.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888ec0
bool BSN::Protocol::Meta::String::IsValid(uint32_t length, const uint8_t* data, uint32_t& count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888ec0 в IDA Pro / Ghidra
