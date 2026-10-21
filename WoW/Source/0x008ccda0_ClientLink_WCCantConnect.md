---
offset: "0x008ccda0"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008ccda0 — `ClientLink_WCCantConnect`

- **Адрес (Offset):** `0x008ccda0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008ccda0
void Grunt::ClientLink::WCCantConnect(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008ccda0 в IDA Pro / Ghidra
