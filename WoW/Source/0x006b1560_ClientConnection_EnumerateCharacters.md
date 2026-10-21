---
offset: "0x006b1560"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1560 — `ClientConnection_EnumerateCharacters`

- **Адрес (Offset):** `0x006b1560`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1560
int32_t ClientConnection::EnumerateCharacters(void (*callback)(CHARACTER_INFO& info, void* param), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1560 в IDA Pro / Ghidra
