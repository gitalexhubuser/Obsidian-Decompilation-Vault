---
offset: "0x009c0cb0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/Tumor.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c0cb0 — `Adapter_RecvDatagram`

- **Адрес (Offset):** `0x009c0cb0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/Tumor.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c0cb0
bool Battlenet::Tumor::Adapter::RecvDatagram(uint32_t connection, void* data, uint32_t size, const IP4::AddressPort& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c0cb0 в IDA Pro / Ghidra
