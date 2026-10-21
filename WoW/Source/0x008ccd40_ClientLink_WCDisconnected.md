---
offset: "0x008ccd40"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008ccd40 — `ClientLink_WCDisconnected`

- **Адрес (Offset):** `0x008ccd40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008ccd40
void Grunt::ClientLink::WCDisconnected(WowConnection* connection, uint32_t timeStamp, const NETCONNADDR* addr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008ccd40 в IDA Pro / Ghidra
