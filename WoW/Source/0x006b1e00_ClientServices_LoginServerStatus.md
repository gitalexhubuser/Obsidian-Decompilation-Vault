---
offset: "0x006b1e00"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1e00 — `ClientServices_LoginServerStatus`

- **Адрес (Offset):** `0x006b1e00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1e00
void ClientServices::LoginServerStatus(LOGIN_STATE state, LOGIN_RESULT result, const char* addressString, const char* stateString, const char* resultString, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1e00 в IDA Pro / Ghidra
