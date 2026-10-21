---
offset: "0x006b02c0"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b02c0 — `LogConnectionStatus`

- **Адрес (Offset):** `0x006b02c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b02c0
static void LogConnectionStatus(WOWCS_OPS op, int32_t errorCode, int32_t initiating, int32_t result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b02c0 в IDA Pro / Ghidra
