---
offset: "0x009c1250"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/Tumor.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c1250 — `Tumor_AllocEventAdapter`

- **Адрес (Offset):** `0x009c1250`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/Tumor.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c1250
Battlenet::Tumor::EventAdapter* Battlenet::Tumor::AllocEventAdapter(BSN::FourCC eventId, EventSubscriber& subscriber, const uint32_t& tendrilId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c1250 в IDA Pro / Ghidra
