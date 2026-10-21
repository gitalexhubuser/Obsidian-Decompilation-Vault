---
offset: "0x00888d30"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/ProtocolMeta.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00888d30 — `Optional_Optional`

- **Адрес (Offset):** `0x00888d30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/ProtocolMeta.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888d30
BSN::Protocol::Meta::Optional::Optional(const Protocol* protocol, uint32_t typeId) : Base(protocol, typeId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888d30 в IDA Pro / Ghidra
