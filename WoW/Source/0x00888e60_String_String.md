---
offset: "0x00888e60"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/ProtocolMeta.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00888e60 — `String_String`

- **Адрес (Offset):** `0x00888e60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/ProtocolMeta.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00888e60
BSN::Protocol::Meta::String::String(const Protocol* protocol, uint32_t typeId) : Base(protocol, typeId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00888e60 в IDA Pro / Ghidra
