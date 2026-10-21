---
offset: "0x006b1100"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1100 — `ClientConnection_PollStatus`

- **Адрес (Offset):** `0x006b1100`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1100
int32_t ClientConnection::PollStatus(WOWCS_OPS& op, const char** text, int32_t& result, int32_t& errorCode) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1100 в IDA Pro / Ghidra
