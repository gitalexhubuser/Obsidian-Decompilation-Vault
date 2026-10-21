---
offset: "0x009c1610"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/Tumor.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c1610 — `Tumor_RecvDatagram`

- **Адрес (Offset):** `0x009c1610`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/Tumor.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c1610
bool Battlenet::Tumor::RecvDatagram(uint32_t connection, void* data, uint32_t size, const IP4::AddressPort& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c1610 в IDA Pro / Ghidra
