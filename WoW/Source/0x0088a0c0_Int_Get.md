---
offset: "0x0088a0c0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/ProtocolType.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0088a0c0 — `Int_Get`

- **Адрес (Offset):** `0x0088a0c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/ProtocolType.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0088a0c0
void BSN::Protocol::Type::Int::Get(int32_t intType, const uint8_t*& cursor, uint32_t& value) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0088a0c0 в IDA Pro / Ghidra
