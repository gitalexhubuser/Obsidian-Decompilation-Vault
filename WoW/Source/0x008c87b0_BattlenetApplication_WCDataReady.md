---
offset: "0x008c87b0"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c87b0 — `BattlenetApplication_WCDataReady`

- **Адрес (Offset):** `0x008c87b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c87b0
void BattlenetApplication::WCDataReady(WowConnection* connection, uint32_t timeStamp, uint8_t* data, int32_t length) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c87b0 в IDA Pro / Ghidra
