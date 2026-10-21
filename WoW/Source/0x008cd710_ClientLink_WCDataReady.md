---
offset: "0x008cd710"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cd710 — `ClientLink_WCDataReady`

- **Адрес (Offset):** `0x008cd710`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cd710
void Grunt::ClientLink::WCDataReady(WowConnection* connection, uint32_t timeStamp, uint8_t* data, int32_t length) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cd710 в IDA Pro / Ghidra
