---
offset: "0x009c1ae0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/Tendril.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c1ae0 — `Interface_SendEvent`

- **Адрес (Offset):** `0x009c1ae0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/Tendril.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c1ae0
void Battlenet::Service::Interface::SendEvent(const uint8_t& eventType, const BSN::FourCC& eventId, const BSN::EncodedObject* data) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c1ae0 в IDA Pro / Ghidra
