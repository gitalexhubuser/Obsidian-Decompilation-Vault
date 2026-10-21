---
offset: "0x009bfe80"
module: "WoW/Source"
file: "WoW/Source/Battlenet/Tumor/TumorManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009bfe80 — `TumorManager_SendEvent`

- **Адрес (Offset):** `0x009bfe80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/Tumor/TumorManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009bfe80
void Battlenet::TumorManager::SendEvent(uint8_t eventType, const BSN::FourCC& eventId, const BSN::EncodedObject* data) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009bfe80 в IDA Pro / Ghidra
