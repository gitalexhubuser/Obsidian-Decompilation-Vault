---
offset: "0x009c0ff0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/Tumor.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c0ff0 — `Adapter_SendDatagram`

- **Адрес (Offset):** `0x009c0ff0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/Tumor.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c0ff0
bool Battlenet::Tumor::Adapter::SendDatagram(uint32_t connection, const void* data, uint32_t size, const IP4::AddressPort& address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c0ff0 в IDA Pro / Ghidra
